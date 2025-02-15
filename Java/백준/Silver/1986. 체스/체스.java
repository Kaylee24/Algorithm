import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N, M
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // Queen 의 개수와 Queen 의 위치 | Queen, Knight, Pawn
        String[] queen = br.readLine().split(" ");
        String[] knight = br.readLine().split(" ");
        String[] pawn = br.readLine().split(" ");

        // 체스보드판 생성
        int[][] board = new int[N][M];

        // idx = 0 : 말의 개수, (idx//2-1, idx//2) : 말의 위치
        // knight
        for (int i=0; i<Integer.parseInt(knight[0]); i++) {
            int r = (i+1)*2-1;
            int c = (i+1)*2;
            r = Integer.parseInt(knight[r])-1;
            c = Integer.parseInt(knight[c])-1;
            board[r][c] = 3;
            // (r, c) 칸을 기준으로 knight 가 공격할 수 있는 8칸을 체크한다.
            int[] dx = {-2, -2, -1, -1, 1, 1, 2, 2};
            int[] dy = {-1, 1, -2, 2, -2, 2, -1, 1};
            for (int j=0; j<8; j++) {
                int p = r + dx[j];
                int q = c + dy[j];
                if (0 <= p && p < N && 0 <= q && q < M && board[p][q] != 3) {
                    board[p][q] = 1;
                }
            }
        }

        // pawn : 장애물의 역할만 한다.
        for (int i=0; i<Integer.parseInt(pawn[0]); i++) {
            int r = (i+1)*2-1;
            int c = (i+1)*2;
            r = Integer.parseInt(pawn[r])-1;
            c = Integer.parseInt(pawn[c])-1;
            board[r][c] = 4;
        }

        // Queen 은 중간에 장애물이 있으면 더 이상 진행하지 못하므로 마지막에 확인한다.
        for (int i=0; i<Integer.parseInt(queen[0]); i++) {
            int r = (i+1)*2-1;
            int c = (i+1)*2;
            r = Integer.parseInt(queen[r])-1;
            c = Integer.parseInt(queen[c])-1;
            board[r][c] = 2;
            // queen 을 중심으로 상하좌우, 대각선 4방향,
            // 총 8방향을 순회하며 장애물이 나올때까지 공격 가능한 칸을 체크한다.
            int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
            int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
            for (int j=0; j<8; j++) {
                int k = 1;
                while (true) {
                    int p = r + dx[j]*k;
                    int q = c + dy[j]*k;

                    if (p < 0 || p >= N || q < 0 || q >= M) break;
                    if (board[p][q] == 2 || board[p][q] == 3 || board[p][q] == 4) break;

                    board[p][q] = 1;
                    k++;
                }
            }
        }
        int safe = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (board[i][j] == 0) {
                    safe++;
                }
            }
        }

        System.out.println(safe);
    }
}