import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 첫째 줄에 테스트 케이스의 개수 T가 주어진다. (1 <= T <= 1000)
        int T = Integer.parseInt(br.readLine());

        // 각 테스트 케이스는 한 줄로 이루어져 있고,
        // R, 공백, C, 공백, 규현이가 보내려고 하는 메시지로 이루어져 있다.
        for (int tc=0; tc<T; tc++) {
            String data = br.readLine();

            // indexOf(String) 메서드 : 특정 문자열(공백 포함)의 위치(인덱스)를 찾아줌.
            int firstSpace = data.indexOf(" ");
            int secondSpace = data.indexOf(" ", firstSpace+1);

            // substring(start, end) 메서드는 문자열의 일부만 잘라서 반환.
            int R = Integer.parseInt(data.substring(0, firstSpace));
            int C = Integer.parseInt(data.substring(firstSpace+1, secondSpace));

            String message = data.substring(secondSpace+1);

            // 1. 모든 글자는 알파벡 대문자와 공백으로 이루어져 있다.
            // 2. 글자는 다음과 같이 숫자로 바뀐다.
            //    공백 = 0, A = 1, B = 2, ..., Y = 25, Z = 26
            // *글자 -> 숫자 -> 5자리 이진수 -> 시계방향 소용돌이 패턴으로 배치 -> 모자라는 칸은 0으로 채운다

            int L = message.length();
            Long[] arr = new Long[L];
            StringBuilder binaryResult = new StringBuilder();

            // 글자 -> 숫자
            for (int i=0; i<L; i++) {
                // String 은 문자 배열처럼 직접 인덱스로 접근할 수 없음.
                // 문자열.charAt(i) 를 사용해 문자열의 i 번째 문자를 가져와야 함.
                char c = message.charAt(i);
                if (c == ' ') {
                    arr[i] = 0L;
                } else {
                    // arr[i] = (int)c - 64;   // 에러!
                    arr[i] = (long)(c-'A'+1);
                }
                String binary = Long.toBinaryString(arr[i]);
                while (binary.length() < 5) {
                    binary = "0" + binary;
                }

                binaryResult.append(binary);
            }

            // 숫자 -> 재배치

            // R*C 빈배열 만들기
            String[][] result = new String[R][C];

            // 시계방향 소용돌이 배치
            // 방향을 알려줄 변수
            int[] dx = {0, 1, 0, -1};
            int[] dy = {1, 0, -1, 0};
            int d = 0;

            // 배치가 끝났는지 확인할 변수
            int cnt = 0;

            // 출발 좌표
            int r = 0;
            int c = 0;

            // 방문 체크 배열
            boolean[][] visited = new boolean[R][C];

            while (cnt < R*C) {
                if (0 <= r && r < R && 0 <= c && c < C && !visited[r][c]) {
                    if (cnt < binaryResult.length()) {
                        result[r][c] = String.valueOf(binaryResult.charAt(cnt));
                    } else {
                        result[r][c] = "0";
                    }
                    cnt += 1;
                    visited[r][c] = true;
                    r += dx[d];
                    c += dy[d];
                } else {
                    r -= dx[d];
                    c -= dy[d];

                    d = (d+1)%4;

                    r += dx[d];
                    c += dy[d];
                }
            }

            StringBuilder secretMessage = new StringBuilder();

            for (int i=0; i<R; i++) {
                for (int j=0; j<C; j++) {
                    if (result[i][j] != null) {
                        secretMessage.append(result[i][j]);
                    } else {
                        secretMessage.append("0");
                    }
                }
            }

            System.out.println(secretMessage);
        }
    }
}

