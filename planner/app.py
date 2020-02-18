from typing import List, Dict, Tuple
import json

from flask import Flask, jsonify, request, send_file
import numpy as np
from PIL import Image

from planner import Planner
from planner.config import COORDINATE_PATH, MAP_PATH
from planner.kinds import Car, Robot, Tile
from planner.detector import getEmptySpaces, captureImage, annotateEmptySpaces

app = Flask(__name__)


@app.route("/emptymap")
def emptymap():
    map_ = load_map(MAP_PATH)
    coordinates = load_coordinates(COORDINATE_PATH)

    image = captureImage()
    if image is None:
        return jsonify({
            "error": "image is None"
        })
    result = annotateEmptySpaces(image, coordinates)

    im = Image.fromarray(
        (255.0 / result.max() * (result - result.min())).astype(np.uint8)
    )
    im.save("anan.png")

    return send_file("../anan.png")


@app.route("/plan")
def plan():
    map_ = load_map(MAP_PATH)
    coordinates = load_coordinates(COORDINATE_PATH)

    image = captureImage()
    if image is None:
        return jsonify({
            "error": "image is None"
        })
    is_empty_map = getEmptySpaces(image, coordinates)

    print(is_empty_map)
    for tile in map_:
        if not is_empty_map.get((tile.y, tile.x), True):
            tile.is_temporarily_blocked = True

    for tile in map_:
        print("~~~ R%dC%d  %s" %(tile.y, tile.x, tile.is_temporarily_blocked))

    robot, cars = parse_args(request.args)

    p = Planner()
    plan = p.plan(
        tiles=map_,
        cars=cars,
        robot=robot
    )
    return jsonify({
        "plan": plan,
        "is_empty": {str(k): bool(v) for k,v in is_empty_map.items()}
    })


def parse_args(args):
    robot_x, robot_y = request.args["robot"].split(",")
    park_cars = [c.split(",") for c in request.args.getlist("parkCar")]
    deliver_cars = [c.split(",") for c in request.args.getlist("deliverCar")]

    return (
        Robot(float(robot_x), float(robot_y)),
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
        d = json.load(f)
        for k in list(d.keys()):
            v = d[k]
            del d[k]
            d[tuple(int(e) for e in k.split(","))] = np.array(v)
        return d
