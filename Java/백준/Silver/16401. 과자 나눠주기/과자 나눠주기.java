import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static long left = 1, right, answer = 0;
    static long[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new long[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i=0; i<N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
            right = Math.max(right, arr[i]);
        }

        f();
        System.out.println(answer);
    }

    static void f() {
        while (left <= right) {
            long mid = (left+right)/2;
            if (M > getMid(mid)) right = mid-1;
            else {
                left = mid+1;
                answer = mid;
            }
        }
    }

    static int getMid(long mid) {
        int cnt = 0;
        for (long a : arr) cnt += a/mid;

        return cnt;
    }
}