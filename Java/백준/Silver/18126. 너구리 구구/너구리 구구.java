import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static long result = 0;
    static ArrayList<Edge>[] ways;
    static boolean[] visited;

    static class Edge {
        int to, length;

        public Edge(int to, int length) {
            this.to = to;
            this.length = length;
        }

        @Override
        public String toString() {
            return "[" + to + ", " + length + "]";
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        ways = new ArrayList[N+1];
        visited = new boolean[N+1];

        for (int i=1; i<N+1; i++) ways[i] = new ArrayList<>();

        for (int i=1; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            ways[A].add(new Edge(B, C));
            ways[B].add(new Edge(A, C));
        }

        visited[1] = true;
        dfs(1, 0);

        System.out.println(result);
    }

    static void dfs(int now, long dist) {
        if (result < dist) result = dist;

        for (Edge next : ways[now]) {
            if (!visited[next.to]) {
                visited[next.to] = true;
                dfs(next.to, dist+next.length);
                visited[next.to] = false;
            }
        }
    }
}