import random
easyQuestionBank = [
    {
        "question" : "What is the biggest country in the world by landmass?",
        "options" : ["China", "India", "ENGLAND", "Russia"],
        "answer" : "Russia"
    },
    {
        "question" : "What date was 9/11?",
        "options" : ["9/11", "11/9", "1/1", "8/9"],
        "answer" : "9/11"
    },
    {
        "question" : "What is the largest planet in our solar system?",
        "options" : ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer" : "Jupiter"
    },
    {
        "question" : "What is the capital of France?",
        "options" : ["London", "Berlin", "Paris", "Madrid"],
        "answer" : "Paris"
    },
    {
        "question" : "How many sides does a hexagon have?",
        "options" : ["5", "6", "7", "8"],
        "answer" : "6"
    },
    {
        "question" : "What animal is the largest mammal in the world?",
        "options" : ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer" : "Blue Whale"
    },
    {
        "question" : "What is the chemical symbol for gold?",
        "options" : ["Au", "Ag", "Gd", "Go"],
        "answer" : "Au"
    },
    {
        "question" : "What is the tallest mountain in the world?",
        "options" : ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer" : "Mount Everest"
    },
    {
        "question" : "What is the largest ocean in the world?",
        "options" : ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer" : "Pacific Ocean"
    },
    {
        "question" : "What is the smallest country in the world by land area?",
        "options" : ["Vatican City", "Monaco", "Nauru", "San Marino"],
        "answer" : "Vatican City"
    }
]

mediumQuestionBank = [
    {
        "question" : "In which year did the Berlin Wall fall?",
        "options" : ["1987", "1989", "1991", "1993"],
        "answer" : "1989"
    },
    {
        "question" : "Who wrote the novel 1984",
        "options" : ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"],
        "answer" : "George Orwell"
    },
    {
        "question" : "What is the chemical symbol for iron?",
        "options" : ["Fe", "Ir", "I", "In"],
        "answer" : "Fe"
    },
    {
        "question" : "Which country has the most natural lakes?",
        "options" : ["Canada", "Russia", "USA", "Brazil"],
        "answer" : "Canada"
    },
    {
        "question" : "What is the capital of New Zealand?",
        "options" : ["Auckland", "Wellington", "Christchurch", "Hamilton"],
        "answer" : "Wellington"
    },
    {
        "question" : "What is the largest desert in the world?",
        "options" : ["Sahara", "Gobi", "Kalahari", "Antarctic Desert"],
        "answer" : "Antarctic Desert"
    },
    {
        "question" : "What is the largest organ in the human body?",
        "options" : ["Liver", "Skin", "Heart", "Lungs"],
        "answer" : "Skin"
    },
    {
        "question" : "What is the capital of Iceland?",
        "options" : ["Reykjavik", "Oslo", "Helsinki", "Copenhagen"],
        "answer" : "Reykjavik"
    },
    {
        "question" : "What is the largest species of shark?",
        "options" : ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark"],
        "answer" : "Whale Shark"
    },
    {
        "question" : "Which element has the atomic number 26?",
        "options" : ["Iron", "Copper", "Zinc", "Manganese"],
        "answer" : "Iron"
    }
]

hardQuestionBank = [
    {
        "question" : "What is the name of the boundary around a black hole beyond which nothing can escape?",
        "options" : ["Event Horizon", "Singularity", "Photon Sphere", "Accretion Disk"],
        "answer" : "Event Horizon"
    },
    {
        "question" : "Which treaty formally ended the state of war between Germany and the Allied Powers after World War I?",
        "options" : ["Treaty of Versailles", "Treaty of Paris", "Treaty of Ghent", "Treaty of Tordesillas"],
        "answer" : "Treaty of Versailles"
    },
    {
        "question" : "Which ancient civilisation developed the cuneiform writing system?",
        "options" : ["Egyptians", "Sumerians", "Babylonians", "Assyrians"],
        "answer" : "Sumerians"
    },
    {
        "question" : "What is the name of the first artificial Earth satellite launched by the Soviet Union in 1957?",
        "options" : ["Sputnik 1", "Explorer 1", "Vostok 1", "Luna 1"],
        "answer" : "Sputnik 1"
    },
    {
        "question" : "Which physicist is known for the uncertainty principle in quantum mechanics?",
        "options" : ["Albert Einstein", "Niels Bohr", "Werner Heisenberg", "Erwin Schrödinger"],
        "answer" : "Werner Heisenberg"
    },
    {
        "question" : "Which element has the highest melting point of all elements?",
        "options" : ["Tungsten", "Carbon", "Iron", "Osmium"],
        "answer" : "Tungsten"
    },
    {
        "question" : "What is the name of the largest moon of Saturn?",
        "options" : ["Titan", "Ganymede", "Callisto", "Io"],
        "answer" : "Titan"
    },
    {
        "question" : "Which mathematician is known for his work on the foundations of calculus and the development of infinitesimal calculus?",
        "options" : ["Isaac Newton", "Gottfried Wilhelm Leibniz", "Carl Friedrich Gauss", "Leonhard Euler"],
        "answer" : "Gottfried Wilhelm Leibniz"
    },
    {
        "question" : "What is the name of the first woman to win a Nobel Prize?",
        "options" : ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Dorothy Hodgkin"],
        "answer" : "Marie Curie"
    },
    {
        "question" : "Which planet in our solar system has the shortest day?",
        "options" : ["Mercury", "Venus", "Jupiter", "Saturn"],
        "answer" : "Jupiter"
    }

]

playAgain = True
attemptedQuestions = 0
questionBank = ""
answer = ""
score = 0

playAgain = True
while playAgain == True:
    difficultyChoice = input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficultyChoice not in ["easy", "medium", "hard"]:
        difficultyChoice = input("Invalid choice. Please choose a difficulty level (easy, medium, hard): ").lower()

    if difficultyChoice == "easy":
        questionBank = easyQuestionBank
    elif difficultyChoice == "medium":
        questionBank = mediumQuestionBank
    elif difficultyChoice == "hard":
        questionBank = hardQuestionBank

    score = 0

    while attemptedQuestions < 5:
        selectedQuestions = random.sample(questionBank, 5)
        for question in selectedQuestions:
            print(question["question"])
            print(question["options"])
            playerAnswer = input("Please enter your answer:").lower()
            lowerOptions = [option.lower() for option in question["options"]]
            while playerAnswer not in lowerOptions:
                playerAnswer = input("Please enter a valid answer:").lower()
            lowerAnswer = question["answer"].lower()
            if playerAnswer == lowerAnswer:
                print("Congratulations, you got it right!")
                score += 1
            else:
                print("Answer: " + lowerAnswer)
                print("Player Answer: " + playerAnswer)
                print(f"Incorrect, the answer was: {question["answer"]}")
                print 
            
            attemptedQuestions += 1
    print(f"Your score was {score}/5.")
    playYN = input("Would you like to play again? Y/N: ").lower()
    while playYN not in ["y","n"]:
        playYN = input("Please enter a valid input, Y/N: ")
    if playYN == "y":
        playAgain = True
        attemptedQuestions = 0
    else:
        playAgain = False
        print("Thank you for playing.")









