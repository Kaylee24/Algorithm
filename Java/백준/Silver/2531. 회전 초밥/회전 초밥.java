import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] eaten = new int[d+1];
        eaten[c] = 3001;
        int[] sushi = new int[N];
        int cnt = 1;

        for (int i=0; i<N; i++) sushi[i] = Integer.parseInt(br.readLine());

        for (int i=0; i<k; i++) {
            int sushiId = sushi[i];
            if (eaten[sushiId] == 0) cnt++;
            eaten[sushiId]++;
        }

        int max = cnt;

        for (int i=0; i<N-1; i++) {
            int s_id = sushi[i];
            int e_id = sushi[i+k<N ? i+k : (i+k)%N];
            if (--eaten[s_id] == 0) cnt--;
            if (++eaten[e_id] == 1) cnt++;
            max = Math.max(max, cnt);
        }

        bw.write(String.valueOf(max));
        bw.flush();
        bw.close();
        br.close();
    }
}