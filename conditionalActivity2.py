def clothingLogic():
    print("great, time to get dressed!")

user_welcome = input('Welcome Princess Zion, please enter your password!')

if user_welcome == 'arianagrande505':
    print('Time to choose your outfit!')

if user_welcome == 'dingdog':
    print('Thats Incorrect Please try again') 

if user_welcome == 'ringring':
    print('Thats Incorrect, Please Try again')   
    
    
user_mood= input('How are you feeling today!: ')

while user_mood == 'good':
    print('thats Wonderful!')
    break
    clothingLogic()

print('Awwe so sorry!  ') 

user_mood= input('what is your mood: ')

while user_mood == 'sad':
    print('thats not good')
    user_mood= input('what is your mood:')

print('Awwe what happened?') 

while user_mood != 'happy':
    print('wow')
user_mood = input('what is your mood?')

print('Thats wonderful  ')
user_clothes= input('Please choose your clothes')

if user_clothes == 'dress please':
    print('thats a wonderful choice!')

if user_clothes == 'shirt please':
    print('great choice!') 

if user_clothes == 'pants please!':
    print('nice choice')    
    
