import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] board = new int[5][5];
    static int r, c;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i=0; i<5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0 ; j<5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board[r][c] = -1;
        dfs(r, c, 0, 0);

        System.out.println(result);
    }

    static void dfs(int i, int j, int move, int apple) {
        if (move==3) {
            if (apple>=2) result = 1;
            return;
        }

        if (apple==2) {
            result = 1;
            return;
        }

        for (int k=0; k<4; k++) {
            int nr = i+di[k];
            int nc = j+dj[k];
            if (0<=nr && nr<5 && 0<=nc && nc<5 && board[nr][nc]!=-1) {
                int a = board[nr][nc];
                board[nr][nc] = -1;
                dfs(nr, nc, move+1, apple+a);
                board[nr][nc] = a;
            }
        }
    }
}