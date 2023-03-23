import re

i = 0
signup = "Please Enter 1 For SignUp"
signin = "Please Enter 2 For SignIn"
quit = "Please Enter 3 to Quit"
data = []
dateFormat = re.compile(r'^\d{2}/\d{2}/\d{4}$')
currentYear = 2023

print(data)
while i == 0:
    print(signup)
    print(signin)
    print(quit)
    userInput = input("Enter 1, 2, or 3:- ")
    if userInput == '1':
        mobile = input("Please enter your mobile number, start with 0 and must be 10 digits:- ")
        password = input("Create a new password:- ")
        confirmPassword = input("Re-enter your password:- ")
        dateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")

        yearOfBirth = dateOfBirth[-4:]
        convertedYearOfBirth = int(yearOfBirth)
        age = currentYear - convertedYearOfBirth
        
        numericValueAtTheEnd = password[-1].isdigit()
   

        if mobile.find('0') == -1:
            print("Mobile number must contain 0 at the beginning")
        elif mobile.index('0') != 0:
            print("Mobile number must start with 0")
        elif len(mobile) != 10:
            print("Mobile number must not be less than or greater than 10 digits")
        elif not dateFormat.match(dateOfBirth):
            print("You have entered a date of birth in invalid format. Please try again.")
        elif password.find('@') == -1:
            print("Password must include @")
        elif numericValueAtTheEnd == False:
            print("Password must contain a number at the end")
        elif password != confirmPassword:
            print("Your passwards are not matching. Please try again:")
        elif age < 21:
            print("You must be at least 21 years old to Sign Up")
        else:
            data.append(mobile)
            data.append(password)
            data.append(dateOfBirth)
            print("You have Successfully Signed Up")
    elif userInput == '2':
        print("SignIn")
        i+=1
    elif userInput == '3':
        print("Thank You for using the Application")
        break    
    else:
        print("no")
       
        
        
