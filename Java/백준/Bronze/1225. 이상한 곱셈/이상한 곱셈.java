import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String A = st.nextToken();
        String B = st.nextToken();

        long result = 0;

        for (String a : A.split("")) {
            int i = Integer.parseInt(a);
            for (String b : B.split("")) {
                int j = Integer.parseInt(b);

                result += i*j;
            }
        }

        System.out.println(result);
    }
}