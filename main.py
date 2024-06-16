#variables, control flow statements, and loops
#Name
ship=0
life=1
rock=0
alone=0
doctor=0
localisation=0
print("""\nCaptain: Hello adventurer, your crue's captain's speaking. We've just made it to planet Pluto.
         We are now ready to lunch your ship. Please remember; your mission is to note as much infomations as possible
         Do not touch anythiing. The scientific crue will take car of that.
         Stay safe out there.\n""") #Isolated, Lake Mercry,Pluto

print("""Your ship comes off the main rocket and you are propuled to the ground of the planet Pluto.

While aproaching the surface, enter your name: """)

while True:
        yourname=str(input(" "))
        print(f"""\nAI voice: Welcome aboard {yourname}! I'll be guiding you throught your whole journey.
          Let's start by checking your speed.\n""")
        break

#Q1

print("""Though your speed is correct, your desire to explore the planet is too strong.
Do you increase the speed?
1. Yes
2. No\n""")

while True:
        choice=int(input())
        if (choice==1):
                print("""AI voice: You've just increased your speed. You are now going too fast.
          Because you've just started, I'll handle the landing for you.\n""")
                break
        elif(choice==2):
                break
        else:
                print(f"{yourname}, please enter a valid number: ")

#Q2

print("""You've successfuly landed on Pluto. You are now standing on the surface of the planet. The ground is covered with what seems to be ice and snow.
The sky is dark and the stars are shining. You barely see the sun.
Your crewmates started to explore the area.
Do you wish to follow them?
1. Yes
2. No\n""")

while True:
        choice=int(input())
        if (choice==1):
                alone=0
                print("""You decide to follow your mates. The scientific crew. They start collecting iced rocks and placing them into bags.\n""")
                break
        elif(choice==2):
                alone=1
                print("""You are now alone.\n
AI voice: No you're not! I'll be guiding you throught your whole journey.
          Try to focus on your mission and collect as much data as you can.\n""")
                break
        else:
                print(f"{yourname}, please enter a valid number: ")

#Q3

if alone==1:
        print("""You are now walking on the surface of Pluto. You see a strange object in the distance.
Do you wish to take it?
1. Yes
2. No\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        rock=1
                        print("""You decide to pick the rock. It feels sticky over your gloves but pretty hard and heavy.\n
AI voice: Please do not come into contact with elements in this environment.
          Focus on your mission, take note of what you see in your report and collect as much data as you can.\n""")
                        break
                elif(choice==2):
                        rock=0
                        print("""You turn on your electronic device and start tying.\n"Purple shiny rock, covered with curious white crystals.\nWas covered at first with snow"\nThose informations will certanly be useful for the scientific crew.\n""")
                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")
elif alone==0:
        print("""Your mates just discovered a strange object in the distance. When they pick up the rock, it felt sticky over their gloves but pretty hard and heavy.\nThey tell you to take note of it in your report.\n
You turn on your electronic device and start tying.\n"Purple shiny rock, covered with curious white crystals.\nWas covered at first with snow"\nThose informations will certanly be useful for the scientific crew.\n""")

#Q4

print(f"""\nCaptain: Crew Captain speaking. We've just located a lake near your position. The scientific crew is expected heading there to collect samples. Adventurer {yourname}, how's your mission going?""")

if alone==0:
        print("""\n1. "Good captain! I'm doing great. Got some interesting data until now."
2. Let a team member answer for you.\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        print("""\nCaptain: Good to hear that. Keep up the work. We'll be waiting for you at the ship in an hour for oxygen change.\n""")
                        break
                elif(choice==2):
                        print("""\nDr.Zapletal: We are doing great so far. The scientific crew collected some interessing data for research.\n
Captain: Thank you Dr.Zapleatal. Don't forget to change your oxygen. The weather conditions here are risky.\n
Dr.Zapletal: Understood.\n
The doctor will remember you for that.\n""")
                        doctor=1
                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")
elif alone==1:
        print("""\n1. "Good Captain! Got some interesting data until now."
2. "Bad Captain. I've lost the location of my team mates."\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        localisation=0
                        print("""\nCaptain: Good to hear that. Keep up the work.\n""")
                        break
                elif(choice==2):
                        localisation=1
                        print("""\nCaptain: I'll send you their location. Please pay more attention next time.\n""")
                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")

#Q5

print(f"""AI: {yourname}, your oxygen level is low. It is recommanded to head back to the ship. The scientific crew will take care of the lake.
Do you wish to head back?""")
if alone==0:
        print("""1. Head back to ship
2. Follow scientific crew\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        if rock==1:
                                print("""You decide to head back to the ship. You remember you've pick the rock up. As you penetrate in the ship, the rock starts to whistle and some smoke start comming from your pocket\nDesesperatee, as you try to throw it away, the rock sticks to your astronauts glove. Unfortunatly, due to low pressure in the cabin of your ship, the rock explodes and you die.\n
You've failed your mission.\n
Implosion Ending (2/5)\n""")
                                life=0
                                break
                        elif rock==0:
                                print("""You decide to head back to the ship. Since you feel kind of dizzy due to Pluto's pressure, you decide to stay in the ship and write your repport until the scientific crue gets back.\n""")
                                ship=1
                                break
                        break
                elif(choice==2):
                        print("""You decide to follow the scientific crew. Even if your oxygen level is low, you are determined to finish your mission.\nHowever, you quickly run out of oxygen and become too tired to follow your mates.\nYou died asphyxiated.\n
You've failed your mission.\n
Asphyxiated Ending (4/5)\n""")

                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")
elif alone==1 and localisation==1:
        print("""1. Head back to ship
2. Follow scientific crew\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        if rock==1:
                                print("""You decide to head back to the ship. You remember you've pick the rock up. As you penetrate in the ship, the rock starts to whistle and some smoke start comming from your pocket\nDesesperatee, as you try to throw it away, the rock sticks to your astronauts glove. Unfortunatly, due to low pressure in the cabin of your ship, the rock explodes and you die.\n
You've failed your mission.\n
Implosion Ending (2/5)\n""")
                                life=0
                        break
                elif(choice==2):
                        print("""You decide to follow the scientific crew. Even if your oxygen level is low, you are determined to finish your mission.\nHowever, you quickly run out of oxygen and become too tired to follow your mates.\nYou died asphyxiated.\n
You've failed your mission.\n
Asphyxiated Ending (4/5)\n""")
                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")
elif alone==1 and localisation==0:
        print("""1. Head back to ship
2. Continue exploring\n""")
        while True:
                choice=int(input())
                if (choice==1):
                        if rock==1:
                                print("""You decide to head back to the ship. You remember you've pick the rock up. As you penetrate in the ship, the rock starts to whistle and some smoke start comming from your pocket\nDesesperatee, as you try to throw it away, the rock sticks to your astronauts glove. Unfortunatly, due to low pressure in the cabin of your ship, the rock explodes and you die.\n
You've failed your mission.\n
Implosion Ending (2/5)\n""")
                                life=0
                                break
                        else:
                                print("""You decide to head back to the ship. Since you feel kind of dizzy due to Pluto's pressure, you decide to stay in the ship and write your repport until the scientific crue gets back.\n""")
                                ship=1
                                break
                elif(choice==2):
                        print("""You decide to continue exploring. Even if your oxygen level is low, you are determined to finish your mission.\nHowever, you quickly run out of oxygen and become too tired to continue.\nYou died alone.\n
You've failed your mission.\n
Alone on Pluto Ending (3/5)\n""")
                        life=0
                        break
                else:
                        print(f"{yourname}, please enter a valid number: ")

#Bonus

if life==1 and ship==1 and doctor==1 and alone==0:
        print("""As you hear someone entering the ship, you turn around and see the doctor. He's holding a bag full of iced rocks.\n
Dr.Zapletal: Those rocks explose at low pressure. Like that, I'll make sure you'll never be able to take the captain's place. See you on the other side, 'mate!\n
The doctor was your rival since you've began as an astronaut. Before escaping the ship, he throws the steaming bag at you. You die as soon as the rocks explode.\n
You've failed your mission.\n
Rivals Ending (5/5)\n""")
elif life==1 and ship==1 and doctor==0:
        print("""The scientific crew came back. They'll be able to analyze the data you've collected.\n
You've achieved successfuly your mission.\n
Best Ending (1/5)\n""")
