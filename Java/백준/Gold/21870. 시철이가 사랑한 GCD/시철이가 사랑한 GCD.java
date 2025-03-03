// 툴린 코드...

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static int gcd(int x, int y) {
        while (y!=0) {
            int tempX = x, tempY = y;
            x = tempY;
            y = tempX%tempY;
        }
        return x;
    }

    public static int gcdOfList(int[] lst) {
        int result = lst[0];
        for (int i=1; i<lst.length; i++) {
            result = gcd(result, lst[i]);
        }
        return result;
    }

    public static int BT(int[] array, int left, int right) {
        if (left==right) {
            return array[left];
        }

        int mid = (right-left+1)/2;
        int leftResult = BT(array, left+mid, right);
        int rightResult = BT(array, left, left+mid-1);
        int leftGcd = gcdOfList(Arrays.copyOfRange(array, left, left+mid));
        int rightGcd = gcdOfList(Arrays.copyOfRange(array, left+mid, right+1));

        return Math.max(leftResult+leftGcd, rightResult+rightGcd);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] a = new int[N];
        for (int i=0; i<N; i++) {
            a[i] = Integer.parseInt(input[i]);
        }

        if (N==1) {
            System.out.println(a[0]);
        } else {
            int result = BT(a, 0, N-1);
            System.out.println(result);
        }
    }
}
