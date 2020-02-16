from typing import Iterable


class PddlObject:
    def __init__(self, name: str, type_: str):
        self.name = name
        self.type = type_

    def __str__(self):
        return f"{self.name} - {self.type}"


class PddlStatement:
    def __init__(self, predicate: str, *args: Iterable[str]):
        self.predicate = predicate
        self.args = args

    def __str__(self):
        return "({} {})".format(self.predicate, ' '.join(self.args))
