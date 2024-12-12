import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part2 {
    public static void Exec() {
        int multiplied = 0;

        boolean doOrDont = true;
        Scanner sc = new Scanner(System.in);
        String regex = "mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)";
        Pattern pattern = Pattern.compile(regex);

        while (sc.hasNextLine()) {
            String line = sc.nextLine().strip();

            Matcher matcher = pattern.matcher(line);

            while (matcher.find()) {
                String match = matcher.group();

                if (match.equals("do()")) {
                    doOrDont = true;
                } else if (match.equals("don't()")) {
                    doOrDont = false;
                } else if (doOrDont) {
                    String[] parts = match.substring(4, match.length() - 1).split(",");
                    int X = Integer.parseInt(parts[0]);
                    int Y = Integer.parseInt(parts[1]);

                    multiplied += X * Y;
                }
            }
        }
        System.out.println(multiplied);

    }
}