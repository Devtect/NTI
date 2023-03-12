from dataclasses import dataclass

@dataclass

class fighter:
    name: str
    attack: int
    defense: int
    level: int
    boost: int

    def __str__(self):
        return f"Name: {self.name} -- Level: {self.level}"


@dataclass
class boss:
    name: str
    attack: int
    defense: int
    level: int
    boost: int

    def __str__(self):
        return f"Name: {self.name} -- Level: {self.level}" 