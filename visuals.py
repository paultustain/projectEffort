from logic import Timer 

class Visualiser:
    FULL_WIDTH = 180
    AIMS_WIDTH = (3 * FULL_WIDTH//4)
    HELP_WIDTH = FULL_WIDTH//4
    def __init__(self, project, aims):
        self._project = project if project is not None else "Unsaved Project"
        self._aims = aims
        self.set_initial()
    
    def set_initial(self):
        project_name_line = f"Currently Tracking for: {self._project}"
        space_left = (self.FULL_WIDTH - len(project_name_line) - 4)
        extra = int(not((space_left / 2) == (space_left // 2)))
        print("=" * self.FULL_WIDTH)
        print(f"||{' ' * ((self.FULL_WIDTH - len(project_name_line) - 4)//2)}{project_name_line}{' ' * (extra + (self.FULL_WIDTH - len(project_name_line) - 4)//2)}||")
        print("=" * self.FULL_WIDTH)
        print("")
        print("=" * (self.AIMS_WIDTH-2)," ","=" * ((self.FULL_WIDTH//4)-1))
        print(f"|| Session Aims:{' ' * (self.AIMS_WIDTH-20)}||   || Commands: {' ' * (self.HELP_WIDTH - 16)}||")

    def __repr__(self):
        if self._seconds < 10:
            seconds_string = "0" + str(self._seconds)
        else:
            seconds_string = str(self._seconds)
        return f"{self._minutes}:{seconds_string}"
    


