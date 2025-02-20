import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static Long N;
    static Long P;
    static Long Q;
    static HashMap<Long, Long> arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Long.parseLong(st.nextToken());
        P = Long.parseLong(st.nextToken());
        Q = Long.parseLong(st.nextToken());

        arr = new HashMap<>();
        long ans = solve(N);
        System.out.println(ans);
    }
    static long solve(long n) {
        if (n == 0) return 1;
        if (arr.containsKey(n)) return arr.get(n);
        arr.put(n, solve(n/P) + solve(n/Q));
        return arr.get(n);
    }
}