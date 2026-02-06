A. Python IF (Single Condition)\par
#1. Write a Python program to check if a number is positive\par
"""\par
num = 20\par
if num>0:\par
    print("positive")\par
    \par
#2. Print "Eligible to vote" if age is 18 or above.\par
\par
age =21\par
if age>=18:\par
    print("Eligible to vote")\par
\par
#3.Check if a number is divisible by 7.\par
num = 14\par
if num%7==0:\par
    print("divisible")\par
\par
#4. Print "Pass" if marks are greater than 40.\par
marks =50\par
if marks>40:\par
    print("pass")\par
\par
#5. Check if a number is greater than 100.\par
num = 95\par
if num>100:\par
    print(greater)\par
   \par
#6. Display a message if temperature exceeds 45\'b0C.\par
temperature = 55\par
if temperature>45:\par
    print("High alert")\par
    \par
#7. Check if a string length is more than 8 characters.\par
\par
#8. Print "Logged In" if password matches "admin123".\par
password ="admin123"\par
if password=="admin123":\par
    print("logged in")\par
\par
#9. Check if a number is a multiple of 10.\par
num = 20\par
if num%10==0:\par
    print("yes")\par
    \par
#10. Print a warning if balance is below minimum limit.\par
balance = 1000\par
if balance<2000:\par
    print("warning")\par
    \par
#B. Python IF\f1\endash ELSE (Two Conditions)\par
#11. Check whether a number is even or odd.\par
num =int(input("enter a number:"))\par
if num%2==0:\par
    print("even")\par
else:    \par
    print("odd")\par
\par
#12. Find the largest of two numbers.\par
n1 =300\par
n2 =40\par
if n1>n2:\par
    print(n1)\par
else:\par
    print(n2)\par
\par
#13. Check whether a person is eligible for driving license.\par
age =13\par
if age>18:\par
    print("eligible")\par
else:\par
    print("not eligible")\par
    \par
#14. Print "Pass" or "Fail" based on marks.\par
marks = 95\par
if marks>=55:\par
    print("pass")\par
else:\par
    print("fail")\par
    \par
#15. Check whether a number is positive or negative.\par
num = -4\par
if num>0:\par
    print("positive")\par
else:\par
    print("negative")\par
   \par
#16. Check whether a character is a vowel or consonant\par
ch = "s"\par
if ch in "AIOUEaioue":\par
    print("vowel")\par
else:\par
    print("consonant")\par
 \par
#17. Check if a year is leap or not\par
"""\par
"""\par
#18. Print "Valid Password" or "Invalid Password".\par
password = "helloindia"\par
if password=="helloindia":\par
    print("valid password")\par
else:\par
    print("invalid password")\par
\par
#19. Determine whether salary is taxable or not.\par
salary = 500000\par
if salary>=7000000:\par
    print("taxable")\par
else:\par
    print("not taxable")\par
    \par
#20. Check whether a number is greater than 50 or not.\par
num =int(input("enter a number:"))\par
if num>50:\par
    print("yes")\par
else:\par
    print("no")\par
    "\par
#C. Python NESTED IF\endash ELSE\par
#21. Find the largest of three numbers.\par
n1 = 10000\par
n2 = 4000000\par
n3 = 500000\par
if n1>n2:\par
    if n1>n3:\par
        print(n1)\par
    else:\par
        print(n3)\par
else:\par
    if n2>n3:\par
        print(n2)\par
    else:\par
        print(n3)\par
        \par
#22. Check whether a number is positive, negative, or zero.\par
num = 5\par
if num>0:\par
    if num<0:\par
        print("negative")\par
    else:\par
        print("positive")\par
else:\par
    print("zero")\par
        \par
#23. Assign grades:\par
#A \f2\u8594?\f0  marks \f2\u8805?\f0  90\par
#B \f2\u8594?\f0  marks \f2\u8805?\f0  75\par
#C \f2\u8594?\f0  marks \f2\u8805?\f0  60\par
#Fail \f2\u8594?\f0  below 60\par
marks =45\par
if marks>=90:\par
    print("A")\par
else:\par
    if marks>=75:\par
        print("B")\par
    else:\par
        if marks>=60:\par
            print("C")\par
        else:\par
            print("fail")\par
            \par
        \par
#24. Check whether a triangle is equilateral, isosceles, or scalene   \par
#25. Check whether a character is uppercase, lowercase, digit, or special character.\par
ch ="sanjana"\par
if ch >="0":\par
    if ch<="9":\par
        print("digit")\par
    else:\par
        if ch>="a":\par
            if ch<="z":\par
                print("lowercase")\par
            else:\par
                if ch>="A":\par
                    if ch<="Z":\par
                        print("uppercase")\par
                    else:\par
                        print("special character")\par
\par
 \par
#26. Calculate electricity bill using slab-wise rates.\par
#27. Validate login using username and password.\par
username ="sanjana.33"\par
password ="1234"\par
if username=="sanjana.33":\par
    if password=="1234":\par
        print("login done")\par
    else:\par
        print("not valid")\par
else:\par
    print("no valid")\par
\par
#28. Check student result using marks of 3 subjects.\par
hindi = 40\par
english = 40\par
maths = 40\par
if hindi>=40:\par
    if english>=40:\par
        if maths>=40:\par
            print("pass")\par
        else:\par
            print("maths_fail")\par
    else:\par
        print("english_fail")\par
else:\par
    print("hindi_fail")\par
    \par
#29. Find the second largest number among three numbers.\par
#30. Check loan eligibility using age, salary, and credit score\par
age = "31"\par
salary = "50000"\par
creditscore ="700"\par
\par
if age>="21":\par
    if salary>="50000":\par
        if creditscore>="700":\par
            print("verified")\par
        else:\par
            print("poor cs")\par
    else:\par
        print("low salary")\par
else:\par
    print("below 21")\par
    \par
#D. Python ELIF (Multiple Conditions)\par
#31. Print day name using day number (1\f1\endash 7).\par
num =5\par
if num==1:\par
    print("monday")\par
elif num==2:\par
    print("tuesday")\par
elif num==3:\par
    print("wednesday")\par
elif num==4:\par
    print("thursday")\par
elif num==5:\par
    print("friday")\par
elif num==6:\par
    print("saturday")\par
elif num==7:\par
    print("sunday")\par
else:\par
    print("not valid")    \par
\par
#32. Print month name using month number.\par
num =9\par
if num==1:\par
    print("january,")\par
elif num==2:\par
    print("february")\par
elif num==3:\par
    print("march")\par
elif num==4:\par
    print("april")\par
elif num==5:\par
    print("may")\par
elif num==6:\par
    print("june")\par
elif num==7:\par
    print("july")\par
elif num==8:\par
    print("august")\par
elif num==9:\par
    print("september")\par
elif num==10:\par
    print("october")\par
elif num==11:\par
    print("november")\par
elif num==12:\par
    print("december")\par
else:\par
    print("not valid")\par
\par
#33. Display grade based on percentage.\par
per=74\par
if per>=90:\par
    print("A")\par
elif per>=80:\par
    print("B")\par
elif per>=70:\par
    print("C")\par
elif per>=60:\par
    print("D")\par
else:\par
    print("fail")\par
    \par
#34. Display bonus percentage based on experience years.\par
year=4\par
if year>=10:\par
    print("15%bonus")\par
elif year>=5:\par
    print("10%bonus")\par
elif year>=1:\par
    print("5%bonus")\par
\par
#35. Identify traffic signal meaning\par
signal="yellow"\par
if signal=="red":\par
    print("stop")\par
elif signal=="yellow":\par
    print("slow down")\par
elif signal=="green":\par
    print("go")\par
    \par
#36. Categorize temperature as Cold / Warm / Hot.\par
tem =11\par
if tem>30:\par
    print("hot")\par
elif tem>=20:\par
    print("warm")\par
elif tem<=19:\par
    print("cold")\par
    \par
#37. Categorize employee based on salary range.\par
salary=90000\par
if salary>=100000:\par
    print("high salary")\par
elif salary>=50000:\par
    print("mid salary")\par
elif salary<50000:\par
    print("low salary")\par
   \par
#38. Print discount percentage based on purchase amount.\par
amt =110000\par
if amt>=10000:\par
    print("500%")\par
elif amt>=5000:\par
    print("100%")\par
elif amt<5000:\par
    print("50%")\par
    \par
#39. Identify number type: single-digit / double-digit / multi-digit.\par
num = 67\par
if num>=100:\par
digit")\par
elif num>=10:\par
    print("double-digit")\par
elif num>=1:\par
    print("single digit")\par
    \par
#40. Assign performance rating: Poor / Average / Good / Excellent.\par
rating =1\par
if rating==10:\par
    print("excellent")\par
elif rating==8:\par
    print("good")\par
elif rating>=5:\par
    print("average")\par
elif rating==1:\par
    print("poor")\par
    \par
#E. Python COMPLEX CONDITIONS (AND / OR / NOT)\par
#41. Check whether a number is divisible by 5 and 11\par
num = 55\par
if num%11==0 and num%5==0:\par
    print("divisible")\par
else:\par
    print("not")\par
    \par
#42. Check if a person is eligible for loan:\par
#\f3\u9679?\f0  age \f2\u8805?\f0  21\par
#\f3\u9679?\f0  salary \f2\u8805?\f0  25,000\par
#\f3\u9679?\f0  credit score \f2\u8805?\f0  700\par
age =23\par
salary =25000\par
credit_score =800\par
if age>=21 and salary>=25000 and credit_score>=700:\par
    print("eligible")\par
else:\par
    print("not eligible")\par
    \par
#43. Validate login using username AND password.\par
user ="sanjana"\par
password ="124"\par
if user=="sanjana" and password=="1234":\par
    print("login done")\par
else:\par
    print("invalid")\par
    \par
#44. Check student pass condition:\par
#All subjects \f2\u8805?\f0  40\par
#Average \f2\u8805?\f0  50\par
hindi = 85\par
maths =40\par
english =80\par
history =56\par
if hindi>=40 and maths>=40 and english>=40 and history>=40:\par
    print("pass")\par
else:\par
    print("fail")\par
    \par
#45. Check if a number lies between 10 and 100\par
num =67\par
if num>=10 and num<=100:\par
    print(num)\par
else:\par
    print("invalid")\par
    \par
#46. Check exam eligibility:\par
#attendance \f2\u8805?\f0  75% OR\par
#medical certificate available\par
attendance =84\par
mc="no"\par
if attendance>=75 or mc=="yes":\par
    print("eligible for exam")\par
else:\par
    print("not eligible")\par
   \par
#47. Validate a date using conditions.\par
date =30\par
if date>=1 and date<=31:\par
    print("valid")\par
else:\par
    print("not valid")\par
    \par
#48. Check whether an email format is valid.\par
#49. Determine insurance eligibility using age, health status, and income\par
#50. Check leap year using complete leap year logic\par
\par
#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS\par
#51. Write a Python program to calculate income tax using slabs.\par
inc =300000\par
if inc>=2000000:\par
    print("25%")\par
elif inc>=1600000:\par
    print("20%tax")\par
elif inc>=1200000:\par
    print("15%tax")\par
elif inc>=800000:\par
    print("10%tax")\par
elif inc>=400000:\par
    print("5%tax")\par
else:\par
    print("0%tax")\par
#52. Create an ATM withdrawal program with balance checks.\par
\par
#53. Check promotion eligibility using experience and performance.\par
per=6\par
exp=5\par
if per>=5 and exp>=4:\par
    print("eligible")\par
else:\par
    print("not eligible")\par
\par
#54. Implement a grading system using nested if\f1\endash else.\par
grade=69\par
if grade>=90:\par
    print("A")\par
else:\par
    if grade>=80:\par
        print("B")\par
    else:\par
        if grade>=70:\par
            print("C")\par
        else:\par
            if grade>=60:\par
                print("D")\par
            else:\par
                if grade<60:\par
                    print("fail")\par
\par
#55. Validate strong password using multiple conditions\par
\par
#56. Calculate delivery charges based on location and order amount\par
location = "50km"\par
order_amt=15000\par
if location=="50km" and order_amt>=2000:\par
    print("100rs charges")\par
elif location=="25km" and order_amt>=1000:\par
    print("free delivery")\par
elif location=="15km" and order_amt>=500:\par
    print("50rs charges")\par
elif location=="10km" and order_amt>=200:\par
    print("20rs charges")\par
    \par
#57. Determine online exam qualification.\par
#58. Create movie ticket pricing logic based on age & show time.age = 13\par
show_time ="3 hour"\par
if age>=60 and show_time=="3 hour":\par
    print("200+20%dis")\par
elif age>=19 and show_time=="3 hour":\par
    print("300rs")\par
elif age>=13 and show_time=="2 hour":\par
    print("100rs")\par
elif age>=8 and show_time=="1 hour":\par
    print("50+10%dis")\par
"""\par
#59. Determine bank account type based on balance.\par
#60. Create a menu-driven program using if\endash elif\endash else.   \f0\lang9\par
}
 
