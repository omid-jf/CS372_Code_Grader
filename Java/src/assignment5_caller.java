//  ============================================================
//  This file is part of the CS372_Code_Grader project.
//
//  Author: Omid Jafari - omidjafari.com
//  Copyright (c) 2022
//
//  For the full copyright and license information, please view
//  the LICENSE file that was distributed with this source code.
//  ============================================================

import static assignment5.assignment5.*;

public class assignment5_caller {
    private static void question1_caller(String input1, int input2) {
        int output = question1(input1, input2);
        System.out.println("Question1: " + output);
    }

    private static void question2_caller(String input1, int input2) {
        int output = question2(input1, input2);
        System.out.println("Question2: " + output);
    }

    private static void question3_caller(String input1, String input2) {
        int output = question3(input1, input2);
        System.out.println("Question3: " + output);
    }

    public static void main(String[] args) {
        switch (args[0]) {
            case "question1":
            	question1_caller(args[1], Integer.parseInt(args[2]));
            	break;
            case "question2":
            	question2_caller(args[1], Integer.parseInt(args[2]));
            	break;
            case "question3":
            	question3_caller(args[1], args[2]);
            	break;
            default:
            	throw new RuntimeException("Question number not given.");
        }
    }
}