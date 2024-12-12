import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Part1 {
    public static void Exec() {
        Scanner sc = new Scanner(System.in);
        int sum = 0;

        while (sc.hasNext()) {
            String s = sc.nextLine();

            String[] data = s.split(" ");
            List<Integer> numeric = Arrays.stream(data).map(Integer::parseInt).collect(Collectors.toCollection(ArrayList::new));

            boolean flag = true;
            boolean increase = numeric.get(1) > numeric.get(0);

            if (numeric.get(1) == numeric.get(0)){
                continue;
            }

            if (increase) {
                for (int i = 1; i < data.length - 1; i++) {
                    if (!(numeric.get(i+1) > numeric.get(i) && Math.abs(numeric.get(i+1) - numeric.get(i)) <= 3)) {
                        flag = false;
                        break;
                    }
                }
            }
            else if (!increase) {
                for (int i = 1; i < data.length - 1; i++) {
                    if (!(numeric.get(i+1) < numeric.get(i)&& Math.abs(numeric.get(i+1) - numeric.get(i)) <= 3)) {
                        flag = false;
                        break;
                    }
                }
            }

            if (flag) {
                sum ++;
            }
        }

        System.out.println(sum);
    }
}
