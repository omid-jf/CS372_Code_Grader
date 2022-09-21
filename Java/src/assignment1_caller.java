//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

import static assignment1.assignment1.*;

public class assignment1_caller {
    private static void question1_caller(int[] input1) {
        int output = question1(input1);
        System.out.println("Question1: " + output);
    }

    private static void question2_caller(int[] input1) {
        int output = question2(input1);
        System.out.println("Question2: " + output);
    }

    private static void question3_caller(int[] input1) {
        String output = question3(input1);
        System.out.println("Question3: " + output);
    }

    private static void question4_caller(int[] input1, int[] input2, int input3) {
        int output = question4(input1, input2, input3);
        System.out.println("Question4: " + output);
    }

    public static void main(String[] args) {
        switch (args[0]) {
            case "question1":
            	question1_caller(utils.str_to_int_array(args[1]));
            	break;
            case "question2":
            	question2_caller(utils.str_to_int_array(args[1]));
            	break;
            case "question3":
            	question3_caller(utils.str_to_int_array(args[1]));
            	break;
            case "question4":
            	question4_caller(
                    utils.str_to_int_array(args[1]),
                    utils.str_to_int_array(args[2]),
                    Integer.parseInt(args[3])
            	);
            	break;
            default -> throw new RuntimeException("Question number not given.");
        }
    }
}