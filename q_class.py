class Question:
  def __init__(self, question, options, correctAns ):
    self.question = question
    self.options = options
    self.correctAns = correctAns

  def checkAnswer(self, ans):
    if(self.correctAns == ans):
      return True
    else:
      return False

  def askQuestion(self):
    f_options = ''
    for option in self.options:
      f_options += f'{option} \n'
    return f'{self.question} \n{f_options}'
