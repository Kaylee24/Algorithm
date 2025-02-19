import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 카드의 적힌 수의 합으로 만들 수 없는 수의 개수 구하기
        // -> 모든 경우의 수를 구해야 함
        // -> DFS 는 시간 초과
        // => 비트마스킹 방식으로 구해야 함

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫번째 줄에는 카드의 개수 N(1<=N<=20)이 주어진다.
        int N = Integer.parseInt(br.readLine());

        // 두번째 줄에는 N개의 수가 주어진다.
        long[] numbers = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 반복문 이용 -> N개의 수를 배열에 담는다.
        long M = 0;   // N개의 수의 총합 구하기
        for (int i=0; i<N; i++) {
            numbers[i] = Long.parseLong(st.nextToken());
            M += numbers[i];
        }

        // 만들 수 있는 수를 구하고, set 를 이용해 중복처리를 한다.
        HashSet<Long> sumSet = new HashSet<>();

        int totalSubsets = 1<<N;   // 2^N subsets
        for (int mask=1; mask<totalSubsets; mask++) {
            long sum = 0;
            for (int i=0; i<N; i++) {
                if ((mask & (1<<i)) != 0) {
                    sum += numbers[i];
                }
            }
            sumSet.add(sum);
        }

        // 만들 수 있는 수의 개수를 구한다.
        long count = 0;
        for (long sum : sumSet) {
            if (1<=sum && sum<=M) {
                count++;
            }
        }

        // 만들 수 없는 수의 개수를 출력한다.
        System.out.println(M - count);
    }
}

