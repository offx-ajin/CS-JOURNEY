#include <stdio.h>
int main()
{
int a[10][10],row1,col1,row2,col2,i,j,b[10][10],sum[10][10];
printf("Enter the number of rows and columns :");
scanf("%d%d",&row1,&col1);
printf("Enter the number of rows and columns :");
scanf("%d%d",&row2,&col2);
if (row1!=row2 && col1!=col2)
	{
	printf("Matrix cannot be added");
	return 0;
	}
else
{
printf("Enter the elements of first matrix");
for (i=0;i<row1;i++)
	{
	for(j=0;j<col1;j++)
		{
		scanf("%d",&a[i][j]);
		}
		
	}
printf("Enter the elements of second matrix");
for (i=0;i<row2;i++)
	{
	for(j=0;j<col2;j++)
		{
		scanf("%d",&b[i][j]);
		}
        }



for (i=0;i<row1;i++)
	{
	for (j=0;j<col1;j++)
		{
		sum[i][j]=a[i][j]+b[i][j];
		}
	}
}	
printf("the resultant matrix\n");
for (i=0;i<row1;i++)
{
for (j=0;j<col1;j++)
{printf(" %d" ,sum[i][j]);
}
printf("\n");
}



return 0;
}
