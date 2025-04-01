#include <stdio.h>
struct Employee {
		char name[50];
		int id;
		float salary;
		};
int main()
{
int n,i;
printf("Enter the number of employee:");
scanf("%d",&n);
struct Employee emp[n];
for ( i=0;i<n;i++)
	{
	printf("Enter the details for employee%d:\n",i+1);
	printf("Name:");
	scanf("%s",emp[i].name);
	printf("ID:");
	scanf("%d",&emp[i].id);
	printf("Salary:");
	scanf("%f",&emp[i].salary);
	}
printf("The employees details are :");
for (i=0;i<n;i++)
	{
	printf("Employee %d : Name-%s\nID-%d\nSalary-%f\n",i+1,emp[i].name,emp[i].id,emp[i].salary);
	}
return 0;
}
