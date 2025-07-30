
import java.util.Scanner;

public class grade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the mark: ");
        int mark = scanner.nextInt();

        if (mark >= 90) {
            System.out.println("The grade is A");
        } else if (mark >= 75) {
            System.out.println("The grade is B");
        } else if (mark >= 60) {
            System.out.println("The grade is C");
        } else {
            System.out.println("You have failed");
        }

       
    }
}
