class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod      
    def change_leaves(cls, new_leaves):         
        cls.no_of_leaves = new_leaves
        
    @classmethod       
    def from_str(cls, str1):
        return cls(*str1.split("-"))

    @staticmethod
    def simple_func(str2):
        return ("This is a STATIC-METHOD " + str2)

class Player:
    no_of_games = 5
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_game_details(self):
        return f"The name is {self.name}. The game is {self.game}"

class Employee_player(Employee, Player):
    language = "Java"
    var = 10
    def print_lang(self):
        print(self.language) 

rahul = Employee("Rahul", 45000, "Coder")
rohit = Employee_player("Rohit", 35000, "Programmer")

lovish = Player("Lovish", ["Cricket", "Football", "Basketball"])
atul = Employee_player.from_str("Atul-85000-HR")
# atul = Player.print_game_details("Atul", "Chess")   # Shows error

print(atul.print_details())
atul.print_lang()
print(atul.var)                 # 1st-Employee_player; 2nd-Employee; 3rd-Player  -> in chronological order as defined above in class