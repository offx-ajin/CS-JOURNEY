echo "Enter 1st number :"
read a
echo "Enter 2nd number :"
read b
echo "enter 1 to add ,2 to sub,3 to multiply, 4 to divide "
read op
case $op in
	1)rs=$((a+b))
	echo "sum=$rs";;
	2)rv=$((a-b))
	echo "sub=$rv";;
	3)rm=$((a*b))
	echo "product=$rm";;
	4)if [ $b -ne 0 ];
	then
	rd=$((a/b))
	echo "quotient=$rd";
	else
	echo "Invalid input"
	fi
esac
