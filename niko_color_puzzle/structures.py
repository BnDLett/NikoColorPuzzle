from abc import ABC
from random import choice

class Color(ABC):
    representation: str

    @staticmethod
    def compare(color: type["Color"], other: str) -> bool:
        """
        Compares the first letter of `other` and the specified color.
        :param color: The color to compare to.
        :param other: The string being compared to.
        :return: True if they have the same first letter representation; otherwise false.
        """
        return other[0] == color.representation[0]

    def __format__(self, format_spec):
        if format_spec == 'full':
            return f'{self.representation}'

        return self.representation[0]

    def __eq__(self, other: "Color"):
        return self.representation.lower() == other.representation.lower()

class Puzzle:
    answer: list[type[Color]]

    def __init__(self, answer: list[type[Color]]):
        self.answer = answer

    def confirm_answer(self, answer: list[str]) -> int:
        correct_count = 0
        iterations = min(len(answer), len(self.answer))

        for i in range(iterations):
            if Color.compare(self.answer[i], answer[i]):
                correct_count += 1

        return correct_count

    @staticmethod
    def generate(length: int) -> "Puzzle":
        answer: list[type[Color]] = list()

        for _ in range(abs(length)):
            color: type[Color] = choice(Color.__subclasses__())
            answer.append(color)

        return Puzzle(answer)
