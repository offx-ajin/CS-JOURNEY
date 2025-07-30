package ajin;
class Details{
	String title;
	String author;
	double price;
	int qua;
	Details(String title,String author,double price,int qua){
		this.title=title;
		this.author=author;
		this.price=price;
		this.qua=qua;
		
	}
	public void Displaydetails() {
		System.out.println("Title:"+title);
		System.out.println("Author :"+ author);
		System.out.println("Price:"+ price);
		System.out.println("Quantity"+ qua);
		System.out.println("Total value :"+ price*qua);
	
	}
}

public class Book {
	public static void main(String[]args) {
		Details b1 = new Details ("Wings","Ajin",250,45);
		b1.Displaydetails();
	}

}
