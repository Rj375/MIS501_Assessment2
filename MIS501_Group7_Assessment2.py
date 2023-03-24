import re


signup = "Please Enter 1 For SignUp"
signin = "Please Enter 2 For SignIn"
quit = "Please Enter 3 to Quit"
resetPassword = "Please Enter 1 For reseting the password"
signOut = "Please Enter 2 For signing Out"
data = []
dateFormat = re.compile(r'^\d{2}/\d{2}/\d{4}$')
currentYear = 2023
emptyInputs = "Inputs cannot be empty, please enter all the inputs"

#this loop keeps running until the condition is met and user do not break loop.
while True: 
    print(signup)
    print(signin)
    print(quit)
   
    #it takes input values either 1,2 or 3.
    userInput = input("Enter 1, 2, or 3:- ") 
    
    #iF user types 1, then program takes user to signUp section.
    if userInput == '1':
        name = input("Please enter your Full Name:- ")
        mobile = input("Please enter your mobile number, start with 0 and must be 10 digits:- ")
        password = input("Create a new password:- ")
        confirmPassword = input("Re-enter your password:- ")
        dateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")
        
        #checks is there any inputs Fields leFt empty or not.
        if name == "" and mobile == "" and password == "" and confirmPassword == "" and dateOfBirth == "":
            print(emptyInputs)
        #iF all the input are Field then it proceeds to Further process.
        else:
            #only the year taken From the input. 
            yearOfBirth = dateOfBirth[-4:] 
            #year oF birth is converted to integer.
            convertedYearOfBirth = int(yearOfBirth) 
            #it calculates the age oF user.
            age = currentYear - convertedYearOfBirth
            #this is For the password validation which checks is there any number in end oF password.
            numericValueAtTheEnd = password[-1].isdigit()

            #this condition checks are all the required things are there or not.
            #checks whether there is 0 in number or not.
            if mobile.find('0') == -1:
                print("Mobile number must contain 0 at the beginning")
            #checks whether the 0 is in index 0 or not.
            elif mobile.index('0') != 0:
                print("Mobile number must start with 0")
            #checks the length of the mobile number == 10 or not.
            elif len(mobile) != 10:
                print("Mobile number must not be less than or greater than 10 digits")
            #checks the Format oF date oF birth is correct or not.
            elif not dateFormat.match(dateOfBirth):
                print("You have entered a date of birth in invalid format. Please try again.")
            #checks whether the password contains @ or not.
            elif password.find('@') == -1:
                print("Password must include @")
            #checks is there any number in end oF password.
            elif numericValueAtTheEnd == False:
                print("Password must contain a number at the end")
            #checks whether the password and conFIrmPassword match or not.
            elif password != confirmPassword:
                print("Your passwards are not matching. Please try again:")
            #checks whether the user is below 21 years old or not.
            elif age < 21:
                print("You must be at least 21 years old to Sign Up")
                break
            else:
                #it adds all the input value in list called data.
                data.append(name)
                data.append(mobile)
                data.append(password)
                data.append(dateOfBirth)
                print("You have Successfully Signed Up")
    #iF the user type 2 in input value, the user is taken to sign In section.
    elif userInput == '2':
        #checks whether the length oF the data is 0 or not.
        if len(data) == 0:
            print("You have not Signed Up, Please Sign Up First")
        else:
            j = 0
            #it is a loop that loops 3 times.
            for login in range(3):
                username = input("Please enter your Username (Mobile Number):- ")
                loginPassword = input("Please enter your Password:- ")
                #checks whether the inputs are empty or not.
                if username == "" and loginPassword == "":
                    print(emptyInputs)
                else:
                    #checks whether the username user typed is in list oF data or not.
                    #iF not it throws error message.
                    if username != data[1]:
                        print("Invalid Username, Please try again.")
                    #checks whether the password user typed is in list oF data or not.
                    #iF not it throws error message.
                    if loginPassword != data[2]:
                        #j is increaced by 1 every time user types wrong credentials.
                        j += 1
                        print("Invalid Password. you have used",j,"attempts out oF 3 attempts")
                        
                        #iF j is equal to 3.
                        #iF user Fails to give valid username or password For 3 times then, user is taken to reset password section.
                        if j == 3:
                            print("You have used maximum attempts oF login, please reset the password.")
                            isUsername = input("Please enter your Username (Mobile Number):- ")
                            isDateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")
                            #checks whether the inputs are empty or not.
                            if isUsername == "" and isDateOfBirth == "":
                                print(emptyInputs)
                            else:
                                if isUsername == data[1] and isDateOfBirth == data[3]:
                                    newResetPassword = input("Please enter your new password:- ")
                                    confirmNewResetPassword = input("Please re-enter the new password:- ")
                                    #checks whether the input contains @ or not.
                                    if newResetPassword.find('@') == -1:
                                        print("Password must include @")
                                    #checks whether the input contains number at the end or not.
                                    elif newResetPassword[-1].isdigit() == False:
                                        print("Password must contain a number at the end")
                                    #checks whether the password entered matches the password in list oF data.
                                    elif newResetPassword == data[2]:
                                        print("You can not re-enter your old password, Please choose new one")
                                    #checks whether the password entered matches the conFirm password.
                                    elif newResetPassword == confirmNewResetPassword:
                                        print("Your password has been reset successfully")
                                        #it replaces the new password with old password in the list oF data.
                                        data[2] = newResetPassword
                                    else:
                                        print("Passwords do not match with each other.")   
                                        break
                                else:
                                    print("The data you entered are invalid")
                    else:
                        #iF username and password are correct then these messages pops up.
                        print("You have Successfully Signed In.")
                        print("Welcome,", data[0])
                        print(resetPassword)
                        print(signOut)
                        
                        #asking user to type either 1 or 2.
                        loggedUserInput = input("Enter 1 or 2:- ")

                        #iF user types 1, then user is taken to reset password section.
                        if loggedUserInput == '1':
                            resetUserInput = input("Please enter your Username (Mobile Number):- ")
                            oldPassword = input("Please enter your old password:- ")
                            #checks whether the inputs are empty or not.
                            if resetUserInput == "" and oldPassword == "":
                                print(emptyInputs)
                            else:
                                #checks whether username, login password and oldpassword matches with values in list oF data.
                                #iF they match then user is given permission to reset password.
                                if username == data[1] and loginPassword == data[2] and oldPassword == data[2]:
                                    newPassword = input("Please enter your new password:- ")
                                    #checks whether password has @ or not.
                                    if newPassword.find('@') == -1:
                                       print("Password must include @")
                                    #checks whether password has number at the end or not.
                                    elif newPassword[-1].isdigit() == False:
                                       print("Password must contain a number at the end")
                                    #checks whether new password matches with password in list oF data/old password or not.
                                    elif newPassword == data[2]:
                                       print("You can not re-enter your old password, Please choose new one")
                                    else:
                                        #iF everything is good, then password in list oF data is replaces by new password.
                                        data[2] = newPassword
                                        print("Your password has been reset successFully")
                                else:
                                    print("The inFormation you provided is not valid")
                        #iF user types 2, then user is sign out and taken to login section.
                        elif loggedUserInput == '2':
                            print("You are Successlly Signed Out.")
                        else:
                            print("Please enter valid input eg:- 1 or 2.")
    #iF user types 3, then the application is closed or breaks the loop.
    elif userInput == '3':
        print("Thank You for using the Application")
        break
    else:
        print("Please enter valid input eg:- 1, 2 or 3")
