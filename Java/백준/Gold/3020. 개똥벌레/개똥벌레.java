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
        int H = Integer.parseInt(st.nextToken());
        
        int[] up = new int[N/2];
        int[] down = new int[N/2];
        
        for (int i=0; i<N; i++) {
            if (i%2 == 0) down[i/2] = Integer.parseInt(br.readLine());
            else up[i/2] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(up);
        Arrays.sort(down);
        
        int min = Integer.MAX_VALUE;
        int x = 0;
        for (int i=1; i<=H; i++) {
            int d = calc(0, N/2, down, i);
            int u = calc(0, N/2, up, H-i+1);
            
            if (min > d+u) {
                min = d+u;
                x = 1;
            } else if (min == d+u) x++;
        }

        System.out.println(min + " " + x);
    }
    
    static int calc(int left, int right, int[] arr, int h) {
        while (left < right) {
            int mid = (left+right)/2;
            
            if (arr[mid] >= h) right = mid;
            else left = mid+1;
        }
        
        return arr.length - right;
    }
}