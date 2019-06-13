import json 
import prizes

def set_question(question, options, answer):
  selected_question = dict()
  selected_question['question'] = question
  selected_question['options'] = options
  selected_question['answer'] = answer
  return selected_question

# define our variables
def load_questionaire():
  questionaire = []
  with open('questionaire.json') as json_file:
    data = json.load(json_file)
    for q in data['questions']:
      questionaire.append(set_question(q['question'], q['options'], q['answer']))
  return questionaire

def test_answer(correct_answer, answer):
    if(correct_answer == answer):
        return True
    else:
      return False

def ask_question(q):
  question= q['question']
  options = q['options']
  ops = ''
  for option in options:
    ops += f'{option}\n'
  return f'{question}\n{ops}' 

# app
def validate_input(inp):
  val = 0
  try:
    val = int(inp)
  except ValueError:
    val = validate_input(input("Not a real option! Try Again "))
  if(val < 1 or val > 4):
    val = validate_input(input("Not a real option! Try Again "))
  return val

def app():
  questionaire = load_questionaire()
  wins = 0
  print("Welcome to who wants to be a Millionaire! ")
  print("We will ask questions and input your answer as you see as numbers 1-4")

  for question in questionaire:
 
    print(f"\ncurrent wins: {wins}. \nYour prize: ")
    print(prizes.contestant_prize(wins))
    print("\n")
    print(ask_question(question))
    ans = validate_input(input("Select Your answer (1-4): "))
    result = test_answer(question['answer'], ans)

    if result == False:
      print("\nWrong Answer!")
    elif result == True:
      wins += 1
      print("\nCorrect!")

  print(f"final score: {wins} \nYour Prize")
  print(prizes.contestant_prize(wins))

app()