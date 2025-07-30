package ajin;

class Shape{
	public int area(int side) {
		System.out.println("I am square");
		return side*side;
		
	}
	
	public int area(int l, int b) {
		System.out.println("i am rectangle");
		return l*b;
		
	}
	public double area(float radius) {
		System.out.println(" i an circle");
		return (3.14 *(radius*radius));
		
		
	}
}

public class Methodoverloading {
	public static void main(String[]args) {
		Shape shape = new Shape();
		
		int rectanglearea = shape.area(5 , 10);
		System.out.println("Area of rectangle:"+rectanglearea);
		
		int squarearea = shape.area(5);
		System.out.println("Area of square:"+squarearea);
		
		double circlearea = shape.area(6.2f);
		System.out.println("Area of circle:"+circlearea);
		
	}

}
