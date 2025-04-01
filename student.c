#include <stdio.h>
struct student{
char name[50];
int roll_no;
float marks[3];
};
int main()
{
int n;
float total=0,avg;
printf("Enter the number of students:");
scanf("%d",&n);
struct student stu[n];
for (int i=0;i<n;i++)
	{
	printf("Enter the details of student %d\n",i+1);
	printf("Name:");
	scanf("%s",stu[i].name);
	printf("Roll No:");
	scanf("%d",&stu[i].roll_no);
	printf("Enter the marks of 3 subjects:");
	for(int j=0;j<3;j++)
	{
	scanf("%f",&stu[i].marks[j]);
	}
	}
printf("Student details:");
for (int i=0;i<n;i++)
	{
	total=0;
	for (int j=0;j<3;j++)
		{
		total+=stu[i].marks[j];
		}
		avg=total/3;
		printf("Student:%d\n Name:%s\n RollNo:%d\n total marks:%.2f\n average marks:%.2f\n",i+1,stu[i].name,stu[i].roll_no,total,avg);
	}
return 0;
}
	
