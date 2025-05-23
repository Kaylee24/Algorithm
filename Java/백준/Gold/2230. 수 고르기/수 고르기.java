import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M, answer = Integer.MAX_VALUE;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        int left = 0;
        int right = 0;

        while (right<N && left<=right) {
            int temp = arr[right] - arr[left];
            if (temp >= M) {
                left++;
                answer = Math.min(answer, temp);
            } else right++;
        }

        System.out.println(answer);
    }
}