import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int N, A, minimum;
    static int[] teamA;
    static boolean[] visited;
    static int[][] synergy;

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        synergy = new int[N][N];
        visited = new boolean[N];

        for (int i=0; i<N; i++) {
            String[] temp = br.readLine().split(" ");
            for (int j=0; j<N; j++) {
                synergy[i][j] = Integer.parseInt(temp[j]);
                minimum += synergy[i][j];
            }
        }

        for (A=1; A<N; A++) {
            teamA = new int[A];
            dfs(0, 0);
        }

        bw.write(minimum + "");
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int idx, int d) {
        if (d==A) {
            List<Integer> teamBList = new ArrayList<>();
            for (int i=0; i<N; i++) {
                if (!visited[i]) {
                    teamBList.add(i);
                }
            }

            Object[] teamB = teamBList.toArray();

            int sumA = 0, sumB = 0;

            for (int i=0; i<A; i++) {
                for (int j=0; j<A; j++) {
                    sumA += synergy[teamA[i]][teamA[j]];
                }
            }

            for (int i=0; i<N-A; i++) {
                for (int j=0; j<N-A; j++) {
                    sumB += synergy[(int)teamB[i]][(int)teamB[j]];
                }
            }

            minimum = Math.min(minimum, Math.abs(sumA-sumB));
            return;
        }

        for (int i=idx; i<N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                teamA[d] = i;
                dfs(i, d+1);
                visited[i] = false;
            }
        }
    }
}