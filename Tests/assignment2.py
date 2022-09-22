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
            "0->1,0->2,1->2,2->0,2->3,3->3",
            1
        ],
        "outputs": ["1,2,0,3"]
    },
    {
        "inputs": [
            "2->0,0->2,1->2,0->1,3->3,1->3",
            2
        ],
        "outputs": ["2,0,1,3"]
    },
    {
        "inputs": [
            "0->1,0->2,0->3,1->4,2->4,3->4",
            0
        ],
        "outputs": ["0,1,4,2,3"]
    },
]

question2 = [
    {
        "inputs": [
            "0->1,0->2,1->2",
        ],
        "outputs": ["No"]
    },
    {
        "inputs": [
            "0->1,2->0,1->2",
        ],
        "outputs": ["Yes"]
    },
    {
        "inputs": [
            "0->1,0->2,1->2,2->0,2->3,3->3",
        ],
        "outputs": ["Yes"]
    },
    {
        "inputs": [
            "0->1,0->2,1->2,2->3",
        ],
        "outputs": ["No"]
    },
]

question3 = [
    {
        "inputs": [
            [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]],
        ],
        "outputs": [5]
    },
    {
        "inputs": [
            [[1, 1, 1, 1, 0],
             [1, 1, 0, 1, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]],
        ],
        "outputs": [1]
    },
    {
        "inputs": [
            [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1]],
        ],
        "outputs": [1]
    },
]

questions = [question1,
             question2,
             question3]
