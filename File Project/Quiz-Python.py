greetings = print('Hi Welcome To My Quiz Which I Made On Python. You Will be Assigned 5 Questions And If You Get Them All Correct, I Will Be Proud Of You.')
score = 0
name = (input('Before We get Started, Tell Me What Should I Call You.'))

print(f'Alright {name} lets get started :)')

Answer_1 = ('Mercury')
Question_1 = print('First Question is Which Planet Is The Closest To The Sun?')

Response_1 = input('Your Answer Is:')

if Response_1.lower() == Answer_1.lower():  
    print(f'Good Job {name} Your Answer Is Correct.')
    score += 1
   

else:
    print('Your Answer Is Incorrect:(.')
    


Question_2 =print('How Many Continents Are There In The World')
Response_2 = input('Your Answer Is:')
Answer_2 = ('7')

if Response_2.lower() == Answer_2.lower():
    print(f'Excellent answer {name} keep it up :)')
    score += 1
    

else:
    print('How did You Get That Wrong, We Learned That In Preschool Lmao.')
   

Question_3 = print('How many bones are there in the human body?')
Response_3 = input('Your Answer Is:')
Answer_3 = ('206')

if Response_3 == Answer_3:
    print(f'Excellent Work {name} only two more to go:)')
    score += 1
    

else:
    print('Wrong answer hopefully you do better in the next one.')
   


Question_4 = print('Who was the first man to land on the moon?')
Response_4 = input('Your Answer Is:')
Answer_4 = ('Neil Armstrong')

if Response_4.lower() == Answer_4.lower():
    print(f'Good job {name} your answer is flawless.')
    score +=1

else:
    print('Your answer is completely erroneous hopefully you do better next time.')


Question_5 = print('How many zeros are there in a billion?')
Response_5 = input('Your Answer Is:')
Answer_5 = ('9')

if Response_5 == Answer_5:
    print(f'Good job {name} looks like you have a billion iq too(that was cringe im sorry).')
    score +=1

else:
    print('Your answer is sadly incorrect.')


if score == 5:
    print(f'{name} You have scored {score} out of 5')
    print(f'I am Proud Of You {name} And You Have Made Me Proud.')

elif score < 5:
    print(f'You have scored {score} out of 5')

print('Thanks For Attempting My Python Quiz. I Hope You Enjoyed:)')
          

    





    


    



    






