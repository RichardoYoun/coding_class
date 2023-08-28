import random

a = random.randrange(1,4)
compAnswer = ""

if (a == 1):
    compAnswer = "바위"
    
if (a == 2):
    compAnswer = "가위"

if (a == 3):
    compAnswer = "보"




userInput = input("가위, 바위, 보 중에 아무거나 내주세요")

if (userInput == "가위"):
    if (compAnswer == "가위"):
        print("비겼다")
    if (compAnswer == "바위"):
        print("졌다")
    if (compAnswer == "보"):
        print("이겼다")

if (userInput == "보"):
    if (compAnswer == "보"):
        print("비겼다")
    if (compAnswer == "바위"):
        print("이겼다")
    if (compAnswer == "가위"):
        print("졌다")

if (userInput == "바위"):
    if (compAnswer == "가위"):
        print("이겼다")
    if (compAnswer == "바위"):
        print("비겼다")
    if (compAnswer == "보"):
        print("젔다")
        
print("컴퓨터는"+ compAnswer  +"를 냈습니다")
