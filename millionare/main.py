questions = [
    ["Who is Shahrukh Khan?", "WWE wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Which ocean is the largest?", "Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", 1],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 1]   
]

prizes = [1000, 2000, 3000, 4000, 5000]

i = 0

for question in questions:
    print("\n" + question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    a = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
    if a == question[5]:
            print("✅ Correct answer!")
    else:
            correct_option = ["a", "b", "c", "d"][question[5]-1]
            correct_text = question[question[5]]
            print(f"❌ Incorrect. The correct answer was option {correct_option}: {correct_text}")
            print("Better luck next time!")
            break
    print("you won {}")
    i +=1
    
