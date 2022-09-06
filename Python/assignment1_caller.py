#  ============================================================
#  This file is part of the CS372_Code_Grader project.
#
#  Author: Omid Jafari - omidjafari.com
#  Copyright (c) 2022
#
#  For the full copyright and license information, please view
#  the LICENSE file that was distributed with this source code.
#  ============================================================

import sys
from utils import str_to_int_list
import importlib.util
from pathlib import Path


def question1_caller(input1: list[int]):
    output = question1(input1)
    print(f"Question1: {output}")


def question2_caller(input1: list[int]):
    output = question2(input1)
    print(f"Question2: {output}")


def question3_caller(input1: list[int]):
    output = question3(input1)
    print(f"Question3: {output}")


def question4_caller(input1: list[int], input2: list[int], input3: int):
    output = question4(input1, input2, input3)
    print(f"Question4: {output}")


def main():
    student_code_path = Path(sys.argv[1])
    spec = importlib.util.spec_from_file_location("py_code", student_code_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    globals().update(vars(foo))

    if sys.argv[2] == "question1":
        question1_caller(str_to_int_list(sys.argv[3]))

    elif sys.argv[2] == "question2":
        question2_caller(str_to_int_list(sys.argv[3]))

    elif sys.argv[2] == "question3":
        question3_caller(str_to_int_list(sys.argv[3]))

    elif sys.argv[2] == "question4":
        question4_caller(str_to_int_list(sys.argv[3]), str_to_int_list(sys.argv[4]), int(sys.argv[5]))

    else:
        raise Exception("Question number not given.")


if __name__ == "__main__":
    main()
