# --------------Simple Logging System
#2020-2021
#python 3.8
#programmer : fazelahmadi32@gmail.com
#--------------------------------------------------------------------#
#reading users and passwords from txt files
allowed_users = open('users.txt', 'r').read() 
allowed_passwords = open('passwords.txt', 'r').read()
#convert lines to python lists
lines_users = allowed_users.split('\n')
lines_passwords = allowed_passwords.split('\n')

def main():
    userName = input("Enter username: ")
    if userName == '':
        raise Exception("dont put empty")
    
    if userName in allowed_users:
        #find the location of user in the users file
        for i, line in enumerate(lines_users): 
            if userName in line:
                userName_line_count = i+1;
                
        passWord = input("Enter password: ")
        if passWord == '':
            raise Exception("dont put empty")
        
        if passWord in allowed_passwords:
            #find the location of password in the passwords file
            for i, line in enumerate(lines_passwords):
                if passWord in line:
                    passWord_line_count = i+1;
            
            #check if password belong to exact user;
            if userName_line_count == passWord_line_count:
                print("logged in\nwellcome {}".format(userName));
            elif userName_line_count != passWord_line_count:
                print("worng password")
                return main()
            else:
                raise Exception("undifined info!")
        
        elif passWord not in allowed_passwords:
            return main()
                
    elif userName not in allowed_users:
        print("sorry, your name is not in the list")
        
        
        def add_New_User(): # add new user to users list;
            new_User = input("Enter username you want: ")
            if new_User in allowed_users: # check if username been taken or not;
                print("The username has been taken")
                return add_New_User();
            
            else:
                new_User_Pass = input("Enter Password you want: ")
                #open txt files in 'a' mode;
                users_update = open('users.txt', 'a')
                passwords_update = open('passwords.txt', 'a')
                #update txt files data;
                users_update.write(new_User)
                users_update.write('\n')
                users_update.close()
                passwords_update.write(new_User_Pass)
                passwords_update.write('\n')
                passwords_update.close()
                
        add_New_User();
                
    else:
        quit()
                
main()
    