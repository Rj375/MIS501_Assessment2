import re


signup = "Please Enter 1 For SignUp"
signin = "Please Enter 2 For SignIn"
quit = "Please Enter 3 to Quit"
resetPassword = "Please Enter 1 For reseting the password"
passwordErrorMessage = "Password must start with alphabetic characters, must contain one @ and must end with digit"
signOut = "Please Enter 2 For signing Out"
data = []
dateFormat = re.compile(r'^\d{2}/\d{2}/\d{4}$')
currentYear = 2023
emptyInputs = "Inputs cannot be empty, please enter all the inputs"

MobileValidationRegex = re.compile(r'^0[0-9]{9}$')
PasswordValidationRegex = re.compile(r'^[a-zA-Z@]*\d$')


while True: #this loop keeps running until the condition is met and user do not break loop.
    print(signup)
    print(signin)
    print(quit)
   
    
    userInput = input("Enter 1, 2, or 3:- ") #it takes input values either 1,2 or 3.
       
    if userInput == '1': #iF user types 1, then program takes user to signUp section.
        name = input("Please enter your Full Name:- ")
        mobile = input("Please enter your mobile number, start with 0 and must be 10 digits:- ")
        password = input("Create a new password:- ")
        confirmPassword = input("Re-enter your password:- ")
        dateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")
        
        #checks is there any inputs Fields leFt empty or not.
        if name == "" and mobile == "" and password == "" and confirmPassword == "" and dateOfBirth == "":
            print(emptyInputs)
        else:
            yearOfBirth = dateOfBirth.split("/") #only the year taken From the input with the split method.            
            convertedYearOfBirth = int(yearOfBirth[2]) #year oF birth is converted to integer.           
            age = currentYear - convertedYearOfBirth #it calculates the age oF user.           
            isMobileValid = re.search(MobileValidationRegex, mobile) #checks For the valid mobile input with regular expression.           
            isPasswordValid = re.search(PasswordValidationRegex, password) #checks For the valid password input with regular expression.

            #this condition checks are all the required things are there or not.
            if isMobileValid == None: #checks whether there is 0 in number or not.
                print("Mobile number must start with 0 and must be equal to 10 digits")            
            elif not dateFormat.match(dateOfBirth): #checks the Format oF date oF birth is correct or not.
                print("You have entered a date of birth in invalid format. Please try again.")            
            elif isPasswordValid == None: #checks whether the password starts with alpha, contains @ or not and end with digit or not.
                print(passwordErrorMessage)            
            elif password != confirmPassword: #checks whether the password and conFIrmPassword match or not.
                print("Your passwards are not matching. Please try again:")           
            elif age < 21: #checks whether the user is below 21 years old or not.
                print("You must be at least 21 years old to Sign Up")
                break
            else:
                #it adds all the input value in list called data.
                data.append(name)
                data.append(mobile)
                data.append(password)
                data.append(dateOfBirth)
                print("You have Successfully Signed Up")  
    elif userInput == '2':  #iF the user type 2 in input value, the user is taken to sign In section.
        if len(data) == 0: #checks whether the length oF the data is 0 or not.
            print("You have not Signed Up, Please Sign Up First")
        else:
            j = 0           
            for login in range(3): #it is a loop that loops 3 times.
                username = input("Please enter your Username (Mobile Number):- ")
                loginPassword = input("Please enter your Password:- ")           
                if username == "" and loginPassword == "": #checks whether the inputs are empty or not.
                    print(emptyInputs)
                else:                   
                    if username != data[1]: #checks whether the username user typed is in list oF data or not.
                        print("Invalid Username, Please try again.")
                    if loginPassword != data[2]: #checks whether the password user typed is in list oF data or not.                       
                        j += 1 #j is increaced by 1 every time user types wrong credentials.
                        print("Invalid Password. you have used",j,"attempts out oF 3 attempts")                       
                        #iF j is equal to 3.                       
                        if j == 3: #iF user Fails to give valid username or password For 3 times then, user is taken to reset password section.
                            print("You have used maximum attempts oF login, please reset the password.")
                            isUsername = input("Please enter your Username (Mobile Number):- ")
                            isDateOfBirth = input("Enter a date of birth (DD/MM/YYYY) No Space:- ")
                           
                            if isUsername == "" and isDateOfBirth == "":  #checks whether the inputs are empty or not.
                                print(emptyInputs)
                            else:
                                if isUsername == data[1] and isDateOfBirth == data[3]:
                                    newResetPassword = input("Please enter your new password:- ")
                                    confirmNewResetPassword = input("Please re-enter the new password:- ")
                                                                        
                                    isResetPasswordValid = re.search(PasswordValidationRegex, newResetPassword) #checks For the valid reset password input with regular expression.
                                    
                                    if isResetPasswordValid == None: #checks whether the password starts with alpha, contains @ or not and end with digit or not.
                                        print(passwordErrorMessage)                                    
                                    elif newResetPassword == data[2]: #checks whether the password entered matches the password in list oF data.
                                        print("You can not re-enter your old password, Please choose new one")                                    
                                    elif newResetPassword == confirmNewResetPassword: #checks whether the password entered matches the conFirm password.
                                        print("Your password has been reset successfully")                                       
                                        data[2] = newResetPassword #it replaces the new password with old password in the list oF data.
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
                                               
                        loggedUserInput = input("Enter 1 or 2:- ") #asking user to type either 1 or 2.
                        
                        if loggedUserInput == '1': #iF user types 1, then user is taken to reset password section.
                            resetUserInput = input("Please enter your Username (Mobile Number):- ")
                            oldPassword = input("Please enter your old password:- ")
                            
                            if resetUserInput == "" and oldPassword == "": #checks whether the inputs are empty or not.
                                print(emptyInputs)
                            else:
                                #checks whether username, login password and oldpassword matches with values in list oF data.
                                #iF they match then user is given permission to reset password.
                                if username == data[1] and loginPassword == data[2] and oldPassword == data[2]:
                                    newPassword = input("Please enter your new password:- ")
                                   
                                    isNewPasswordValid = re.search(PasswordValidationRegex, newPassword) #checks For the valid reset password input with regular expression.
                                   
                                    if isNewPasswordValid == None: #checks whether the password starts with alpha, contains @ or not and end with digit or not.
                                       print(passwordErrorMessage)                                    
                                    elif newPassword == data[2]: #checks whether new password matches with password in list oF data/old password or not.
                                       print("You can not re-enter your old password, Please choose new one")
                                    else:                                       
                                        data[2] = newPassword #iF everything is good, then password in list oF data is replaces by new password.
                                        print("Your password has been reset successFully")
                                else:
                                    print("The inFormation you provided is not valid")                      
                        elif loggedUserInput == '2': #iF user types 2, then user is sign out and taken to login section.
                            print("You are Successlly Signed Out.")
                        else:
                            print("Please enter valid input eg:- 1 or 2.")   
    elif userInput == '3': #iF user types 3, then the application is closed or breaks the loop.
        print("Thank You for using the Application")
        break
    else:
        print("Please enter valid input eg:- 1, 2 or 3")
