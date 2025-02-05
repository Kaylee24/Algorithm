import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maximum = 0;
        int r = 1;
        int c = 1;

        for (int i=1; i<=9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=1; j<=9; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (num > maximum) {
                    maximum = num;
                    r = i;
                    c = j;
                }
            }
        }

        System.out.println(maximum);
        System.out.println(r + " " + c);
    }
}