import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr);

    int temp = Integer.MAX_VALUE;
    int left = 0, right = 0;
    int low = 0, high = N-1;

    while (low < high) {
        int sum = arr[low] + arr[high];

        if (Math.abs(sum) < temp) {
            temp = Math.abs(sum);
            left = arr[low];
            right = arr[high];
        }

        if (sum < 0) low++;
        else high--;
    }

    System.out.println(left + " " + right);
    }
}