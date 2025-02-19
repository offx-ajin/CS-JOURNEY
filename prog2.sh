echo "Enter your first and second number and third number  "
read n1
read n2
read n3

if [ $n1 -gt $n2 ] 
then
	if [$n1 -gt $n3] 
	then
	echo "The largest is $n1"
	else
	echo "The largest is $n3"
	fi
	
else 

	if [$n2 -gt $n3]
	then 
	echo "The largest is $n2"
	else
	echo "The largest is $n3"
	fi
fi

	

