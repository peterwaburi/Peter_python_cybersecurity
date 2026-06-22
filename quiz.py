quiz_show =[
    {
        "questions" : "Which is your gender?",
        "option" :["A.male","B.female","C.trans","D.it depends"],
        "answer" : "A"
    },

    {
       "questions" : "How do you write the extension of a file",
       "option": ["A.in small caps", "B.in capital letters","C.mixed ", "D.neither"],
       "answer" : "A"
    },

    {
        "questions" : "Who is the president of kenya?",  
        "option" : ["A.Ruto", "B.Raila", "C.Museveni", "D.Kibaki"],
        "answer": "A"
    },

    {
        "questions" : "Which year is this?", 
        "option" : ["A.2026", "B.2025", "C.2024","D.2013"], 
        "answer" :"A"
    },
    
    {
        "questions" :"which is the capital city of Kenya?",
        "option" : ["A.Nairobi", "B.Nakuru", "C.Turkana","D.Mombasa"],
        "answer" : "A"
    },
    
    {
        "questions" : "when did kenya attain indipendence?",
        "option" : ["A.1962", "B.1961", "C.1900","D.2007"],
        "answer" : "A",
    }
]

score = 0
print("----lets do a simple quiz----")

for q in quiz_show:
    print(q["questions"])

    for option in q["option"]:
        print(option)


    answer =input("Enter your answer(A/B/C/D):").upper

    if answer == q["answer"]:
        print("correct\n")
        score +=1
    else:
        print(f"Wrong , the correct answer is {q['answer']}\n")

print("Quiz finished wel done.")
print(f"-----Your final score is {score}/{len(q ["questions"])}-----")
