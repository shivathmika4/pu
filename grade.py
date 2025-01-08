#Write a Python program that takes a student's marks in three subjects as input.
#If the average is greater than or equal to 90, print "Grade: A".
#If the average is between 80 and 89, print "Grade: B".
#If the average is between 70 and 79, print "Grade: C".
#Otherwise, print "Grade: Fail".

marks1=89
marks2=94
marks3=85
average=(marks1+marks2+marks3)//3
if average>=90:
    print("Grade A")
elif average>=80:
    print("Grade B")
elif average>=70:
    print("Grade C")  
else:
    print("Fail")          
