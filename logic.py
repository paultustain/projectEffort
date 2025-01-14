from time import sleep, perf_counter

class Timer:
    def __init__(self, work_length=25, break_length=5):
        
        self._minutes = work_length
        self._seconds = 0
        self.stage = "Work"
        self._work_length = work_length
        self._break_length = break_length
        self.round = 1
        self._running = True
        self._reset_stage = False

    def get_next(self):
        if self._seconds == 0:
            self._seconds = 59
            if self._minutes == 0:
                self._reset_stage = True
                if self.stage == "Work":
                    self._minutes = self._break_length
                    self.stage = "Break"
                else:
                    self._minutes = self._work_length
                    self.stage = "Work"
                    self.round += 1
                self._seconds = 0
            else:
                self._minutes -= 1
        else:
            self._seconds -= 1 

    def clear_line(self):
        print("\033[A                                                                                                     \033[A")
    
    
#     def print_stage(self):
#         print(f"""------------------------------------------------------
# {self._stage}
# ------------------------------------------------------""")
    

    def print_time(self):
        if self._seconds < 10:
            seconds_string = "0" + str(self._seconds)
        else:
            seconds_string = str(self._seconds)
        print(f"{self._minutes}:{seconds_string}")
        

    def count_down(self):

        print("")
        while self._running: 
            start = perf_counter()
            self.clear_line()
            if self._reset_stage:
                self.clear_line()
                self.clear_line()
                self.clear_line()
                self.print_stage()
            self.print_time()
            self.get_next()

            sleep(0.01 - (perf_counter() - start))



    
