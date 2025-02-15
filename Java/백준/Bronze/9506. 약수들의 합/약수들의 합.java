import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int N = Integer.parseInt(br.readLine());

            if (N == -1) {
                break;
            }

            int[] array = new int[N];

            int sum = 0;

            for (int i = 1; i <= N; i++) {
                if (N % i == 0 && i != N) {
                    array[i] = i;
                    sum += i;
                }
                // 약수가 아니라면 0이 기본값으로 배열에 들어가 있음.
            }

            if (sum != N) {
                sb.append(N + " is NOT perfect. \n");
                continue;
            }

            sb.append(N + " = 1");

            for (int i = 1; i <= N; i++) {
                if (array[i-1] != 0 && array[i-1] != 1) {
                    sb.append(" + " + array[i-1]);
                }
            }

            sb.append("\n");
        }
        br.close();
        System.out.println(sb);
    }
}
