import java.util.Scanner;

public class Odd_num {
	public static void main(String [] args) {
		Scanner scanner = new Scanner (System.in);
		
		System.out.println("enter a number :");
		int n=scanner.nextInt();
		
		for(int i=1;i<=n;i++)
		{
			if (i%2 == 0) {
				continue;
			}
			
			
				System.out.println(i);
			}
		}

}