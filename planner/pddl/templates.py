from typing import List, Iterable

import pystache

from planner.pddl.kinds import PddlObject, PddlStatement


class ProblemTemplate:
    def __init__(self, path: str):
        with open(path) as f:
            self.template = f.read()
            self.renderer = pystache.Renderer()

    def render(self, objects: List[PddlObject], init: List[PddlStatement]) -> str:
        return pystache.render(self.template, {
            "objects": self.__concat_pretty(str(obj) for obj in objects),
            "init": self.__concat_pretty(str(i) for i in init),
        })

    @staticmethod
    def __concat_pretty(xs: Iterable[str], indent: str = " " * 8):
        return indent + ("\n" + indent).join(xs)
