import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static boolean[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        arr = new boolean[N+1][N+1];

        for (int i=1; i<N; i++) {
            int E = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            for (int j=0; j<E; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[i][num] = true;
            }
        }

        for (int k=1; k<N; k++) {
            for (int i=1; i<N; i++) {
                for (int j=1; j<N; j++) {
                    if (arr[i][k] && arr[k][j]) {
                        arr[i][j] = true;
                    }
                }
            }
        }

        String result = "NO CYCLE";

        for (int i=1; i<N; i++) {
            if (arr[1][i] && arr[i][i]) {
                result = "CYCLE";
                break;
            }
        }

        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}