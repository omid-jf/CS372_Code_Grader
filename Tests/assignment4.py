#  ============================================================
#  This file is part of the CS372_Code_Grader project.
#
#  Author: Omid Jafari - omidjafari.com
#  Copyright (c) 2022
#
#  For the full copyright and license information, please view
#  the LICENSE file that was distributed with this source code.
#  ============================================================

question1 = [
    {
        "inputs": [
            "60:10,100:20,120:30",
            50
        ],
        "outputs": [240]
    },
    {
        "inputs": [
            "280:40,100:10,120:20,120:24",
            60
        ],
        "outputs": [440]
    },
    {
        "inputs": [
            "20:4,18:3,14:2",
            7
        ],
        "outputs": [42]
    },
]

question2 = [
    {
        "inputs": [
            "0-1(4),1-2(3),1-3(2),1-4(3),2-4(5),4-3(1),0-2(2),2-3(4)",
        ],
        "outputs": ["0-2(2),1-2(3),1-3(2),4-3(1)"]
    },
    {
        "inputs": [
            "0-1(10),0-2(6),0-3(5),1-3(15),2-3(4)",
        ],
        "outputs": ["0-1(10),0-3(5),2-3(4)"]
    },
]

question3 = [
    {
        "inputs": [
            [6, 14, 21, 1],
            [15, 7, 10, 10]
        ],
        "outputs": [21]
    },
    {
        "inputs": [
            [1, 2, 3],
            [1, 100, 3]
        ],
        "outputs": [-1]
    },
    {
        "inputs": [
            [6, 14, 21, 10],
            [15, 7, 10, 10]
        ],
        "outputs": [-1]
    },
    {
        "inputs": [
            [11, 18, 26, 6, 25],
            [15, 8, 10, 10, 1]
        ],
        "outputs": [26]
    },
]

questions = [question1,
             question2,
             question3]
