import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        long[] arr = new long[N];
        long max = 0;
        
        for (int i=0; i<N; i++) {
            arr[i] = Long.parseLong(br.readLine());
            max = Math.max(max, arr[i]);
        }
        
        long left = 1;
        long right = max;
        long result = 0;
        
        while (left <= right) {
            long mid = (left+right)/2;
            int cnt = 0;
            
            for (long a : arr) cnt += a/mid;
            
            if (cnt >= K) {
                result = mid;
                left = mid+1;
            } else {
                right = mid-1;
            }
        }

        System.out.println(result);
        br.close();
    }
}