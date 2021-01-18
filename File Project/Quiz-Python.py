greetings = ('Hi Welcome To My Quiz Which I Made On Python. You Will be Assigned 5 Questions And If You Get Them All Correct, I Will Be Proud Of You.')
print(greetings.title())
score = 0
name = (input('Before We get Started, Tell Me What I should Call You.'))
print(name.title())

print(f'Alright {name} Lets Get Started :)')

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
   

Question_3 = ('How many bones are there in the human body?')
print(Question_3.title())

Response_3 = input('Your Answer Is:')
Answer_3 = ('206')

if Response_3 == Answer_3:
    print(f'Excellent Work {name} Only Two More To Go:)')
    score += 1
    

else:
Wrong_answer = ('Wrong answer hopefully you do better in the next one.')
print(Wrong_answer.title())
   


Question_4 = ('Who was the first man to land on the moon?')
print(Question_4.title())
Response_4 = input('Your Answer Is:')
Answer_4 = ('Neil Armstrong')

if Response_4.lower() == Answer_4.lower():
    print(f'Good job {name} Your Answer Is Flawless.')
    score +=1

else:
 Wrong_answer2 = ('Your answer is completely erroneous hopefully you do better next time.')
 print(Wrong_answer2.title())


Question_5 = print('How many zeros are there in a billion?')
print = (Question_5.title())
Response_5 = input('Your Answer Is:')
Answer_5 = ('9')

if Response_5 == Answer_5:
Feed_back = (f'Good job {name} looks like you have a billion iq too(that was cringe im sorry).')
print(Feed_back.title())
 score +=1

else:
    print('Your answer Is Sadly Incorrect.')


if score == 5:
    print(f'{name} You Have Scored {score} Out Of 5')
    print(f'I Am Proud Of You {name} And You Have Made Me Proud.')

elif score < 5:
    print(f'You Have Scored {score} Out Of 5')

print('Thanks For Attempting My Python Quiz. I Hope You Enjoyed:)')
          

    





    


    



    






