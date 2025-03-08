import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long[] timetable = new long[1001];
        int N = Integer.parseInt(br.readLine());

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());

            for (int j=0; j<K; j++) {
                int time = Integer.parseInt(st.nextToken());
                timetable[i] |= ((long)1 << time);
            }
        }

        int M = Integer.parseInt(br.readLine());

        for (int i=0; i<M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int size = Integer.parseInt(st.nextToken());
            long temp = 0;

            for (int j=0; j<size; j++) {
                int time = Integer.parseInt(st.nextToken());
                temp |= ((long)1 << time);
            }

            temp = ~temp;
            int cnt = 0;

            for (int j=0; j<N; j++) {
                if ((temp & timetable[j]) == 0) cnt++;
            }

            sb.append(cnt + "\n");
        }

        System.out.println(sb);
    }
}