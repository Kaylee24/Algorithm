import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int M, N;
    static int[][] thing;
    static boolean[][] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        thing = new int[M][N];
        visited = new boolean[M][N];
        for (int i=0; i<M; i++) {
            String[] temp = br.readLine().split("");
            for (int j=0; j<N; j++) {
                thing[i][j] = Integer.parseInt(temp[j]);
            }
        }

        // 0 : 전류가 통하는 흰색 격자, 1 : 전류가 통하지 않는 검은색 격자
        for (int j=0; j<N; j++) {
            if (thing[0][j]==0 && !visited[0][j]) {
                bfs(0, j);
            }
        }

        System.out.println("NO");
    }
    private static void bfs (int p, int q) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {p, q});
        visited[p][q] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int d=0; d<4; d++) {
                int np = now[0]+dy[d];
                int nq = now[1]+dx[d];

                if (0<=np && np<M && 0<=nq && nq<N) {
                    if (!visited[np][nq] && thing[np][nq]==0) {
                        if (np==M-1) {
                            System.out.println("YES");
                            System.exit(0);
                        }
                        visited[np][nq] = true;
                        queue.add(new int[] {np, nq});
                    }
                }
            }
        }
    }
}