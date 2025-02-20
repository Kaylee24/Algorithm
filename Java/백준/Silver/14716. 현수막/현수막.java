import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {1, -1, 0, 0, 1, 1, -1, -1};
    static int[] dy = {0, 0, 1, -1, 1, -1, 1, -1};

    static int M, N;
    static int[][] banner;
    static boolean[][] visited;
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        banner = new int[M][N];
        visited = new boolean[M][N];

        for (int m=0; m<M; m++) {
            String[] temp = br.readLine().split(" ");
            for (int n=0; n<N; n++) {
                banner[m][n] = Integer.parseInt(temp[n]);
            }
        }

        // BFS 를 이용하여 문자의 개수를 구한다.
        for (int i=0; i<M; i++) {
            for (int j=0; j<N; j++) {
                if (!visited[i][j] && banner[i][j]==1) {
                    bfs(i, j);
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
    private static void bfs(int p, int q) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {p, q});
        visited[p][q] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int d=0; d<8; d++) {
                int np = now[0]+dx[d];
                int nq = now[1]+dy[d];

                if (0 <= np && np < M && 0 <= nq && nq < N) {
                    if (!visited[np][nq] && banner[np][nq]==1) {
                        visited[np][nq] = true;
                        queue.add(new int[] {np, nq});
                    }
                }
            }
        }
    }
}