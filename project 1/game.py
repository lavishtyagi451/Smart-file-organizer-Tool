name = input("enter your name   ")

print("hello ", name,"lets start the game")


answer = input("SCENARIO : \n You are traveling alone through a desert. After walking for hours, you reach a dead end between two paths.\n QUESTION:\n Which direction do you choose?\n A)left\n B)right").lower()


if answer == "left":
    s1 = input("SCENARIO:\n You take the left path. After some distance, you see a wide river blocking your way. The water is flowing fast.\n QUESTION:\n What do you do?\nOPTIONS:\nA)swim\nB)look for bridge").lower()

#SCENARIO S3 – SWIM THE RIVER
    if s1 == "swim":
        answer = input("SCENARIO:\nYou enter the river. The current is extremely strong. \nQUESTION:\nHow do you handle the current?\nOPTIONS:\nA)fight the current\nB)go with flow").lower()
        if answer == "fight the current":
            print("game over")
        elif answer == "go with flow":
            print("game over")
    elif answer == "look for bridge":
        print("SCENARIO:\nYou walk along the river and find a broken wooden bridge.\nQUESTION:\nWhat do you do?")
        question = input("OPTIONS:\n A)cross bridge\n B)turn back")

        if question == "cross bridge":
            print("congrats ",name, 'you won')
        else:
            print("winner never turn back:\n sorry ",name,"you loose")



elif answer == "right":
    s2 = input("SCENARIO:\nYou take the right path. You find an abandoned jeep half-buried in sand.\nQUESTION:\nWhat do you do?\nOPTIONS:\nA)search jeep\nB)ignore and move on").lower()

else:
    print("not a valid answer ")