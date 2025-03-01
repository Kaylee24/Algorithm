import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, M, Guitar;
    static int max = 0;
    static long[] guitarBit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());   // 기타의 개수 N
        M = Integer.parseInt(st.nextToken());   // 곡의 개수 M
        guitarBit = new long[N];

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            st.nextToken();
            char[] guitarYN = st.nextToken().toCharArray();
            for (int j=0; j<M; j++) {
                if (guitarYN[j] == 'Y') guitarBit[i] |= (1L<<j);
            }
        }

        search(0, 0L, 0);
        if (Guitar == 0) Guitar = -1;

        bw.write(String.valueOf(Guitar));
        bw.flush();
        bw.close();
        br.close();
    }

    static void search(int i, long guitarMask, int v) {
        int bitCount = Long.bitCount(guitarMask);

        if (bitCount == max && v < Guitar) Guitar = v;

        if (bitCount > max) {
            Guitar = v;
            max = bitCount;
        }

        if (bitCount==M || i==N) return;

        search(i+1, guitarMask | guitarBit[i], v+1);
        search(i+1, guitarMask, v);
    }
}