questions = ('What is your best programming language',
             'Which of the following is true about javascript',
             'What is your fav hobby',
             'Which is your easiest programming language',
             'Which is the worst programming language')
options = (('A. python','B. java','C. c#','D. javascript'),
           ('A. difficult','B. easy to learn','C. hard syntax','D. easy'),
           ('A. eating','B. sleeping','C. coding','D. playing games'),
           ('A. python','B. html and css','C. javascript','D. java'),
           ('A. java','B. c','C. python','D. kotlin')) #we are using tuples because they are inchangebale
answers = ('A','B','C','D')
guesses = [] # cause we have to list our answers in a list format
score = 0  # our score varibale
question_number = 0 # keep track of our question number
  
for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
      
    guess = input('Enter option(A,B,C,D): ') 
    guesses.append(guess) 
    if guess == answers[question_number]:
        score += 1
        print('Correct')
    else:
     print('Incorrect')
     print(f'{answers[question_number]} is the correct answer')

question_number += 1   

print('🚀🚀 Results 🚀🚀🚀 ')

for guess in guesses:
   print(guess, end='')
print()

score = int(score / len(questions) * 100)
print(f'Your final score is {score}%') #score is converted to percentage
