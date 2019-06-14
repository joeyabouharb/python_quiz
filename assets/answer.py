def get_question(number):
  if(number == 1):
    return '''this is question 1
 1) option 1
 2) option 2
 3) option 3
 4) option 4
    '''
  elif(number == 2):
    return '''this is question 1
 1) option 1
 2) option 2
 3) option 3
 4) option 4
    
'''
  elif(number == 3):
    return '''this is question 1
 1) option 1
 2) option 2
 3) option 3
 4) option 4
    '''
  elif(number == 4):
def check_answer(number, ans):
  if(number == 1):
    if(ans == 2):
      return True
    else:
      return False
  else:
    return False

def get_current_prize(wins):
  pass

def quiz_time():
  print('who wants to be a millionaire! ')
  print('first question...')
  total_questions = 10

  for q in range(1, total_questions):
    wins = 0
    print(q)
    question = get_question(q)
    print(question)
    _input = input('Your Answer: ')
    if (check_answer(q, _input) == True):
      print('correct')
      wins += 1
      get_current_prize(wins)
    else:
      print('incorrect')
    
quiz_time()