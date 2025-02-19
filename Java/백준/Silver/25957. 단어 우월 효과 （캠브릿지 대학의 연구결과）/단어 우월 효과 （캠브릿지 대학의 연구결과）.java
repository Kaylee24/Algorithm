import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        Map<String, String> wordMap = new HashMap<>();

        for (int i=0; i<N; i++) {
            String word = br.readLine().trim();
            wordMap.put(getBitmaskKey(word), word);
        }

        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            String s = st.nextToken();
            String key = getBitmaskKey(s);
            sb.append(wordMap.getOrDefault(key, s)).append(" ");
        }

        System.out.println(sb.toString().trim());
    }


    private static String getBitmaskKey(String word) {
        if (word.length() <= 3) return word;

        char[] middleChars =  word.substring(1, word.length()-1).toCharArray();
        Arrays.sort(middleChars);

        return word.charAt(0) + new String(middleChars) + word.charAt(word.length() - 1);
    }
}