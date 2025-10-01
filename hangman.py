#hangman project
import random
print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                   ''')
words = [
    
    "elephant", "giraffe", "kangaroo", "alligator", "penguin", "dolphin",
    "cheetah", "rhinoceros", "buffalo", "crocodile", "ostrich", "hippopotamus",
    "peacock", "camel", "squirrel", "tiger", "lion", "zebra", "leopard",
    "gorilla", "monkey", "rabbit", "donkey", "parrot", "eagle",

    
    "banana", "strawberry", "pineapple", "watermelon", "pomegranate", "mango",
    "papaya", "orange", "blueberry", "guava", "apple", "pear", "grapes",
    "plum", "peach", "apricot", "cherry", "kiwi", "lychee", "fig",

    
    "canada", "brazil", "germany", "france", "argentina", "australia",
    "japan", "egypt", "mexico", "spain", "italy", "india", "china",
    "sweden", "norway", "finland", "denmark", "portugal", "chile", "turkey",

    
    "purple", "turquoise", "crimson", "beige", "emerald", "maroon",
    "navy", "gold", "silver", "indigo", "violet", "black", "white",
    "yellow", "brown",

    
    "bicycle", "telephone", "backpack", "umbrella", "scissors", "mirror",
    "pillow", "guitar", "camera", "notebook", "pencil", "chair", "table",
    "window", "ladder", "spoon", "bottle", "basket", "television", "remote",
    "helmet", "wallet", "shoe", "blanket", "balloon",

    
    "python", "javascript", "computer", "keyboard", "laptop", "algorithm",
    "variable", "syntax", "function", "debugging", "database", "network",
    "binary", "boolean", "software", "hardware", "internet", "program",
    "compiler", "developer",

    
    "doctor", "engineer", "teacher", "farmer", "pilot", "nurse", "lawyer",
    "scientist", "artist", "writer", "chef", "singer", "dancer", "driver", "actor",

    
    "wizard", "pirate", "castle", "rocket", "dragon", "unicorn", "galaxy",
    "planet", "zombie", "treasure", "magic", "witch", "sword", "shield",
    "giant", "ghost", "alien", "spaceship", "monster", "knight",
    "robot", "dungeon", "adventure", "quest", "legend",

    
    "run", "jump", "swim", "climb", "dance", "sing", "write", "read",
    "listen", "speak", "drive", "cook", "sleep", "study", "laugh",
    "cry", "play", "watch", "build", "travel",

    
    "happy", "sad", "angry", "funny", "silly", "crazy", "beautiful",
    "ugly", "tall", "short", "brave", "shy", "kind", "mean", "smart",
    "lazy", "strong", "weak", "rich", "poor"
]
stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

b=random.choice(words)
#print(b)
arr1=list(b)
arr=[]
arr2=[]
print("Guess the word: ",end="")
for i in range(len(b)):
    print('_',end=" ")
    arr.append("_")
print()      
count=6
print()
while count>=0:
    if count==0:
        print(f"The word was {b},YOU LOST!")
        break
    letter=input("Guess the letter: ").lower()
    if letter in arr2:
        print("You already guessed that!")
        continue
    arr2.append(letter)
    for i in range(len(b)):
        if arr1[i]==letter:
            arr[i]=letter
            continue
    for i in range(len(b)):
        print(arr[i],end=" ")
    word="".join(arr)
    if word==b:
        print("YOU WON!!")
        break
    
    if letter not in b:
        count-=1
        print()
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(stages[count])
    print()
    print(f"****************************{count}/6 LIVES LEFT****************************")    

