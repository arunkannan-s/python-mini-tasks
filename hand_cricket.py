import random

def cricket(team):
    runs = 0
    balls = 1
    numbers = [1,2,3,4,5,6]
    if team == user:
        while True:
            print(f"-----Ball no.{balls}-----")
            bowling = random.choice(numbers)
            batting = int(input("Hit any num: "))
            print(f"{comp} bowled {bowling}")
            if batting == bowling:
                print(f"Ohhh {team} is OUT...! \n{team} Score: {runs}")
                print("--------------")
                if comp_score > 0:
                    print("^^^^^^---------^^^^^^^")
                    print(f"{comp} won the Match by {comp_score - runs} Runs..")
                return runs
                break
            else:
                runs += batting
                balls += 1
                print(f"Runs Till now: {runs}")   
                if comp_score > 0:
                    if runs > comp_score:
                        print("^^^^^^---------^^^^^^^")
                        print(f"{user} won the match!")
                        print(f"Score Board \n {comp} : {comp_score} \n {user}: {runs}")
                        break    
        
    else:
         while True:
             print(f"-----Ball no.{balls}-----")
             bowling = int(input("Throw the ball: "))
             batting = random.choice(numbers)
             print(f"{comp} hits -> {batting}")
             if bowling == batting:
                print(f"Ohhh {team} is OUT...! \n{team} Score: {runs}")
                print("---------------")
                if user_score > 0:
                    print("^^^^^^---------^^^^^^^")
                    print(f"{user} won the match by {user_score - runs} Runs")
                return runs
                break
             else:
                 runs += batting
                 balls += 1
                 print(f"Runs till now {runs}")
                 if user_score > 0:
                     if runs > user_score:
                        print("^^^^^^---------^^^^^^^")
                        print(f"{comp} won the Match!")
                        print(f"Score Board \n {user} : {user_score} \n {comp}: {runs}")
                        break

print("-------> Welcome to Hand Cricket <-------")
toss = ["head","tail"]
bat_bowl = ["bat","bowl"]
user = input("Enter your team name: ").title()
comp = "Computer"
user_score = 0
comp_score = 0
#----Toss
toss_choose = input(f"Hello {user}! Choose head/tail: ")
toss_result = random.choice(toss)
print(f"Toss is {toss_result}")
#----Choose bat or bowl
if toss_result == toss_choose:
    user_won_toss = input(f"{user} won toss, Choose bat/bowl: ")
    if user_won_toss == "bat":
        print(f"{user} choose to bat first.")
        user_score = cricket(user)
        print(f"Now {comp} Batting")
        comp_score = cricket(comp)
    else:
        print(f"{comp} choose to bat first.")
        comp_score = cricket(comp)
        print(f"Now {user} Batting")
        user_score = cricket(user)
else:
    comp_won_toss = random.choice(bat_bowl)
    print(f"Computer won toss & choose to {comp_won_toss}")
    if comp_won_toss == "bat":
        comp_score = cricket(comp)
        print(f"Now {user} Batting")
        user_score = cricket(user)
    else:
        user_score = cricket(user)
        print(f"Now {comp} Batting")
        comp_score = cricket(comp)