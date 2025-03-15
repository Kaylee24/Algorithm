import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder result = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] A = new int[N];
            int[] B = new int[M];

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                A[j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                B[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(B);
            int temp = 0;
            for (int k=0; k<N; k++) {
                int low = 0;
                int high = M-1;
                int cnt = 0;
                while (low <= high) {
                    int mid = (low+high)/2;
                    if (B[mid] < A[k]) {
                        low = mid+1;
                        cnt = mid+1;
                    } else {
                        high = mid-1;
                    }
                }
                temp += cnt;
            }
            result.append(temp + "\n");
        }

        bw.write(result + "");
        bw.flush();;
        bw.close();
    }
}