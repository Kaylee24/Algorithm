import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st =  new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());

        int left = 0;
        int right = 0;
        int cnt = 0;
        int max = Integer.MIN_VALUE;
        while (right<N) {
            if (cnt + arr[right] <= M) {
                cnt += arr[right];
                max = Integer.max(max, cnt);
                right++;
            } else {
                cnt -= arr[left];
                left++;
            }
        }

        System.out.println(max);
    }
}