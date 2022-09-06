//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

public class utils {
    public static int[] str_to_int_array(String input) {
        String[] tokens = input.split(",");
        int[] output = new int[tokens.length];

        for (int i = 0; i < tokens.length; i++)
            output[i] = Integer.parseInt(tokens[i]);

        return output;
    }
}
