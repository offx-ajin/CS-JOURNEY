package ajin;

import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        float num1 = scanner.nextFloat();

        System.out.print("Enter second number: ");
        float num2 = scanner.nextFloat();

        System.out.println("Choose an operation: +, -, *, /");
        System.out.print("Enter your choice: ");
        char operation = scanner.next().charAt(0);

        float result;

        switch (operation) {
            case '+':
                result = num1 + num2;
                System.out.println("Result: " + result);
                break;
            case '-':
                result = num1 - num2;
                System.out.println("Result: " + result);
                break;
            case '*':
                result = num1 * num2;
                System.out.println("Result: " + result);
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Result: " + result);
                } else {
                    System.out.println("Error! Division by zero.");
                }
                break;
            default:
                System.out.println("Invalid operation!");
        }

        scanner.close();
    }
}

