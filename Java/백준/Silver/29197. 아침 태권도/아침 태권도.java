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

        // 각 학생들 별로 기울기를 구하고 set 에 넣는다.
        // set 의 원소의 수를 구한다.
        Set<Double> slopes = new HashSet<>();

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());

            if (X == 0) {
                if (Y > 0) {
                    slopes.add(Double.POSITIVE_INFINITY);
                } else {
                    slopes.add(Double.NEGATIVE_INFINITY);
                }
            } else {
                double slope = (double) Y/X;
                slopes.add(slope);
            }
        }

        System.out.println(slopes.size());
    }
}