# Name: Alex Janssens
# Prog Purpose: This Magic 8-Ball code answers all your questions accurately, if you asked the right question.

import random
answer_8_ball = ("As I see it, yes", "Ask again later""Better not tell you now","Cannot predict now","Concentrate and ask again", "Don't count on 25""It is certain", "It is decidedly so","Most Likely","My reply is по","My sources say no","Outlook good","Outlook not so good", "Reply hazy try again","Signs point to yes","Very doubtful","Without a doubt","Yes""Yes definitely", "You may rely on it",)

def main():

    print("I am the Magic 8 BALL and can answer any yes or no question!")

    another_question =True
    while another_question:
        answer = random.choice(answer_8_ball)
        
        print("\nShake the Magic 8 Ball")
        print(".....and now.....")
        question = input("\nWhat is your YES or NO question")
        print("The Magic 8 Ball says: " + answer)

        askAgain = input("\nWould you like to ask me another question (Y or N)?: ")
        if askAgain.upper() =="N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions.")
    print("\nMagic 8 Ball OUT")

main()