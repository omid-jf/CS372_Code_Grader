#  ============================================================
#  This file is part of the CS372_Code_Grader project.
#
#  Author: Omid Jafari - omidjafari.com
#  Copyright (c) 2022
#
#  For the full copyright and license information, please view
#  the LICENSE file that was distributed with this source code.
#  ============================================================

def str_to_int_list(input1: str) -> list[int]:
    return [int(x) for x in input1.split(",")]


def str_to_2d_int_list(input1: str) -> list[list[int]]:
    return [[int(x) for x in sublist.split(",")] for sublist in input1.split("|")]
