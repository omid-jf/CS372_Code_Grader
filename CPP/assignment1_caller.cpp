//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

#include "assignment1.h"
#include "utils.h"

void question1_caller(const std::vector<int>& input1) {
    int output = question1(input1);
    std::cout << "Question1: " << output << std::endl;
}

void question2_caller(const std::vector<int>& input1) {
    int output = question2(input1);
    std::cout << "Question2: " << output << std::endl;
}

void question3_caller(const std::vector<int>& input1) {
    std::string output = question3(input1);
    std::cout << "Question3: " << output << std::endl;
}

void question4_caller(const std::vector<int>& input1, const std::vector<int>& input2, int input3) {
    int output = question4(input1, input2, input3);
    std::cout << "Question4: " << output << std::endl;
}

int main(int argc, char** argv) {
    std::vector<std::string> all_args(argv, argv + argc);

    if (all_args[1] == "question1")
        question1_caller(str_to_int_vector(all_args[2]));

    else if (all_args[1] == "question2")
        question2_caller(str_to_int_vector(all_args[2]));

    else if (all_args[1] == "question3")
        question3_caller(str_to_int_vector(all_args[2]));

    else if (all_args[1] == "question4")
        question4_caller(
                str_to_int_vector(all_args[2]),
                str_to_int_vector(all_args[3]),
                std::stoi(all_args[4])
                );

    else
        throw std::runtime_error("question number not given.");
}