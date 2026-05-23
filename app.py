from auth import register, login
from ai_questions import generate_questions
from save_score import save_score

print("\n===== AI QUIZ GENERATOR =====")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose Option: ").strip()
    while choice == "":
        print("Please enter an option!")
        choice = input("Choose Option: ").strip()
    if choice == "1":
        success, username = register()
        if success:
            print("\nRegistration Successful!")
            print(f"Welcome, {username}!")
            break
    elif choice == "2":
        attempts = 3
        while attempts > 0:
            username = login()
            if username is not None:
                break
            attempts -= 1
            print(f"\nRemaining Attempts: {attempts}")
        if attempts == 0:
            print("\nToo Many Failed Attempts!\n")
            exit()
        if username is not None:
            break 
    elif choice == "3":
        print("Thank You for using AI Quiz Generator!",end="\n")
        exit()

print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty_choice = input("Enter Choice: ")
while difficulty_choice not in ["1", "2", "3"]:
    print("Invalid choice!")
    difficulty_choice = input("Enter Choice: ").strip()
if difficulty_choice == "1":
    difficulty = "Easy"
elif difficulty_choice == "2":
    difficulty = "Medium"
else:
    difficulty = "Hard"
print("\nGenerating AI Questions...")

questions = generate_questions(difficulty)
if len(questions) < 5:
    print("\nCould not generate quiz questions!")
    exit()

score = 0
wrong = 0

for index, q in enumerate(questions, start=1):
    print(f"\nQuestion {index}")
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter Option: ").strip().lower()
    while answer not in ["a", "b", "c", "d"]:
        print("Invalid option! Enter only a, b, c, or d.")
        answer = input("Enter Option: ").strip().lower()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print(f"Correct Option: {q['answer']}")
        wrong += 1

final_score = score - (wrong * 0.25)

print("\n===== RESULT =====")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong}")
print(f"Final Score     : {final_score}")

if len(questions) > 0:
    percentage = (score / len(questions)) * 100
else:
    percentage = 0

print(f"Percentage      : {percentage:.2f}%")
print("======================")

save_score(username, final_score, percentage, difficulty)
print("Score saved successfully!\n")



