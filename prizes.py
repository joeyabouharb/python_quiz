def congratulations():
  return ("\U0001F4E3 \U0001F4E3 \U0001F4E3 \U0001F4E3 \U0001F4E3 \U0001F4E3 \n"
  'Congratulations you won $1000000! \n'
  '\U0001F389 \U0001F389 \U0001F389 \U0001F389 \U0001F389 \U0001F389\n'
  "\U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600\n"
  )

def contestant_prize(wins):
  msg = {
    0: lambda:'$0',
    1: lambda:'$200',
    2: lambda:'$500',
    3: lambda:'$1000',
    4: lambda:'$5000',
    5: lambda:'$20000',
    6: lambda:'$25000',
    7: lambda:'$50000',
    8: lambda:'$100000',
    9: lambda:'$250000',
    10: congratulations
  }
  result = msg.get(wins, '0')
  return result()
