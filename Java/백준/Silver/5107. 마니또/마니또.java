import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int tc = 1;

        while (true) {
            int N = Integer.parseInt(br.readLine());   // N명
            if (N == 0) {
                break;
            }

            Map<String, String> manittoMap = new HashMap<>();
            Map<String, Boolean> doneMap = new HashMap<>();
            for (int i=0; i<N; i++) {
                String name = br.readLine().trim();
                int f = name.indexOf(" ");
                String giver = name.substring(0, f);
                String taker = name.substring(f+1);
                manittoMap.put(giver, taker);
                doneMap.put(giver, false);
            }

            // 첫번째 이름부터 순회하면서 고리를 타고 간다.
            // 고리가 끝나면(=첫번째 이름으로 돌아오면) cnt 를 센다.
            // 다음 이름으로 넘어가면, 이전 고리에 속한 고리인지 여부를 확인한다.
            // 속하지 않은 이름일때에 새로운 고리를 시작한다.
            // 모든 이름이 고리에 포함이 되면 cnt 를 출력한다.
            int cnt = 0;
            for (String start : manittoMap.keySet()) {
                if (!doneMap.get(start)) {
                    cnt++;
                    String currentGiver = start;
                    while (!doneMap.get(currentGiver)) {
                        doneMap.put(currentGiver, true);
                        currentGiver = manittoMap.get(currentGiver);
                    }
                }
            }

            sb.append(tc).append(" ").append(String.valueOf(cnt)).append("\n");
            tc++;
        }

        System.out.println(sb);
    }
}