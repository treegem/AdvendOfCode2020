import numpy as np


class Day1Solver:

    def __init__(self):
        self.input = np.loadtxt("input.txt", dtype=np.int)

    def solve_for_two_numbers(self):
        for i_number1, number1 in enumerate(self.input):
            for number2 in self.input[i_number1:]:
                summed = number1 + number2
                if summed == 2020:
                    return print("solution for two numbers:", number1 * number2)
        return print("no solution found")

    def solve_for_three_numbers(self):
        for i_number1, number1 in enumerate(self.input):
            for i_number2, number2 in enumerate(self.input[i_number1:]):
                for number3 in self.input[i_number2:]:
                    summed = number1 + number2 + number3
                    if summed == 2020:
                        return print("solution for two numbers:", number1 * number2 * number3)
        return print("no solution found")


if __name__ == '__main__':
    solver = Day1Solver()
    solver.solve_for_two_numbers()
    solver.solve_for_three_numbers()
