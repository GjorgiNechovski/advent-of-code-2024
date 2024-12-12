import java.util.*;
import java.util.stream.Collectors;

public class Part2 {
    public static void Exec() {
        Scanner sc = new Scanner(System.in);
        int sum = 0;

        while (sc.hasNext()) {
            String s = sc.nextLine();

            String[] data = s.split(" ");
            List<Integer> numeric = Arrays.stream(data).map(Integer::parseInt).collect(Collectors.toCollection(ArrayList::new));

            boolean flag = true;
            boolean mistake = true;
            boolean increase = false;

            increase = numeric.get(1) > numeric.get(0);
            if (numeric.get(0) == numeric.get(1)) {
                mistake = false;

                if (numeric.get(1) == numeric.get(2)) {
                    flag = false;
                    continue;
                }
                increase = numeric.get(2) > numeric.get(1);

            }



            if (increase) {
                for (int i = 0; i < numeric.size() - 1; i++) {
                    if (!(numeric.get(i+1) > numeric.get(i) && Math.abs(numeric.get(i+1) - numeric.get(i)) <= 3)) {
                        if (mistake){
                            mistake = false;
                            continue;
                        }
                        flag = false;
                        break;
                    }
                }
            }
            else if (!increase) {
                for (int i = 0; i < numeric.size() - 1; i++) {
                    if (!(numeric.get(i+1) < numeric.get(i)&& Math.abs(numeric.get(i+1) - numeric.get(i)) <= 3)) {
                        if (mistake){
                            mistake = false;
                            continue;
                        }
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
