#Python Quiz game

questions = ("Who is the first women president of India",
             "Who painted the Mona Lisa?",
             "Which organ in the human body purifies blood?",
             "What is the currency of Japan?",
             "What is the chemical symbol for gold?")

options = (("A. Pratibha Patil", "B.Indira Gandhi", "C.Sarojini Naidu", "D.Droupadi Murmu"),
           ("A. Vincent van Gogh", "B.Pablo Picasso", "C.Michelangelo", "D.Leonardo da Vinci"),
           ("A.Heart", "B.Liver", "C.Kidney", "D.Lungs"),
           ("A.Yuan", "B.Yen", "C.Won", "D.Ringgit"),
           ("A.Ag", "B.Au", "C.Gd", "D.Go"))

answers = ("A", "D", "C", "B","B") #Correct answers
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess= input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1 
    
print("-------------------------------------------------")
print("                    RESULTS                      ")
print("-------------------------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")
