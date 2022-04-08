import numpy as np

# Put the starting conditions in place
def newstart():
  pastanswers = []
  answer = np.random.randint(1000,9999)
  solutions = [x for x in range(1000,9999)]
  return pastanswers, answer, solutions

# Compare a guess vs. the answer
def compare(guess, answer):
  listguess = [x for x in str(guess)]
  listanswer = [x for x in str(answer)]
  correct = 0
  wrongplace = 0
  # Count corrects
  for i in range(len(listguess)):
    if listguess[i] == listanswer[i]:
      correct += 1
      listguess[i] = 'x'
      listanswer[i] = 'y'
  # Count wrongplaces, and at the end, wrongs
  for i in range(len(listguess)):
    if listguess[i] in listanswer:
      wrongplace += 1
      listanswer[listanswer.index(listguess[i])] = 'y'
      listguess[i] = 'x'
    wrong = 4-correct-wrongplace
  return correct, wrongplace, wrong

# Set up the start
pastanswers, answer, solutions = newstart()

solve = True
print('This game has a solver built in. To turn it off, type _solveoff_. To turn it on again, type _solveon_.\n')
while True:
  guess = input('Enter a number between 1000 and 9999. Press r to get a new number, p to view previous guesses, q to quit.\n')
  if guess.isnumeric():
    guess = int(guess)
    if guess == answer:
      print('Congratulations, you guessed the answer!\nPlay again?')
      pastanswers, answer, solutions = newstart()
    elif 1000 <= guess <= 9999:
      correct, wrongplace, wrong = compare(guess, answer)
      print(f'Your guess had {correct} correct digits, {wrongplace} digits in the wrong place and {wrong} incorrect digits')
      pastanswers.append(f'Guess: {guess} - {correct} correct, {wrongplace} wrong places, {wrong} incorrect')
      # Solver starts here
      if solve:
        solutions = [x for x in solutions if (correct, wrongplace, wrong) == compare(x, guess)]        
        print(f"This number is a perfect fit: {np.random.choice(solutions)}")
      # Solver ends here
    else:
      print('Invalid input!')
  elif guess == 'r':
    pastanswers, answer, solutions = newstart()
  elif guess == 'p':
    p = "\n".join(pastanswers)
    print(p)
  elif guess == 'q':
    print('Thanks for playing!')
    break
  elif guess == 'answer':
    print(answer)
  elif guess == 'solveoff':
    solve = False
  elif guess == 'solveon':
    solve = True
  else: 
    print('Invalid input!')

