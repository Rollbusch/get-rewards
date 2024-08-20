import pyautogui

def searchWord(sufix = '', attempts = 0):
  try:
    for attempt in range(attempts):
      pyautogui.press('super')
      pyautogui.write(generateWord(sufix, attempt), interval=0.15)
      pyautogui.press('enter')
  except:
    print('Error in searchWord')

def generateWord(sufix, index = 0):
  return f'{sufix}{index}'

def Start():
  try:
    attempts = None

    while True:
      attempts = pyautogui.prompt(text='Quantidade de tentativas:', title='getRewards' , default='0')
      if attempts == None or attempts.isnumeric():
        break
    if attempts != None and attempts.isnumeric():
      sufix = pyautogui.prompt(text='Sufixo da pesquisa (ex: asdasd):', title='getRewards' , default='')
      searchWord(sufix, int(attempts))
  except:
    print('Error in Start')

Start()