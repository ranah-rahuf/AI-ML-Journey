# Classes & Objects:

from Student import student

student1=student("John","Computer Science",3.1,False)
student2=student("Alice","Mathematics",3.8,False)
print(student1.name)
print(student2.gpa)

#class function & Object function:

print(student1.on_honor_roll())
print(student2.on_honor_roll())


# Building a multiple choice quiz:
from question import question

question_prompts=[
    "what is the color of apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what is the color of banana?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
    "what is the color of sky?\n(a) Blue\n(b) Green\n(c) Orange\n\n"
]

questions=[
    question(question_prompts[0],"a"),
    question(question_prompts[1],"b"),
    question(question_prompts[2],"a")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("you got "+str(score)+"/"+str(len(questions))+" correct")

run_test(questions)

# Inheritance:

from chef import chef
from ChineseChef import ChineseChef

myChef=chef()
myChef.make_chicken()
myChef.make_special_dish()
myChef.make_salad()

myChineseChef=ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()


