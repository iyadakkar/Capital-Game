
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QHBoxLayout, QPushButton, QLabel
from random import *
app = QApplication([])
questions = [
    {'question':'What is the capital of France?',
     'options' :['Paris', 'Marseille', 'Lille', 'Nice'],
     'answer':'Paris'},
    {'question':'What is the capital of Morocco?',
     'options' :['Kenitra', 'Berkane', 'Rabat', 'Souk Lerbaa'],
     'answer':'Rabat'} ,
    {'question':'What is the capital of Italy?',
     'options' :['Milan', 'Rome', 'Torino', 'Napoli'],
     'answer':'Rome'},
     {'question':'What is the capital of Germany?',
     'options' :['Berlin', 'Munchen', 'Dortmund', 'Koln'],
     'answer':'Berlin'},
    {'question':'What is the capital of the United Kingdom?',
     'options' :['London', 'Manchester', 'Brighton', 'Newcastle'],
     'answer':'London'},
    {'question':'What is the capital of the United States of Anerica?',
     'options' :['Georgia', 'New York city', 'Washington DC', 'Austin'],
     'answer':'Washington DC'},

]
 
correctAnswer = 'Paris'

main_win = QWidget()
RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton(questions[0]['options'][3])
rbtn_2 = QRadioButton(questions[0]['options'][0])
rbtn_3 = QRadioButton(questions[0]['options'][1])
rbtn_4 = QRadioButton(questions[0]['options'][2])
answerbtn = QPushButton('Answer')
questionbtn = QPushButton('Next Question')
question = QLabel(questions[0]['question'])
question1   = QLabel("Easy")

# layouts
layouth1 = QHBoxLayout()   
layouth2 = QHBoxLayout() 
layoutv1 = QVBoxLayout()
mainlayout = QVBoxLayout()

# answer group component
layouth1.addWidget(rbtn_1)
layouth1.addWidget(rbtn_2)
layouth2.addWidget(rbtn_3)
layouth2.addWidget(rbtn_4)
layoutv1.addLayout(layouth1)
layoutv1.addLayout(layouth2)
RadioGroupBox.setLayout(layoutv1)

answerresult = QGroupBox('Test Result')
layout1 = QVBoxLayout()
answer = QLabel('Your answer is')
layout1.addWidget(answer, alignment=Qt.AlignCenter)
answerresult.setLayout(layout1)


# main window
main_win.setWindowTitle('Card Game')
mainlayout.addWidget(question1,alignment=Qt.AlignCenter)
mainlayout.addWidget(question,alignment=Qt.AlignCenter)
mainlayout.addWidget(RadioGroupBox,alignment=Qt.AlignCenter)
mainlayout.addWidget(answerresult)
mainlayout.addWidget(answerbtn,alignment=Qt.AlignCenter)
mainlayout.addWidget(questionbtn,alignment=Qt.AlignCenter)
main_win.setLayout(mainlayout)

question1.hide()
answerresult.hide()
questionbtn.hide()

answervalue = ""


def setAnswerValue():
    global answervalue
    if (rbtn_1.isChecked()):
        rbtn_1.setChecked(False)
        answervalue = rbtn_1.text()
        print(answervalue)
    if (rbtn_2.isChecked()):
        rbtn_2.setChecked(False)
        answervalue = rbtn_2.text()
        print(answervalue)
    if (rbtn_3.isChecked()):
        rbtn_3.setChecked(False)
        answervalue = rbtn_3.text()
        print(answervalue)
    if (rbtn_4.isChecked()):
        rbtn_4.setChecked(False)
        answervalue = rbtn_4.text()
        print(answervalue)
 

def checkAnswer():
    global answervalue, correctAnswer, score
    setAnswerValue()
    if answervalue == correctAnswer:
        answer.setText('Your answer is CORRECT')                                                                                                                                                                                                                                                                                                                                                                                 
    else :
        answer.setText('Your answer is WRONG')
    question1.show()
    answerresult.show()
    questionbtn.show()
    RadioGroupBox.hide()
    answerbtn.hide()
    question.hide()
answerbtn.clicked.connect(checkAnswer)

def get_random_question():
    global questions
    return choice(questions)

def setup_question(q):
    global questions, correctAnswer
    rbtn_2.setText(q['options'][0])
    rbtn_1.setText(q['options'][3])
    rbtn_3.setText(q['options'][1])
    rbtn_4.setText(q['options'][2])
    question.setText(q['question'])
    correctAnswer = q['answer']

def NextQuestion():
    setup_question(get_random_question())
    question1.hide()
    answerresult.hide()
    questionbtn.hide()
    RadioGroupBox.show()
    answerbtn.show()
    question.show()
questionbtn.clicked.connect(NextQuestion)



main_win.show()
app.exec_()

 
 
