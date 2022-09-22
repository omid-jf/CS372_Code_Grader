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

    public static int[][] str_to_2d_int_array(String input) {
        String[] sub_arrs = input.split("\\|");
        String[] arr = sub_arrs[0].split(",");
        int[][] output = new int[sub_arrs.length][arr.length];

        for (int i = 0; i < sub_arrs.length; i++) {
            arr = sub_arrs[i].split(",");

            for (int j = 0; j < arr.length; j++)
                output[i][j] = Integer.parseInt(arr[j]);
        }

        return output;
    }
}
