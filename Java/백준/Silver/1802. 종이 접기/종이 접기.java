import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String input;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++) {
            input = br.readLine();
            if (check(0, input.length()-1)) {
                sb.append("YES").append("\n");
            } else {
                sb.append("NO").append("\n");
            }
        }
        System.out.println(sb);
    }

    static boolean check(int s, int e) {
        if (s==e) {
            return true;
        }
        int mid = (s+e)/2;
        for (int i=s; i<mid; i++) {
            if (input.charAt(i) == input.charAt(e-i)) {
                return false;
            }
        }
        return check(s, mid-1) && check(mid+1, e);
    }
}