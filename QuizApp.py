import json
# import getpass
import random

def addQuestion():
    if len(user)== 0:
        print("You have not logged in.\n")

    elif len(user) == 2:
        if user[1] == "ADMIN":
            print("<<<<< Add Questions >>>>>")
            ques = input("Enter the question\n")
            opt = []
            print("Enter the options with A., B., C. ,D. in initials(starting) of each options\n")
            for _ in range(4):
                opt.append(input())
            ans = input("enter the answer \n")
            with open("quizquestest.json", 'r+') as adder:
                add_question = json.load(adder)
                dic = {"question": ques, "options": opt, "answer": ans}
                add_question.append(dic)
                adder.seek(0)
                json.dump(add_question, adder)
                adder.truncate()
                print("Questions added sucessfully")
        else:
            print("You are not 'ADMIN' \n")



user = []
# login

def login():
    username = input("Enter your user name \n")
    password = input("Enter your password \n")

    with open('login_info.json', 'r') as login_checker:
        users = json.load(login_checker)

        if username not in users.keys():
            print("Invalid username. Please try again")

        elif username in users.keys():
            if users[username][0] !=password:
                print("Invalid Password")
            elif users[username][0] == password:
                print(f"Logged In Successfully as {users[username][1]}")
                user.append(username)
                user.append(users[username][1])


def play_game():
    print("<<<Welcome to my first quiz game>>>")
    print("You will be attempting 5 questions")

    score = 0
    with open("quizquestest.json", 'r+') as play:
        game = json.load(play)
        for i in range(5):
            no_of_questions = len(game)
            ch = random.randint(0, no_of_questions -1)
            print(f"\nQ{i+1} :", game[ch]["question"],"\n")
            for opt in game[ch]["options"]:
                print(opt)
            ans = input("\nEnter your answer\n")
            if game[ch]["answer"][0] == ans[0].upper():
                print("Your answer is correct\n")
                score += 1
            else:
                print("Your answer is incorrect\n")
                del[ch]
        print("<<<<<<<<<<Game Over>>>>>>>>>>")
        print(f" Your final score : {score}\n")


def logout():
    global user
    if len(user)== 0:
        print("You are already logged out \n")
    else:
        user = []
        print("You have sucessfully logged out \n")


# signup

def signup():
    username = input("Enter username\n")
    password = input("Enter password:\n")

    # password = input("Enter password\n")
    with open('login_info.json', 'r+') as f:
        users = json.load(f)
        if username in users.keys():
            print("Username already exists")
        else:
            users[username] = [password, "Player"]
            f.seek(0)
            json.dump(users, f)
            f.truncate()
            print("Sucessfully Created")



if __name__ == '__main__':
    choice = 1
    while choice !=6:
        print("\n<<<<<<< Quiz Menu >>>>>>>")
        print(" 1) Play\n",
              "2) Login\n",
              "3) Logout\n",
              "4) Sign up\n",
              "5) Add Question\n",
              "6) Exit\n")
        choice = int(input("Enter your choice\n"))
        if choice == 1:
            play_game()
        elif choice == 2:
            login()
        elif choice == 3:
            logout()
        elif choice == 4:
            signup()
        elif choice == 5:
            addQuestion()
        elif choice == 6:
            break
        else:
            print("Worng input. Enter correct option")


