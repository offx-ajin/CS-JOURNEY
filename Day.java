import java.util.Scanner;

public class Day {
	public static void main(String [] args) {
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("Enter a number bw 1 and 7 :");
		int Day = scanner.nextInt();
		
		switch (Day) {
		case 1 :
			System.out.println("The Day is SUNDAY");
			break;
		case 2 :
			System.out.println("The day is MONDAY");
			break;
		case 3 :
			System.out.println("The day is TUESDAY");
			break;
		case 4 :	
			System.out.println("The day is WEDNESDAY");
			break;
		case 5 :
			System.out.println("The day is THURSDAY");
			break;
		case 6 :
			System.out.println("The day is FRIDAY");
			break;
		case 7 :
			System.out.println("The day is SATURDAY");
			break;
			default :
				System.out.println("Wrong number inputted !");
		}	
		scanner.close();
		}
	}


