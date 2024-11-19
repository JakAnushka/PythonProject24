import random
logged = False
log_user = ''
marks=0

def register():
    na = input("Enter your name: ")
    en = input("Enter your enrollment: ")
    clg = input("Enter your college: ")
    pwd = input("Enter your password: ")

    with open('userDetails.txt', 'a') as user:
        user.write(f"{na},{en},{clg},{pwd}\n")

    with open('loginDetails.txt', 'a') as login:
        login.write(f"{en},{pwd}\n")
    main()


def login():
    global logged
    global log_user
    en = input("Enter your Enrollment: ")
    pw = input("Enter your password: ")

    with open('loginDetails.txt', 'r') as login:
        us = login.readlines()
        for i in us:
            i = i.replace('\n', '')
            li = i.split(',')
            if li[0] == en and li[1] == pw:
                print("login successful")
                logged = True
                log_user = en
                break
        else:
            print("Wrong Credentials")
        main()


# login()


def changePassword():
    global logged
    global log_user

    if logged:
        with open('loginDetails.txt', 'r') as file:
            file.readlines()
def attemptQuiz():
    print()
    ask = []
    global marks
    # if logged==False:
    #     print("--" * 5, "Please LogIn First", "--" * 5, "\n")
    #     main()
    choice=input('''a. DSA b. DBMS c. Python''').lower()
    questions = []
    answers=[]

    if choice=='a':
        with open("dsa.txt", mode="r") as file:

            questions = file.readlines()

        ques_num = random.randint(0, len(questions) - 1)
        answers = ["d", "d", "c", "a", "a", "a", "d"]

    elif choice=="b":
        with open("dbms.txt", mode="r") as file:

            questions = file.readlines()

        ques_num = random.randint(0, len(questions) - 1)

        answers = ["b", "d", "b", "d", "c", "d", "d"]
    elif choice=="c":
        with open("python.txt", mode="r") as file:

            questions = file.readlines()

        ques_num = random.randint(0, len(questions) - 1)
        answers=["c","d","d","a","a","b","b"]
    else:
        print("Invalid Input !")

    while len(ask) < len(questions):
        ques = random.choice(questions)
        if ques not in ask:
            print("--" * 15)
            question=ques.split(",")
            for q in question:
                print(q)
            print("--" * 15)
            ask.append(ques)
            q_index = questions.index(ques)
            useranswer = input("Enter answer:").lower()
            if useranswer == answers[q_index]:
                marks += 1
                print("Correct!")
            else:
                print("Incorrect!")
    showResult()
def showResult():
    print()
    if logged == True:
        print("Your result:", marks)
        with open("marksheet.txt","a") as file:
            file.write(f"{log_user,marks}")
        print("Wanna Try once again")
        main()
    else:
        print("--" * 5, "Please LogIn First", "--" * 5,"\n")
        main()

def main():
    op = input("""Choose an option 
                1. Register
                2. Login
                3. Attempt quiz a. DSA b. DBMS c. Python
                4. Show result
                5. Exit
                Enter your choice : """)
    if op == '1':
        register()
    elif op == '2':
        login()
    elif op == '3':
        attemptQuiz()
    elif op == '4':
        showResult()
    elif op == '5':
        exit()
    else:
        print("Wrong choice")
main()

