import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int T = scan.nextInt();

        Node[] node = new Node[N+1];
        for (int i=1; i<=N; i++) {
            int K = scan.nextInt();
            int S = scan.nextInt();
            node[i] = new Node(K, S);
        }

        int[][] dp = new int[N+1][T+1];
        for (int i=1; i<=N; i++) {
            for (int j=0; j<=T; j++) {
                if (node[i].time <= j) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-node[i].time] + node[i].score);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        System.out.println(dp[N][T]);
    }

    public static class Node {
        int time, score;

        public Node(int time, int score) {
            this.time = time;
            this.score = score;
        }
    }
}