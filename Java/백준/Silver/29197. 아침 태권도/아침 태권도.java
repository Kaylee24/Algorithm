import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Set<Double> quad1 = new HashSet<>();
        Set<Double> quad2 = new HashSet<>();
        Set<Double> quad3 = new HashSet<>();
        Set<Double> quad4 = new HashSet<>();
        Set<String> axis = new HashSet<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());

            if (X > 0 && Y > 0) {
                quad1.add((double) Y/X);
            } else if (X < 0 && Y > 0) {
                quad2.add((double) Y/X);
            } else if (X < 0 && Y < 0) {
                quad3.add((double) Y/X);
            } else if (X > 0 && Y < 0) {
                quad4.add((double) Y/X);
            }
            else if (X == 0 && Y > 0) {
                axis.add("Y");
            } else if (X == 0 && Y < 0) {
                axis.add("-Y");
            } else if (X > 0 && Y == 0) {
                axis.add("X");
            } else if (X < 0 && Y == 0) {
                axis.add("-X");
            }
        }

        int cnt = quad1.size() + quad2.size() + quad3.size() + quad4.size() + axis.size();
        System.out.println(cnt);
        br.close();
    }
}