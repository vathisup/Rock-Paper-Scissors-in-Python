import random
level_1 = True
level_2 = True
hum_score = 0
bot_score = 0
int(hum_score)
int(bot_score)
welcome=input("Welcome to the Rock-Paper-Scissor game. Press Enter to continue.")

#1=rock, 2=paper, 

while(level_1):
    while(level_2):
        bot_choice=random.randint(1,3)
        int(bot_choice)
        print("Please make your move. 1=Rock, 2=Paper, 3=Scissor")
        user_choice=input("Your move: ")
        
        print(f"You chose {user_choice}, Bot Chose {bot_choice}")

        if(int(user_choice)==1):
            print(f'''You chose Rock.
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
            ''')
            if(int(bot_choice)==1):
                print(f'''Bot chose Rock.
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
                ''')
            elif(int(bot_choice)==2):
                print(f'''Bot chose Paper.
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
                ''')
            elif(int(bot_choice)==3):
                print(f''''Bot chose scissor.
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
                ''')
        elif(int(user_choice)==2):
            print(f'''You chose paper.
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
            ''')
            if(int(bot_choice)==1):
                print(f'''Bot chose Rock.
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
                ''')
            elif(int(bot_choice)==2):
                print(f'''Bot chose Paper.
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
                ''')
            elif(int(bot_choice)==3):
                print(f''''Bot chose scissor.
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
                ''')
        elif(int(user_choice)==3):
            print(f'''You chose scissor.
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
            ''')
            if(int(bot_choice)==1):
                print(f'''Bot chose Rock.
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
                ''')
            elif(int(bot_choice)==2):
                print(f'''Bot chose Paper.
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
                ''')
            elif(int(bot_choice)==3):
                print(f''''Bot chose scissor.
        _______
    ---'   ____)____
              ______)
           __________)
           (____)
    ---.__(___)
                ''')



            
        
        

        if(int(user_choice)==1 and int(bot_choice)==1):
            print("It is a draw.")
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==2 and int(bot_choice)==2):
            print("It is a draw.")
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==3 and int(bot_choice)==3):
            print("It is a draw.")
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==1 and int(bot_choice)==2):
            print(f"You lost.")
            bot_score=bot_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==1 and int(bot_choice)==3):
            print(f"You win!")
            hum_score=hum_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==2 and int(bot_choice)==3):
            print(f"You lost.")
            bot_score=bot_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==2 and int(bot_choice)==1):
            print(f"You win!")
            hum_score=hum_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==3 and int(bot_choice)==1):
            print(f"You lost.")
            bot_score=bot_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        elif(int(user_choice)==3 and int(bot_choice)==2):
            print(f"You win!")
            hum_score=hum_score+1
            print(f"You: {hum_score}, Bot: {bot_score}")

        if(int(hum_score)==3):
            print(f"You win this round.")
        elif(int(bot_score)==3):
            print(f"You lose this round.")

        if(int(hum_score)==3 or int(bot_score)==3):
            level_2=False
            
        
            
        
    conti=input(f"Do you want to continue? (Y/N): ")
    if(conti=="N" or conti=="n"):
        print(f"Exiting the game.")
        level_1=False
    elif(conti=="Y" or conti=="y"):
        level_2=True
        print(f"Restarting the game...")
        bot_score=bot_score-bot_score
        hum_score=hum_score-hum_score
    else:
        print("invalid input")


    

    