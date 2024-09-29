questions = [
    ["Which programming language is primarily used for Android app development?", "Python", "Java", "Swift", "C#", 2],
    ["Which programming language is known for its use in web development?", "Python", "HTML", "Java", "C++", 2],
    ["Who is the founder of Microsoft?", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk", 2],
    ["Which of these is a version control system?", "Git", "Java", "Python", "HTML", 1],
    ["What does HTML stand for?", "Hyper Text Markup Language", "Hyper Tool Markup Language", "High Tech Markup Language", "Hyper Transfer Markup Language", 1],
    ["Which company created the iPhone?", "Microsoft", "Google", "Apple", "Samsung", 3],
    ["Which operating system is open-source?", "Windows", "macOS", "Linux", "iOS", 3],
    ["What is the shortcut for 'copy' on most computers?", "Ctrl + P", "Ctrl + C", "Ctrl + V", "Ctrl + Z", 2],
    ["What is the most used programming language for Android app development?", "C++", "Python", "Java", "PHP", 3],
    ["Which of these companies was co-founded by Steve Jobs?", "Microsoft", "Apple", "Google", "Amazon", 2],
]

levels = [1000, 10000, 50000, 100000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 100000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"{i + 1}. {question[0]}")
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c. {question[3]}    d. {question[4]}")

    ans = input("Enter the option (a, b, c, d) or press 0 to quit: ").strip().lower()

    if ans == '0':
        print(f"You have chosen to quit. Total money won: {money}")
        break


    answer_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    if answer_map.get(ans) == question[5]:
        print(f"Correct! You won {levels[i]}!")
        money += levels[i]
    else:
        print("Incorrect! Game over.")
        break

print(f"Total money won: {money}")