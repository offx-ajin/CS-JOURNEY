import java.util.Scanner;

class Details {
	String name;
	int rollno;
	int mat;
	int phy;
	int che;
	float avg;
	Details(String name,int rollno,int mat , int phy ,int che ){
		this.name = name;
		this.rollno = rollno;
		this.mat = mat;
		this.phy = phy;
		this.che = che;
		
	}
	public void avgcalculator(){
		avg = (mat+phy+che)/3;
	}
	public void displaydetails()
	{
		System.out.println("Name :"+ name);
		System.out.println("Roll no:"+ rollno);
		System.out.println("Maths : "+ mat);
		System.out.println("Physics :"+ phy);
		System.out.println("Chemistry"+ che);
		
				
	}
}

public class Average {
	public static void main(String[]args) {
		Details student1 = new Details("Ajin",11,45,65,47);
		student1.displaydetails();
		student1.avgcalculator();
		Details student2 = new Details("Saji",15,45,67,86);
		student2.displaydetails();
		student2.avgcalculator();
	}

	}


