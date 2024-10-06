# The volume of a sphere with radius r is (4/3)* pie * r**3. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

radius=int(input("Enter radius of sphere:"))
volume=(4/3)*3.14*radius**2
print(f"the volume of the sphere with radius {radius} is {volume:.2f} cubic units.")

# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard.

base_of_triangle=int(input("Enter base of triangle"))
height_of_triangle=int(input("Enter height of triangle"))
area_of_triangle=(1/2*base_of_triangle*height_of_triangle)
print(f"The area of a triangle is {area_of_triangle}")

#Question One
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail

#approach one
def calculate_grade():
  
   mark = int(input("\nEnter mark scored:\t"))

   if mark >=90 and mark <=100: 
      print("GRADE IS A")
   elif mark >=80 and mark <=89: 
      print("GRADE IS B")
   elif mark >=70 and mark <=79:
      print("GRADE IS C")
   elif mark >=60 and mark <=69:
      print("GRADE IS D")
   elif mark >=50 and mark <=59:
      print("GRADE IS E")
   else: print( "Fail")
calculate_grade()


#approach two
marks = int(input("\nEnter marks scored:")) 
if marks >= 90 and marks <=100 :
    print("GRADE A")
elif marks >=80 and marks <=89:
    print("GRADE B")
elif marks >= 70 and marks <= 79:
    print("GRADE C")
elif marks >= 60 and marks <=69:
    print("GRADE D")
elif marks >=50 and marks <= 59:
    print("GRADE E")
else:
    print("FAIL")


#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.



def saccoTransactions():

    accountBalance = 0
    run = 1
    while run == 1:
        
        print("\n welcome to, WITU Academy Sacco")

         #Menu
        print('1.Deposit Money')
        print('1.Withraw Money')
        print('1.Check Balance')

        studentChoice = int(input("Enter your selection(1,2,or 3):"))
         #performing the transactions basing on the selection
        if studentChoice == 1:
            print('\n...processing a deposit transaction...')
            depositAmount = int(input("Enter amount to the deposited:"))
            # checking if deposit amount is less than 1000
            if depositAmount < 1000:
                print('\nMinimum deposit is 1000')
            else:
                accountBalance == depositAmount
                print(f'Dear student, you have deposited{depositAmount:,}and your new account balance is{accountBalance:,}')
                
        elif studentChoice == 2:
            print(f'your account balance is {accountBalance:,}')
            
        elif studentChoice == 3:
            print("you entered a wrong choice!! please select 1,2, or 3\n")

        
        else:
            print("You entered a wrong choice!! Please select 1,2, or 3\n")

            run = int(input("enter 1 to continue or any number to exit:"))
        if run!=1:
            print("thanks for using our sacco")
            break
saccoTransactions()

