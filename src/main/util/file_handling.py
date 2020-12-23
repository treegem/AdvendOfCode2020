from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename) as input_file:
        return input_file.readlines()


def read_file_stripped(filename: str) -> List[str]:
    return [line.strip() for line in read_file(filename)]
