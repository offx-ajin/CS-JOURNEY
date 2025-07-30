import java.util.Scanner;

class Student
{
	String name;
	int age;
	public void studentdetails()
	{
		System.out.println(name);
		System.out.println(age);
	
	}
}

public class Students  {
	public static void main(String [] args)
	{
	Scanner sc = new Scanner (System.in);
	Student s1 = new Student();
	System.out.println("Enter the name :");
	s1.name = sc.nextLine();
	System.out.println("Enter the age");
	s1.age = sc.nextInt();
	s1.studentdetails();
		
	}}
	
