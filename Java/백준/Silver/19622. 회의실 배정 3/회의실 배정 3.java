import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N+2][2];
        for (int i=2; i<=N+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            st.nextToken();
            int cur = Integer.parseInt(st.nextToken());
            arr[i][0] = Math.max(arr[i-1][0], arr[i-1][1]);
            arr[i][1] = Math.max(arr[i-1][0], arr[i-2][1]) + cur;
        }
        System.out.println(Math.max(arr[N+1][0], arr[N+1][1]));
    }

    public static void main(String[] args) throws IOException{
        new Main().solution();
    }
}