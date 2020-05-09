# https://youtu.be/rfscVS0vtbw?t=14258

from question import NewQuestion

question_prompts = [
    "\nWhat color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "\nWhat color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "\nWhat color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    NewQuestion(question_prompts[0], "a"),
    NewQuestion(question_prompts[1], "c"),
    NewQuestion(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\n\nYou got " + str(score) + "/" + str(len(questions)) + " questions right")

run_test(questions)
