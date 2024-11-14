import java.util.Scanner;

class Counter {
    public int countPerson(int k, int n) {
        int[][] findPerson = new int[k+1][n+1];

        for(int room = 1; room <= n; room++) {
            findPerson[0][room] = room;
        }
        for(int floor = 1; floor <= k; floor++) {
            for(int room = 1; room <= n; room++) {
                findPerson[floor][room] = findPerson[floor - 1][room] + findPerson[floor][room - 1];
            }
        }

        return findPerson[k][n];
    }
}

public class Beakjoon2775 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        Counter counter = new Counter();



        int t = scanner.nextInt();

        for (int i  = 0; i < t; i++) {
            int k = scanner.nextInt();
            int n = scanner.nextInt();
            sb.append(counter.countPerson(k,n)).append("\n");
        }
        System.out.println(sb);




    }

}
