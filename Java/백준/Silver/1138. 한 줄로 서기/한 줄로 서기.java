import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] data = br.readLine().split(" ");

        int[] people = new int[N];

        for (int i=0; i<N; i++) {
            int x = Integer.parseInt(data[i]);
            int idx = 0;

            while (x>0) {
                while (people[idx] != 0) {
                    idx++;
                }
                idx++;
                x--;
            }

            while (people[idx] != 0) {
                idx++;
            }
            people[idx] = i+1;
        }

        for (int i=0; i<N-1; i++) {
            System.out.print(people[i] + " ");
        }
        System.out.print(people[N-1]);
    }
}