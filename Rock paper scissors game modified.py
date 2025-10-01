#Rock paper scissors game modified
import random
print("Welcome to Rock Paper Scissors.")
rock = r'''
    _______
---'   ____)
      (______)
      (_______)
      (______)
---.__(___)
'''

paper = r'''
     _______
---'    _____)______
           _________)
          __________)
         __________)
---.__________)
'''

scissors = r'''
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
''' 
rock_1=rps_art = r'''   
                         ___ 
                         | |  
           _ __ ___   ___| | __
        | /__/ _ \ / __| |/ /
        | | | (_) | (__|   < 
        |_|  \___/ \___|_|\_\        _ __   __ _ _ __   ___ _ __ 
                                   | '_ \ / _` | '_ \ / _ \ '__|
                                   | |_) | (_| | |_) |  __/ |   
                                   | .__/ \__,_| .__/ \___|_|   
                                   | |         | |              
                                   |_|         |_|             
                                                              _                        
                                                             (_)                       
                                                     ___  ___ _ ___ ___  ___  _ __ ___ 
                                                    / __|/ __| / __/ __|/ _ \| '__/ __|
                                                    \__ \ (__| \__ \__ \ (_) | |  \__ \
                                                    |___/\___|_|___/___/\___/|_|  |___/ 


'''
 
print(rock_1)
input_user=input("Enter your choice: (Rock/Paper/Scissors)")
if input_user.lower() == 'rock':
    print("Your choice: rock")
    print(rock)
elif input_user.lower() == 'paper':
    print("Your choice: paper")
    print(paper)    
elif input_user.lower() == 'scissors':
    print("Your choice: scissors")
    print(scissors)
M=random.randint(1,3)
if M==1:
    print("opponents  choice: rock")
    print(rock)
elif M==2:
    print("opponents  choice: paper")
    print(paper)
elif M==3:
    print("opponents  choice: scissors")
    print(scissors)       
if input_user.lower()=='rock' and M==1:
    print("Tie sorry")
elif input_user.lower()=='rock' and M==3:
    print("You Win")    
elif input_user.lower()=='rock' and M==2:
    print("Opponet wins")
elif input_user.lower()=='paper' and M==2:
    print("Tie sorry")
elif input_user.lower()=='paper' and M==1:
    print("You Win")    
elif input_user.lower()=='paper' and M==3:
    print("Opponet wins")
elif input_user.lower()=='scissor' and M==3:
    print("Tie. Try again.")
elif input_user.lower()=='scissor' and M==2:
    print("You Win")    
elif input_user.lower()=='scissor' and M==1:
    print("Opponet wins")        

