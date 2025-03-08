import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int caffeine = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] coffees = new int[N];
        for (int i=0; i<N; i++) {
            coffees[i] = Integer.parseInt(st.nextToken());
        }

        // 배낭 알고리즘
        int[] dp = new int[caffeine+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i=0; i<N; i++) {
            int coffee = coffees[i];

            for (int j=caffeine; j>=0; j--) {
                if (j-coffee >= 0&& dp[j-coffee] != Integer.MAX_VALUE) {
                    dp[j] = Math.min(dp[j], dp[j-coffee]+1);
                }
            }
        }
        
        System.out.println(dp[caffeine] == Integer.MAX_VALUE ? -1 : dp[caffeine]);
    }
}