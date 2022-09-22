//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

#include "assignment2.h"
#include "utils.h"

void question1_caller(const std::string& input1, int input2) {
    std::string output = question1(input1, input2);
    std::cout << "Question1: " << output << std::endl;
}

void question2_caller(const std::string& input1) {
    std::string output = question2(input1);
    std::cout << "Question2: " << output << std::endl;
}

void question3_caller(const std::vector<std::vector<int>>& input1) {
    int output = question3(input1);
    std::cout << "Question3: " << output << std::endl;
}


int main(int argc, char** argv) {
    std::vector<std::string> all_args(argv, argv + argc);

    if (all_args[1] == "question1")
        question1_caller(all_args[2], std::stoi(all_args[3]));

    else if (all_args[1] == "question2")
        question2_caller(all_args[2]);

    else if (all_args[1] == "question3")
        question3_caller(str_to_2d_int_vector(all_args[2]));

    else
        throw std::runtime_error("question number not given.");
}