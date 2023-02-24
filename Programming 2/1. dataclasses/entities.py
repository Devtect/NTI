from dataclasses import dataclass


@dataclass
class Player:

    name: str
    attack: int
    hp: int
    maxhp: int

    def __str__(self) -> str:
        return f"Name: {self.name} Health: {self.hp}"


@dataclass
class Enemy:

    name: str
    attack: int
    hp: int
    maxhp: int

    def __str__(self) -> str:
        return f"Name: {self.name} Health: {self.hp}"


@dataclass
class Healer:

    name: str
    attack: int
    hp: int
    maxhp: int
    heal_amount: int

    def __str__(self) -> str:
        return f"Name: {self.name} Health: {self.hp}"
