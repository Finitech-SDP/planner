"""
Author: Bora M. Alper <s1739976@ed.ac.uk>
"""
from typing import List

import contextlib
import os
import subprocess
import sys
import tempfile

from planner.config import DOMAIN_PATH, PROBLEM_TEMPLATE_PATH
from planner.kinds import Tile, Car, Robot
from planner.pddl.templates import ProblemTemplate
from planner.pddl.kinds import PddlObject, PddlStatement


class Planner:
    def __init__(self):
        self.problem_template = ProblemTemplate(PROBLEM_TEMPLATE_PATH)
        with open(DOMAIN_PATH) as f:
            self.domain = f.read()

    def plan(self, tiles: List[Tile], cars: List[Car], robot: Robot) -> List[str]:
        problem = self.problem_template.render(
            objects=[PddlObject(f"Car{i}", "car") for i, _ in enumerate(cars)],
            init=[
                     PddlStatement("IsAt", "Robot", f"R{int(robot.row)}C{int(robot.column)}")
                 ] + [
                     PddlStatement("IsAt", f"Car{i}", f"R{car.row}C{car.column}")
                     for i, car in enumerate(cars)
                 ] + [
                     PddlStatement("AwaitingParking", f"Car{i}")
                     for i, car in enumerate(cars)
                     if car.status == Car.CarStatus.AWAITING_PARKING
                 ] + [
                     PddlStatement("AwaitingDelivery", f"Car{i}")
                     for i, car in enumerate(cars)
                     if car.status == Car.CarStatus.AWAITING_DELIVERY
                 ] + [
                     PddlStatement("TemporarilyBlocked", f"R{tile.row}C{tile.column}")
                     for tile in tiles
                     if tile.is_temporarily_blocked
                 ],
        )
        return self.__call_planner(self.domain, problem)

    @staticmethod
    def __call_planner(domain: str, problem: str) -> List[str]:
        domain_f = None
        problem_f = None
        plan_f = None

        try:
            domain_f = tempfile.NamedTemporaryFile("w+")
            problem_f = tempfile.NamedTemporaryFile("w+")
            plan_f = tempfile.NamedTemporaryFile("w+")

            domain_f.write(domain)
            problem_f.write(problem)

            domain_f.flush()
            problem_f.flush()

            subprocess.check_output(
                [config.PLANNER_PATH,
                 "--domain", domain_f.name,
                 "--problem", problem_f.name,
                 "--output", plan_f.name],
                stderr=subprocess.STDOUT
            )
            plan_f.seek(0)
            return list(filter(None, plan_f.read().split("\n")))
        except subprocess.CalledProcessError as exc:
            print(exc.stdout, file=sys.stderr, flush=True)
            print(file=sys.stderr, flush=True)
            print(problem, file=sys.stderr, flush=True)
            print(file=sys.stderr, flush=True)
            raise exc
        finally:
            with contextlib.suppress(Exception):
                os.unlink("execution.details")
            domain_f.close()
            problem_f.close()
            plan_f.close()
