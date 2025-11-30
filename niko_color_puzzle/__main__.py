from niko_color_puzzle.structures import Puzzle
from niko_color_puzzle import standard_colors


def input_loop(puzzle: Puzzle, counter: int) -> bool:
    """
    The loop for the user input.
    :param puzzle: The puzzle object itself.
    :return: True if the loop should continue; false if it shouldn't.
    """
    answer = input(f"Type in your answer (attempt {counter}): ")
    correct_count = puzzle.confirm_answer(list(answer))

    if correct_count == 5:
        print("All colors are correct.")
        return False

    print(f"{correct_count} colors are correct.")
    return True

def main():
    standard_colors.init()
    puzzle = Puzzle.generate(5)
    run_loop = True
    counter = 1

    print("Welcome to the NikoColorPuzzle game. When you're typing in your answer, make sure you only type the first "
          "letter of each color without any spaces. For example: BBPPO; which is: blue blue pink pink orange.")

    while run_loop:
        run_loop = input_loop(puzzle, counter)
        counter += 1

    print(f"Congratulations! You won. It took... {counter} tries. Impressive!")

main()
