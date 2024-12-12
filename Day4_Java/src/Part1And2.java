import java.util.Scanner;

public class Part1And2 {
    public static void Exec() {
        Scanner sc = new Scanner(System.in);

        StringBuilder input = new StringBuilder();
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            input.append(line).append("\n");
        }

        String[] data = input.toString().strip().split("\n");
        int row = data.length;
        int column = data[0].length();

        int p1 = 0;
        int p2 = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (j + 3 < column && data[i].charAt(j) == 'X'
                        && data[i].charAt(j + 1) == 'M' && data[i].charAt(j + 2) == 'A' && data[i].charAt(j + 3) == 'S') {
                    p1++;
                }
                else if (i + 3 < row && data[i].charAt(j) == 'X'
                        && data[i + 1].charAt(j) == 'M' && data[i + 2].charAt(j) == 'A' && data[i + 3].charAt(j) == 'S') {
                    p1++;
                }
                else if (i + 3 < row && j + 3 < column
                        && data[i].charAt(j) == 'X' && data[i + 1].charAt(j + 1) == 'M' && data[i + 2].charAt(j + 2) == 'A' && data[i + 3].charAt(j + 3) == 'S') {
                    p1++;
                }
                else if (j + 3 < column && data[i].charAt(j) == 'S'
                        && data[i].charAt(j + 1) == 'A' && data[i].charAt(j + 2) == 'M' && data[i].charAt(j + 3) == 'X') {
                    p1++;
                }
                else if (i + 3 < row && data[i].charAt(j) == 'S'
                        && data[i + 1].charAt(j) == 'A' && data[i + 2].charAt(j) == 'M' && data[i + 3].charAt(j) == 'X') {
                    p1++;
                }
                else if (i + 3 < row && j + 3 < column && data[i].charAt(j) == 'S'
                        && data[i + 1].charAt(j + 1) == 'A' && data[i + 2].charAt(j + 2) == 'M' && data[i + 3].charAt(j + 3) == 'X') {
                    p1++;
                }
                else if (i - 3 >= 0 && j + 3 < column && data[i].charAt(j) == 'S'
                        && data[i - 1].charAt(j + 1) == 'A' && data[i - 2].charAt(j + 2) == 'M' && data[i - 3].charAt(j + 3) == 'X') {
                    p1++;
                }
                else if (i - 3 >= 0 && j + 3 < column && data[i].charAt(j) == 'X'
                        && data[i - 1].charAt(j + 1) == 'M' && data[i - 2].charAt(j + 2) == 'A' && data[i - 3].charAt(j + 3) == 'S') {
                    p1++;
                }

                if (i + 2 < row && j + 2 < column && data[i].charAt(j) == 'M'
                        && data[i + 1].charAt(j + 1) == 'A' && data[i + 2].charAt(j + 2) == 'S' && data[i + 2].charAt(j) == 'M' && data[i].charAt(j + 2) == 'S') {
                    p2++;
                }
                else if (i + 2 < row && j + 2 < column && data[i].charAt(j) == 'M'
                        && data[i + 1].charAt(j + 1) == 'A' && data[i + 2].charAt(j + 2) == 'S' && data[i + 2].charAt(j) == 'S' && data[i].charAt(j + 2) == 'M') {
                    p2++;
                }
                else if (i + 2 < row && j + 2 < column && data[i].charAt(j) == 'S'
                        && data[i + 1].charAt(j + 1) == 'A' && data[i + 2].charAt(j + 2) == 'M' && data[i + 2].charAt(j) == 'M' && data[i].charAt(j + 2) == 'S') {
                    p2++;
                }
                else if (i + 2 < row && j + 2 < column && data[i].charAt(j) == 'S'
                        && data[i + 1].charAt(j + 1) == 'A' && data[i + 2].charAt(j + 2) == 'M' && data[i + 2].charAt(j) == 'S' && data[i].charAt(j + 2) == 'M') {
                    p2++;
                }
            }
        }

        System.out.println(p1);
        System.out.println(p2);
    }
}
