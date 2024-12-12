import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Part2 {
    public static void Exec() {
        Scanner sc = new Scanner(System.in);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        while (sc.hasNext()) {
            String line = sc.nextLine();

            String[] numbers = line.split("\\s+");
            left.add(Integer.parseInt(numbers[0]));
            right.add(Integer.parseInt(numbers[1]));
        }

        HashMap<Integer, Integer> rightOccurrences = new HashMap<>();
        for (int num : right) {
            rightOccurrences.put(num, rightOccurrences.getOrDefault(num, 0) + 1);
        }

        int sum = 0;
        for (int num : left) {
            int appearances = rightOccurrences.getOrDefault(num, 0);
            sum += num * appearances;
        }

        System.out.println(sum);
    }
}
