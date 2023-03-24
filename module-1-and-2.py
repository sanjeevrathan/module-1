class authentication(object):
    def __init__(self, password=''):
        self.password = password
        
    def lower(self):
        lower = any(c.islower() for c in self.password)
        return lower
    def upper(self):
        upper = any(c.islower() for c in self.password)
        return upper
    def digit(self):
        digit = any(c.islower() for c in self.password)
        return digit
    def Validate(self):
        lower = self.lower()
        upper = self.upper()
        digit = self.digit()        
        length = len(self.password)
        report = lower and upper and digit and length >= 8
        
        if report:
            return True
        elif not lower:
            print("Password must atleast have a lower case")
            return False
        elif not upper:
            print("Password must atleast have a lower case")
            return False
        elif not digit:
            print("Password must have a digit")
            return False
        elif length < 8:
            print("Pasword must be atleast 8 characters")
            return False
        else:
            pass
class Authentication(object):
    def __init__(self, username=''):
        self.username = username
        
    def validation(self):
        length = len(self.username)
        report = length >= 6
        if report:
            return True
        elif length < 6:
            print("username should atleast have 6 characters")
            return False
        else:
            pass

C = Authentication(input("Enter your username : "))
print(C.validation())
D = authentication(input("Enter your password : "))
print(D.Validate())

password = D.Validate()
pass_in_use = [password]

for i in range(6):
    curr_password = input("Enter password again: ")
    if curr_password in pass_in_use:
        print("You have used this password 5 times before.")
        print("Please change your password to continue.")
        new_password = input("Enter a new password: ")
        password = new_password
        pass_in_use = [password]
        for x in range(len(pass_in_use)):
            print (*pass_in_use)
        print("Password changed successfully!")
        break 
    elif curr_password == password:
        print("Login successful!")
        break 
    else:
        print("Incorrect password. Please try again.")

    pass_in_use.append(curr_password)
else:
    print("Maximum login attempts reached. Please try again later.")
