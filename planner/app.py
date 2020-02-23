from typing import List, Dict, Tuple
import json
import io

from flask import Flask, jsonify, request, Response, make_response
from werkzeug.wsgi import FileWrapper
import numpy as np
from PIL import Image

from planner import Planner
from planner.config import COORDINATE_PATH, MAP_PATH
from planner.kinds import Car, Robot, Tile
from planner.detector import getEmptySpaces, captureImage, annotateEmptySpaces

app = Flask(__name__)
THRESHOLD = 0.01


@app.route("/")
def index_view():
    return make_response(""" \
You probably meant one of the following:
<ul>
    <li><a href="/emptymap">/emptymap</a> &mdash; See the annotated image</li>
    <li><a href="/plan">/plan</a> &mdash; Run the planner
        <b>GET Parameters</b>
        <ul>
            <li><b><tt>robot</tt></b><tt>=row,column</tt> &ndash; The position of the Robot. {1}</li>
            <li><b><tt>parkCar</tt></b><tt>=row,column</tt> &ndash; The position of a Car to be parked. [1, ∞)</li>
            <li><b><tt>deliverCar</tt></b><tt>=row,column</tt> &ndash; The position of a Car to be delivered. [1, ∞)</li>
        </ul>
    </li>
</ul>
""")


@app.route("/emptymap")
def emptymap_view():
    coordinates = load_coordinates(COORDINATE_PATH)
    image = captureImage()
    result = annotateEmptySpaces(image, coordinates, THRESHOLD)
    im = Image.fromarray(
        (255.0 / result.max() * (result - result.min())).astype(np.uint8)
    )

    bio = io.BytesIO()
    im.save(bio, "png")
    bio.seek(0)
    w = FileWrapper(bio)
    return Response(w, mimetype="image/png", direct_passthrough=True)


@app.route("/plan")
def plan_view():
    map_ = load_map(MAP_PATH)
    coordinates = load_coordinates(COORDINATE_PATH)

    image = captureImage()
    if image is None:
        return jsonify({
            "error": "image is None"
        })
    is_empty_map = getEmptySpaces(image, coordinates, THRESHOLD)

    for tile in map_:
        if not is_empty_map.get((tile.row, tile.column), True):
            tile.is_temporarily_blocked = True

    robot, cars = parse_args(request.args)

    p = Planner()
    plan = p.plan(
        tiles=map_,
        cars=cars,
        robot=robot
    )
    return jsonify({
        "plan": plan,
        "is_empty": {f"R{k[0]}C{k[1]}": bool(v) for k, v in is_empty_map.items()}
    })


def parse_args(args):
    robot_row, robot_column = args["robot"].split(",")
    park_cars = [c.split(",") for c in args.getlist("parkCar")]
    deliver_cars = [c.split(",") for c in args.getlist("deliverCar")]

    return (
        Robot(float(robot_row), float(robot_column)),
        [
            Car(int(t[0]), int(t[1]), Car.CarStatus.AWAITING_PARKING)
            for t in park_cars
        ] + [
            Car(int(t[0]), int(t[1]), Car.CarStatus.AWAITING_DELIVERY)
            for t in deliver_cars
        ],
    )


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


def load_map(map_path: str) -> List[Tile]:
    with open(map_path) as f:
        return [Tile.from_dict(d) for d in json.load(f)]


def load_coordinates(path: str) -> Dict[Tuple[int, int], np.ndarray]:
    with open(path) as f:
        list_ = json.load(f)
        return {
            (e["row"], e["column"]): np.array(e["coordinates"])
            for e in list_
        }
