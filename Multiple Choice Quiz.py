import random
# imports the random module into the code so we can randomly select a quiz questions

def start_quiz():
    questions = [
        {
            "questions": "Question 1",
            "options": ["A. 1", "B. 2", "C. 3"],
            "answer": "A"
        },
        #This is the first dictionary in the list of questions. 
        #Here will add the question, options and answer to the dictionary
        # I have included a list inside of the dictionary here to facilitate the multiple choice.
        # Now we just need to duplicate this to add as many question options as we want. 
        {
            "questions": "Question 2",
            "options": ["A. 1", "B. 2", "C. 3"],
            "answer": "B"
        },
        {
            "questions": "Question 3",
            "options": ["A. 1", "B. 2", "C. 3"],
            "answer": "C"
        },
    ]
 
 # Now that we have defined the question list for the quiz we are going to print the welcome message. 
 # the message will tell the user how the game is going to work and what to input 

    print("Welcome to Jacks tester quiz")
    print("The game will consist of questions that you answer with A, B or C")
    print("Each correct answer in the game is going to give you one point")

    random.shuffle(questions)
    # Shuffles the questions randomly

    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q["questions"]}")
        for option in q["options"]:
            print(option)
    # this for loop starts iterating through each question in the questions list

        answer = input("Choose, A, B or C?: ").strip().upper()

        if answer == q['answer']:
            print(f"Correct!, the answer is {q['answer']}!")
            score += 1
        else:
            print(f"Incorrect, the answer was {q['answer']}")
    # This will check if the asnwwer is correct in relation to the answer in the list

    print(f"\nGame Over! Your final score was {score} / {len(questions)}")
    if score == len(questions):
        print("Maximum Points!")
    elif 0 < score < len(questions):
        print("Almost! Still Good Tho!")
    else:
        print("Retard")

if __name__ == "__main__":
    start_quiz()

              
            







