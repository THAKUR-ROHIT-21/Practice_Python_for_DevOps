print(" Welcome to KBC Quiz Game ")

start = input("Do you want to start the game? (yes/no):- ")

if start == "yes":

    score = 0
    correct = 0
    wrong = 0
    skipped = 0


    # ---------------- QUESTION 1 ----------------
    print("\n1. What is the capital of India?")
    print("A. Mumbai")
    print("B. Delhi")
    print("C. Kolkata")
    print("D. Chennai")

    ans1 = input("Your answer (A/B/C/D or skip):-  ")

    if ans1 == "B":
        print("Correct!")
        score = score + 1000
        correct = correct + 1
    elif ans1 == "skip":
        print("Skipped!")
        skipped = skipped + 1
    else:
        print("Wrong!")
        wrong = wrong + 1


    # ---------------- QUESTION 2 ----------------
    print("\n2. Which planet is known as Red Planet?")
    print("A. Earth")
    print("B. Venus")
    print("C. Mars")
    print("D. Jupiter")

    ans2 = input("Your answer (A/B/C/D or skip): ")

    if ans2 == "C":
        print("Correct!")
        score = score + 2000
        correct = correct + 1
    elif ans2 == "skip":
        print("Skipped!")
        skipped = skipped + 1
    else:
        print("Wrong!")
        wrong = wrong + 1


    # ---------------- QUESTION 3 ----------------
    print("\n3. Who wrote Hamlet?")
    print("A. Charles Dickens")
    print("B. William Shakespeare")
    print("C. Mark Twain")
    print("D. Jane Austen")

    ans3 = input("Your answer (A/B/C/D or skip): ")

    if ans3 == "B":
        print("Correct!")
        score = score + 3000
        correct = correct + 1
    elif ans3 == "skip":
        print("Skipped!")
        skipped = skipped + 1
    else:
        print("Wrong!")
        wrong = wrong + 1


    # ---------------- QUESTION 4 ----------------
    print("\n4. What is the largest ocean?")
    print("A. Atlantic")
    print("B. Indian")
    print("C. Arctic")
    print("D. Pacific")

    ans4 = input("Your answer (A/B/C/D or skip): ")

    if ans4 == "D":
        print("Correct!")
        score = score + 5000
        correct = correct + 1
    elif ans4 == "skip":
        print("Skipped!")
        skipped = skipped + 1
    else:
        print("Wrong!")
        wrong = wrong + 1


    # ---------------- QUESTION 5 ----------------
    print("\n5. Smallest prime number?")
    print("A. 0")
    print("B. 1")
    print("C. 2")
    print("D. 3")

    ans5 = input("Your answer (A/B/C/D or skip): ")

    if ans5 == "C":
        print("Correct!")
        score = score + 10000
        correct = correct + 1
    elif ans5 == "skip":
        print("Skipped!")
        skipped = skipped + 1
    else:
        print("Wrong!")
        wrong = wrong + 1


    # ---------------- FINAL RESULT ----------------
    print("\n🎯 GAME OVER 🎯")
    print("Total Score:", score)
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)

else:
    print("Maybe next time! 👋")