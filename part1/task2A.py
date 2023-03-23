import re

i = 0
signup = "Please Enter 1 For SignUp"
signin = "Please Enter 2 For SignIn"
quit = "Please Enter 3 to Quit"
resetPassword = "Please Enter 1 For reseting the password"
signOut = "Please Enter 2 For signing Out"
data = []
dateFormat = re.compile(r'^\d{2}/\d{2}/\d{4}$')
currentYear = 2023

while i == 0:
    print(signup)
    print(signin)
    print(quit)
    userInput = input("Enter 1, 2, or 3:- ")
    if userInput == '1':
        name = input("Please enter your Full Name:- ")
        mobile = input("Please enter your mobile number, start with 0 and must be 10 digits:- ")
        password = input("Create a new password:- ")
        confirmPassword = input("Re-enter your password:- ")
        dateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")

        if name == "" and mobile == "" and password == "" and confirmPassword == "" and dateOfBirth == "":
            print("Inputs cannot be empty, please enter all the inputs")
        else:
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
                break
            else:
                data.append(name)
                data.append(mobile)
                data.append(password)
                data.append(dateOfBirth)
                print("You have Successfully Signed Up")
    elif userInput == '2':
        if len(data) == 0:
            print("You have not Signed Up, Please Sign Up First")
        else:
            j = 0
            for login in range(3):
                username = input(
                    "Please enter your Username (Mobile Number):- ")
                loginPassword = input("Please enter your Password:- ")
                if username == "" and loginPassword == "":
                    print("Inputs cannot be empty, please enter all the inputs")
                else:
                    if username != data[1]:
                        print("Invalid Username, Please try again.")
                    if loginPassword != data[2]:
                        print("Invalid password, Please try again.")
                        j += 1
                        if j == 3:
                            print("You have used maximum attempts oF login, please reset the password.")
                            isUsername = input("Please enter your Username (Mobile Number):- ")
                            isDateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")
                            if isUsername == "" and isDateOfBirth == "":
                                print("Inputs cannot be empty, please enter all the inputs")
                            else:
                                if isUsername == data[1] and isDateOfBirth == data[3]:
                                    newResetPassword = input("Please enter your new password:- ")
                                    confirmNewResetPassword = input("Please re-enter the new password:- ")
                                    if newResetPassword.find('@') == -1:
                                        print("Password must include @")
                                    elif newResetPassword[-1].isdigit() == False:
                                        print("Password must contain a number at the end")
                                    elif newResetPassword == data[2]:
                                        print("You can not re-enter your old password, Please choose new one")
                                    elif newResetPassword == confirmNewResetPassword:
                                        print("Your password has been reset successfully")
                                        data[2] = newResetPassword
                                    else:
                                        print("Passwords do not match with each other.")   
                                        break
                                else:
                                    print("The data you entered are invalid")
                    else:
                        print("You have Successfully Signed In.")
                        print("Welcome,", data[0])
                        print(resetPassword)
                        print(signOut)
                        loggedUserInput = input("Enter 1 or 2:- ")

                        if loggedUserInput == '1':
                            resetUserInput = input("Please enter your Username (Mobile Number):- ")
                            oldPassword = input("Please enter your old password:- ")
                            if resetUserInput == "" and oldPassword == "":
                                print("Inputs cannot be empty, please enter all the inputs")
                            else:
                                if username == data[1] and loginPassword == data[2] and oldPassword == data[2]:
                                    newPassword = input("Please enter your new password:- ")
                                    if newPassword.find('@') == -1:
                                       print("Password must include @")
                                    elif newPassword[-1].isdigit() == False:
                                       print("Password must contain a number at the end")
                                    elif newPassword == data[2]:
                                       print("You can not re-enter your old password, Please choose new one")
                                    else:
                                        data[2] = newPassword
                                        print("Your password has been reset successFully")
                                else:
                                    print("The inFormation you provided is not valid")
                        elif loggedUserInput == '2':
                            print("You are Successlly Signed Out.")
                        else:
                            print("Please enter valid input eg:- 1 or 2.")

    elif userInput == '3':
        print("Thank You for using the Application")
        break
    else:
        print("Please enter valid input eg:- 1, 2 or 3")
