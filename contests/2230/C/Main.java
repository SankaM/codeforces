import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int multTestQ = Integer.parseInt(st.nextToken());
        while (multTestQ-- > 0) {
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            long s = 0;
            long ones = 0;
            long slots = 0;
            for (int i = 0; i < n; i++) {
                long x = Long.parseLong(st.nextToken());
                s += x;
                if (x == 1L) {
                    ones++;
                } else {
                    slots += x / 2L - 1L;
                }
            }
            if (ones == n - 1) {
                slots++;
            }
            long wasted = Math.max(0L, ones - slots);
            long ans = s - wasted;
            if (ans < 3L) {
                out.println(0);
            } else {
                out.println(ans);
            }
        }
        out.flush();
        out.close();
    }
}
