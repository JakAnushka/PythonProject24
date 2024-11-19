import random

registered_users={"anushka": "lnct123"}

isloggedIn=False
questionlist = ['''Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom''',
'''Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned''',
'''All keywords in Python are in _________
a) Capitalized
b) lower case
c) UPPER CASE
d) None of the mentioned''',
'''What will be the value of the following Python expression?
                    4 + 3 % 5
a) 7
b) 2
c) 4
d) 1''',
'''Which of the following is used to define a block of code in Python language?
a) Indentation
b) Key
c) Brackets
d) All of the mentioned''',
'''Which keyword is used for function in Python language?
a) Function
b) def
c) Fun
d) Define''',
'''Which of the following character is used to give single-line comments in Python?
a) //
b) #
c) !
d) /*''']
answers=["c","d","d","a","a","b","b"]
marks=0



def option():

    print()
    print("1.Registration \n2.Login \n3.Attempt Quiz \n4.Show Result \n5.Exit")

    choosen_opt = int(input("Enter Your choice:"))
    if choosen_opt == 1:
        register()
    elif choosen_opt == 2:
        login()
    elif choosen_opt == 3:
        if loggedIn:
            attemptquiz(questionlist)
        else:
            print("--"*5,"First log in to app!","--"*5)
            login()
    elif choosen_opt == 4:
        showresult()
    elif choosen_opt == 5:
        print("--"*5,"EXIT","--"*5)
    else:
        print("--"*5,"Invalid Input! Try Again","--"*5)


def register():
    print()
    print("--"*5,"Register here if you are new","--"*5)
    username = input("Enter Your Name:")
    password = input("Enter Password:")
    if username.lower() not in registered_users.keys():
        registered_users[username.lower()] = password
        print("--" * 5, "You've Successfully Registered", "--" * 5)

    else:
        print("--"*5,"You're already Registered! Go to Login Page","--"*5)
    option()

def login():
    global loggedIn
    print()
    print("--"*5,"Login Page","--"*5)
    username=input("UserName:").lower()
    password=input("Password:")
    if username in registered_users.keys():
        if password==registered_users[username]:
            print("--"*5,"You've Successfully logged In","--"*5)
            loggedIn=True
            option()
        else:
            print("--"*5,"Incorrect password!","--"*5)
            login()
    else:
        register()


def attemptquiz(questionlist):
    print()
    ask=[]
    global marks
    while len(ask)<len(questionlist):
        ques = random.choice(questionlist)
        if ques not in ask:
            print("--"*15)
            print(ques)
            print("--" * 15)
            ask.append(ques)
            q_index=questionlist.index(ques)
            useranswer=input("Enter answer:").lower()
            if useranswer==answers[q_index]:
                marks+=1
                print("Correct!")
            else:
                print("Incorrect!")
    showresult()



def showresult():
    print()
    if isloggedIn==True:
        print("Your result:",marks)
        print("Wanna Try once again")
        option()
    else:
        print("--"*5,"Please LogIn First","--"*5)
        option()

option()


