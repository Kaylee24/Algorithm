import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // N과 L이 주어진다.
        // 합이 N 이면서, 길이가 적어도 L 인 가장 짧은 연속된 음이 아닌 정수 리스트
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] array = br.readLine().split(" ");
        long N = Long.valueOf(array[0]);
        long L = Long.valueOf(array[1]);
        boolean check = true;

        while (L <= 100) {
            long start = N/L - (L-1)/2;
            if (start < 0)
                break;

            if (N == (start*2 + L-1) * L/2) {
                for (long i=0; i < L; i++)
                    bw.write(start + i + " ");
                check = false;
                break;
            }

            L += 1;
        }

        if (check)
            bw.write("-1");

        bw.write("\n");
        bw.flush();
    }
}