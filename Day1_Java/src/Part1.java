import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Part1 {
    public static void Exec(){
        Scanner sc = new Scanner(System.in);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        while (sc.hasNext()){
            String line = sc.nextLine();

            String[] numbers = line.split("\\s+");
            left.add(Integer.parseInt(numbers[0]));
            right.add(Integer.parseInt(numbers[1]));
        }

        left = left.stream().sorted().collect(Collectors.toCollection(ArrayList::new));
        right = right.stream().sorted().collect(Collectors.toCollection(ArrayList::new));

        int sum = 0;
        for (int i = 0; i < left.size(); i++){
            sum += Math.abs(left.get(i) - right.get(i));
        }

        System.out.println(sum);
    }
}
