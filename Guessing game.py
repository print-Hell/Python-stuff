


import random
secret_number = (random.randint(0,10))
count = 0


greetings = print(f'Hey Welcome To My Guessing Game Which I Made On Python. You Will Have 3 Guesses And Each Time You Guess I Will Tell You If You Are Close To The Number Or Not.')
print('The secret numbers range is from 1-10')

First_guess =int(input('Your first guess is....'))

if secret_number == First_guess :
    print(f'Outstanding luck your guess was spot on ')
    print('Thanks for playing')
    quit()
    

elif First_guess < secret_number:
    print('Your number is too low')
    count +=1

elif First_guess > secret_number:
    print('Your number is too high')
    count +=1

Second_guess =int(input('Your second guess is....'))

if secret_number == Second_guess:
    print(f'Good job your guess was spot on ')
    print('Thanks for playing')
    quit()

elif Second_guess < secret_number:
    print('Your number is too low')
    count +=1

elif Second_guess > secret_number:
    print('Your number is too high')
    count +=1

Third_guess =int(input('Your last guess is....'))

if secret_number == Third_guess:
    print(f'Good job your guess was spot on ')
    print('Thanks for playing')
    quit()

elif Third_guess < secret_number:
    print('Your number is too low')
    count +=1

elif Third_guess > secret_number:
    print('Your number is too high')
    count +=1

if count == 3:
    print('You have run out of guesses :(. Good luck next time.')
    print(f'Btw the number was {secret_number} dummy! ')
    quit()
    




    
    




    
    

