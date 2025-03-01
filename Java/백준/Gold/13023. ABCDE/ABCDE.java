import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int result = 0;
    static ArrayList<Integer>[] array;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N];
        array = new ArrayList[N];
        for (int i=0; i<N; i++) array[i] = new ArrayList<>();
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            array[A].add(B);
            array[B].add(A);
        }

        for (int i=0; i<N; i++) {
            if (result != 1) dfs(i, 1);
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int s, int d) {
        if (d==5) {
            result = 1;
            return;
        }
        visited[s] = true;
        for (int to : array[s]) {
            if (!visited[to]) dfs(to, d+1);
        }
        visited[s] = false;
    }
}