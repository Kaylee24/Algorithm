import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] layers;
    static long[] patties;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long X = Long.parseLong(st.nextToken());
        layers = new long[N+1];
        patties = new long[N+1];
        layers[0] = 1;
        patties[0] = 1;
        for (int i=1; i<=N; i++) {
            layers[i] = layers[i-1]*2+3;
            patties[i] = patties[i-1]*2+1;
        }
        long result = recur(N, X);
        System.out.println(result);
    }

    static long recur(int l, long x) {
        long cnt = 0;
        long mid = layers[l]/2+1;
        if (l==0) return 1;
        if (x==1) return 0;
        if (x==layers[l]) {
            return patties[l-1]*2+1;
        } else if (x < mid) {
            cnt += recur(l-1, x-1);
        } else if (x==mid) {
            cnt += patties[l-1]+1;
        } else {
            cnt += patties[l-1]+1+recur(l-1, x-layers[l-1]-2);
        }
        return cnt;
    }
}