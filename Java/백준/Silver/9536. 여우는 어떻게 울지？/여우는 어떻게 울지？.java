import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int k=0; k<N; k++){
            String fullRecorded = br.readLine();
            Set<String> soundSet = new HashSet<>();

            String animal = "";
            while(!(animal = br.readLine()).equals("what does the fox say?")){
                String[] strArray = animal.split(" goes ");
                soundSet.add(strArray[1]);
            }
			
            String[] words = fullRecorded.split(" ");
            String result = "";
            for(int i=0; i<words.length; i++){
                if(!soundSet.contains(words[i])){
                    result += words[i] + " ";
                }
            }
            
            System.out.println(result.substring(0, result.length()-1));
        }
    }
}
