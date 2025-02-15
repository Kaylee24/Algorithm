import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] YB = {"", "1", "1", "1990"};
        String[] OB = {"", "31", "12", "2010"};

        for (int i = 0; i < N; i++) {
            String data = br.readLine();
            String[] person = data.split("\\s");
            int check = 0;

            if (Integer.parseInt(YB[3]) < Integer.parseInt(person[3])) {
                YB = person;
                check = 1;
            } else if (Integer.parseInt(YB[3]) == Integer.parseInt(person[3])) {
                if (Integer.parseInt(YB[2]) < Integer.parseInt(person[2])) {
                    YB = person;
                    check = 1;
                } else if (Integer.parseInt(YB[2]) == Integer.parseInt(person[2])) {
                    if (Integer.parseInt(YB[1]) < Integer.parseInt(person[1])) {
                        YB = person;
                        check = 1;
                    }
                }
            }

            if (check == 0) {
                if (Integer.parseInt(OB[3]) > Integer.parseInt(person[3])) {
                    OB = person;
                } else if (Integer.parseInt(OB[3]) == Integer.parseInt(person[3])) {
                    if (Integer.parseInt(OB[2]) > Integer.parseInt(person[2])) {
                        OB = person;
                    } else if (Integer.parseInt(OB[2]) == Integer.parseInt(person[2])) {
                        if (Integer.parseInt(OB[1]) > Integer.parseInt(person[1])) {
                            OB = person;
                        }
                    }
                }
            }
        }
        System.out.println(YB[0]);
        System.out.println(OB[0]);
    }
}
