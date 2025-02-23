import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] costs;
    static boolean[] visited;
    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());   // 도시의 수 N
        costs = new int[N][N];
        visited = new boolean[N];

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                costs[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        result = 1000000*N;
        for (int start=0; start<N; start++) {
            travel(0, start, start, 0);
        }

        System.out.println(result);
    }

    static void travel(int cnt, int start, int city, int sum) {
        if (cnt==N && city==start) {
            if (result > sum) result = sum;
        }

        if (sum > result) return;

        for (int k=0; k<N; k++) {
            if (!visited[k] && costs[city][k]!=0) {
                visited[k] = true;
                travel(cnt+1, start, k, sum+costs[city][k]);
                visited[k] = false;
            }
        }
    }
}