package javaCode;

import java.util.Scanner;

public class Beakjoon30802 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numberOfPerson = scanner.nextInt();
        int[] numberOfSize = new int[6];
        for (int i = 0; i < 6; i++) {
            numberOfSize[i] = scanner.nextInt();
        }
        int[] numberOfList = new int[2];
        for (int i = 0; i < 2; i++) {
            numberOfList[i] = scanner.nextInt();
        }

        int t = numberOfList[0];
        int p = numberOfList[1];

        int resultT = 0;
        for (int i = 0; i < numberOfSize.length; i++) {
            if (numberOfSize[i] % t == 0) {
                resultT += numberOfSize[i] / t;
            } else {
                resultT += numberOfSize[i] / t;
                resultT += 1;
            }
        }

        int resultP1 = numberOfPerson / p;
        int resultP2 = numberOfPerson % p;


        System.out.println(resultT);
        System.out.println(resultP1 + " " + resultP2);



    }
}
