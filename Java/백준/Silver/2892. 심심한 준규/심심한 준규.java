import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");

        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            if (Integer.parseInt(s, 16) >= 64 && Integer.parseInt(s, 16) < 96) {
                sb.append("-");
            } else {
                sb.append(".");
            }
        }
        bw.write(sb.toString());
        bw.close();
    }
}