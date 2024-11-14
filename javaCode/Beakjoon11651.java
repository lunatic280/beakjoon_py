import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Beakjoon11651 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine().trim());

        ArrayList<List<Integer>> comma = new ArrayList<>();
        int number = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < number; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            comma.add(Arrays.asList(x, y));
        }

        comma.sort((a, b) -> {
            if (!a.get(1).equals(b.get(1))) {
                return a.get(1) - b.get(1);
            }
            return a.get(0) - b.get(0);
        });

        StringBuilder sb = new StringBuilder();

        for(List<Integer> coordinate : comma) {
            sb.append(coordinate.get(0)).append(" ").append(coordinate.get(1)).append("\n");
        }
        System.out.println(sb);
    }
}
