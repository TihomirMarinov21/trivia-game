import sys
from colorama import Fore 

# declarations

# Questions, Answers, and Solutions

cs_questions = {
    1: "What does CPU stand for?",
    2: "What is the main function of the operating system?",
    3: "Which of the following is a type of sorting algorithm?",
    4: "Which of these languages is primarily used for web development?",
    5: "What is the purpose of an IP address?",
    6: "What does 'HTML' stand for?",
    7: "Which of the following is a version control system?"
}

cs_answers = {
    1: ["Central Processing Unit", "Central Program Unit", "Computer Power Unit", "Central Programming Unit"],
    2: ["Managing memory", "Running applications", "Managing hardware resources", "All of the above"],
    3: ["QuickSort", "Binary Search", "Linked List", "Cache"],
    4: ["Python", "JavaScript", "C++", "Ruby"],
    5: ["To store data", "To identify a device on a network", "To provide internet access", "To secure online transactions"],
    6: ["HyperText Machine Language", "HyperText Markup Language", "HighText Markup Language", "HyperTab Markup Language"],
    7: ["Git", "SQL", "Docker", "React"]
}

cs_solution = {
    1: "A",  
    2: "D",  
    3: "A",  
    4: "B",  
    5: "B",  
    6: "B",  
    7: "A"   
}

# New Category: General Knowledge
# General Knowledge Questions
questions_general_knowledge = {
    1: "What is the capital of France?",
    2: "Who wrote 'Romeo and Juliet'?",
    3: "What is the largest planet in our solar system?",
    4: "Which element has the chemical symbol 'O'?",
    5: "Who painted the 'Mona Lisa'?",
    6: "In which year did the Titanic sink?",
    7: "Who invented the telephone?"
}

# Answers with varied options
answers_general_knowledge = {
    1: ["Berlin", "London", "Paris", "Madrid"],
    2: ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    3: ["Saturn","Jupiter", "Earth", "Neptune"],
    4: ["Osmium", "Ozone", "Opium","Oxygen"],
    5: ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    6: ["1905", "1898","1912", "1920"],
    7: ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"]
}

# Correct answers (now with variety)
solution_general_knowledge = {
    1: "C",  # Paris
    2: "A",  # William Shakespeare
    3: "B",  # Jupiter
    4: "D",  # Oxygen
    5: "A",  # Leonardo da Vinci
    6: "C",  # 1912
    7: "A"   # Alexander Graham Bell
}


# Classes
class Game:

    round = 1
    running = True
    q_choice = 0

    def __init__(self):
        self.type = "trivia game"

    #takes answer input and handles possible input error    
    @staticmethod
    def get_player_amount():
        while True:  
            try:
                amount_of_players = int(input(f"{Fore.LIGHTMAGENTA_EX}How many players will be playing this game ? (min 2)\n"))
                if amount_of_players < 2:
                    print("The minimum amount of player is 2!!!")
                    continue
                return amount_of_players
            except: 
                print("Invalid input. Integer higher than or equal to 2 expected")
    #takes answer input and handles possible input error
    @staticmethod
    def get_category():
        while True:  
            try:
                Game.q_choice = int(input("1: General knowledge \n2: computer science: "))
                if Game.q_choice not in [1,2]:
                    print("You can only choose between 1 and 2")
                    continue
                return Game.q_choice
            except ValueError:
                    print("Invalid input. You can only choose between 1 and 2")

    
    #the following function creates the players and lets them choose the topic
    @staticmethod
    def start() -> None:
        print(f"{Fore.WHITE}**********************************")
        print("Game starts \n")

        amount_of_players = Game.get_player_amount()

        print(f"{Fore.WHITE}\n**********************************")

        for i in range(amount_of_players):
            print(f"{Fore.LIGHTYELLOW_EX}What is player #{i+1}'s name ?")
            player_name = input()
            player_index = i
            player = Player(player_name,player_index) 

        print(f"{Fore.GREEN}\n{Player.player_list[1].name} can choose the topic")
        Game.get_category()
        print(f"{Fore.WHITE}\n**********************************")
        Question.display_question()

    # evalutes the answer
    @staticmethod
    def check_answer()-> None:
            if Player.currentplayer.answer == Question.solution[Question.count]:
                Player.currentplayer.points += 1
                print(f"{Fore.GREEN}CORRECT !!!")         
                if Game.round == 14:
                    Game.running = False
                    print(f"{Fore.RED}\nThe game is over")
                    Game.show_score()
                    sys.exit()
                else:
                    Game.show_score()
                    del Question.questions[Question.count]
                    Game.round += 1
                    Question.count += 1
                    Question.display_question()
                    print(f"{Fore.WHITE}\n**********************************")
            else:
                print(f"{Fore.RED}WRONG !!!")
                Game.switch_player()
    
    # switches player when the current one makes a mistake
    @staticmethod
    def switch_player()-> None:
        if Player.currentplayer.index == len(Player.player_list) - 1:
            Player.currentplayer = Player.player_list[0]
            Player.answering()
        else:
            Player.currentplayer = Player.player_list[Player.currentplayer.index + 1]
            Player.answering()

    # shows score every time a player has anwered correctly in addition to that it checks after all rounds for the winner
    @staticmethod   
    def show_score()-> None:
        if Game.round == 14:
            max_score = 0
            winners = []

            #find the highest score
            for p in Player.player_list:
                if p.points > max_score:
                    winners = [p]
                    max_score = p.points
                elif p.points == max_score:
                    winners.append(p)

            if len(winners) == 1:
                print(f"{Fore.LIGHTGREEN_EX}The winner is {winners[0]}!!!")
            else:
                print(f"{Fore.YELLOW}It's a draw between:")

        for p in Player.player_list:
            print(f"{p.name}: {p.points}")
        print(f"{Fore.WHITE}\n**********************************")
                        

class Player:
    player_list = []
    currentplayer = None

    def __init__(self,name,index):
        self.name = name
        self.points = 0
        self.index = index
        self.answer = ""
        self.player_list.append(self)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    #takes answer input and handles possible input error
    @staticmethod
    def get_answer():
         while True:
              try:
                Player.currentplayer.answer = input(f"{Fore.GREEN}{Player.currentplayer}'s answer: ").upper()

                if Player.currentplayer.answer not in ["A", "B", "C","D"]:
                     print("Please type in one of this options:\n a,b,c or d")
                     continue
                break
              except: ValueError
              print("This input is not valid!\n Please type in a,b,c or d")

    # lets the players answers in order of sign in
    @staticmethod
    def answering() -> None:
        if Player.currentplayer is None:
            Player.currentplayer = Player.player_list[0] 
        Player.get_answer()
        Game.check_answer()

class Question:
    count = 1

    def __init__(self)-> None:
        self.questions = None
        self.answers = None
        self.solution = None

    # determines the category and displays the questions
    @staticmethod
    def display_question()-> None:
        
        print(f"{Fore.LIGHTYELLOW_EX}Round #{Game.round}")
        
        if Question.count == 8:
            print(f"{Fore.CYAN}Topic changes")
            Game.q_choice = 1 if Game.q_choice == 2 else 2
            Question.count = 1

        if Game.q_choice == 2:
            Question.questions = cs_questions 
            Question.answers = cs_answers 
            Question.solution = cs_solution
        else:
            Question.questions = questions_general_knowledge
            Question.answers = answers_general_knowledge
            Question.solution = solution_general_knowledge
            
        for value in Question.questions:
            labels = ["A", "B", "C", "D"]
            print(f"{Fore.LIGHTYELLOW_EX}Question: {Question.questions[value]} \n")
            for i,ans in enumerate(Question.answers[value]):
                print(f"{labels[i]}: {ans}")
            print(f"{Fore.WHITE}\n**********************************")
            Player.answering()

# main function
def main()-> None:
    Game.start()
if __name__ == "__main__":
    main()

