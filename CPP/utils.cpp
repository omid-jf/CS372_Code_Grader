//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

#include "utils.h"

std::vector<int> str_to_int_vector(const std::string& input) {
    std::vector<int> output;
    int val;
    char comma;

    std::stringstream sstream(input);

    while (sstream >> val) {
        output.push_back(val);
        sstream >> comma;
    }

    return output;
}


std::vector<std::vector<int>> str_to_2d_int_vector(const std::string& input) {
    std::vector<std::vector<int>> output;
    std::vector<int> tmp_vec;
    int i_val;
    char c_val;

    std::stringstream sstream(input);

    while (sstream >> i_val) {
        tmp_vec.push_back(i_val);
        sstream >> c_val;

        if (c_val == '|') {
            output.push_back(tmp_vec);
            tmp_vec.clear();
        }
    }

    output.push_back(tmp_vec);

    return output;
}
