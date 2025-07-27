questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal?",
    "Which language is used to create web pages?"
]

options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Nehru", "B. Bhagat Singh", "C. Gandhi", "D. Bose"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippo"],
    ["A. HTML", "B. C++", "C. Python", "D. Java"]
]

answers = ["B", "C", "B", "B", "A"]
money = 0

for i in range(len(questions)):
    print(f"\nQ{i+1}: {questions[i]}")
    for opt in options[i]:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()

    if user_ans == answers[i]:
        money += 10000
        print("✅ Correct! You won ₹10,000\n")
    else:
        print("❌ Wrong answer!")
        print(f"You take home ₹{money}")
        break
else:
    print("🎉 Congratulations! You answered all questions correctly!")
    print(f"You take home ₹{money}")