class kids {
String name;
public static int studentCount;
kids(String name){
	this.name=name;
	studentCount ++;
	
}
public static  int getstudentCount() {
	return studentCount;
	
}
}
public class Static {
	public static void main(String []args) {
		kids s1 =  new kids("Ajin");
		kids s2 = new kids("Christ");
		kids s3 = new kids("Alvin");
		int total = kids.getstudentCount();
		System.out.println("No of Students = "+ total);
	}

}
