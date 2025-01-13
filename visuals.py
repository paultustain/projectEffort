from logic import Timer 
from enum import Enum 

class Styles:
    NORMAL = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    CYAN = "\033[36m"
    WHITE = "\033[90m"
    GREEN = "\033[32m"
    STRONG_GREEN = "\033[92m"


class Visualiser:
    FULL_WIDTH = 180
    AIMS_WIDTH = (3 * FULL_WIDTH//4)
    HELP_WIDTH = FULL_WIDTH//4
    
  
    def __init__(self, project, aim_flag):
        self.styles = Styles()
        self.timer = Timer()
        self._project = project if project is not None else "Unsaved Project"
        self._aim_flag = aim_flag
        self._aims = []
        if aim_flag:
            self._set_project_aims()
        self.set_initial()
        
    
    def _set_project_aims(self):
        for _ in range(5):
            print("Add notes around an aim for the session:")
            aim = input() 
            self._aims.append(aim)
            print("Do you want to add another aim? (y/n):")
            another = input()
            if another.lower() == "n":
                break 


    def set_initial(self):
        project_name_line = f"Currently Tracking for: {self.styles.UNDERLINE}{self.styles.CYAN}{self._project}{self.styles.NORMAL}{self.styles.WHITE}{self.styles.BOLD}"
        space_left = (self.FULL_WIDTH - (28 + len(self._project)))
        extra = int(not((space_left / 2) == (space_left // 2)))
        print(f"{self.styles.BOLD}{self.styles.WHITE}{'='* self.FULL_WIDTH}")
        print(f"||{' ' * (self.FULL_WIDTH -4)}||")
        print(f"||{' ' * (space_left//2)}{project_name_line}{' ' * (extra + space_left//2)}||")
        print(f"||{' ' * (self.FULL_WIDTH -4)}||")
        print("=" * self.FULL_WIDTH)
        print("")
        print("=" * (self.AIMS_WIDTH-2)," ","=" * ((self.FULL_WIDTH//4)-1))
        print(f"|| {self.styles.UNDERLINE}Session Aims{self.styles.NORMAL}{self.styles.WHITE}{self.styles.BOLD}:{' ' * (self.AIMS_WIDTH-20)}||   || {self.styles.UNDERLINE}Commands{self.styles.NORMAL}{self.styles.WHITE}{self.styles.BOLD}: {' ' * (self.HELP_WIDTH - 16)}||")
        for n, aim in enumerate(self._aims):
            distance_left = self.AIMS_WIDTH - (10 + len(aim))
            print(f"||{self.styles.NORMAL}{self.styles.NORMAL} {n+1}. {aim}{' '*distance_left}{self.styles.NORMAL}{self.styles.WHITE}{self.styles.BOLD}||   ||{' ' * (self.HELP_WIDTH - 5)}||")
        print("=" * (self.AIMS_WIDTH-2)," ","=" * ((self.FULL_WIDTH//4)-1))
        self._print_stage()
        self.timer.count_down()


    def _print_stage(self):
        swatch = {
            "main": self.styles.GREEN, 
            "highlight": self.styles.STRONG_GREEN
        } 
        print(f"{swatch['main']}=" * (self.AIMS_WIDTH-2))
        print(f"|| {self.timer.stage}{' '*(self.AIMS_WIDTH-(len(self.timer.stage)+7))}||")


    def __repr__(self):
        if self._seconds < 10:
            seconds_string = "0" + str(self._seconds)
        else:
            seconds_string = str(self._seconds)
        return f"{self._minutes}:{seconds_string}"
    


