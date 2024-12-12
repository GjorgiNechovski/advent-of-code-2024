import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part1 {
    public static void Exec() {
        int multiplied = 0;
        try (Scanner sc = new Scanner(System.in)) {
            String regex = "mul\\((\\d+),\\s*(\\d+)\\)";

            while (sc.hasNextLine()) {
                String s = sc.nextLine();

                Pattern pattern = Pattern.compile(regex);
                Matcher matcher = pattern.matcher(s);

                while (matcher.find()) {
                    int X = Integer.parseInt(matcher.group(1));
                    int Y = Integer.parseInt(matcher.group(2));

                    int result = X * Y;
                    multiplied = multiplied + result;
                }
            }

            System.out.println(multiplied);
        }
    }
}