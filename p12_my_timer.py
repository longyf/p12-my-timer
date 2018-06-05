# p12_my_timer.py
"""
Test MyTimer.
My version.
"""
import time

class MyTimer:
    
    def __init__(self):
        self.start_timing = False
        self.end_timing = False
        self.start_time = 0
        self.end_time = 0
        self.time_difference = 0

    def start(self):
        if self.start_timing == True:
            print("Already started.")
        else:
            print("Start timing.")
            self.start_timing = True
            self.start_time = time.localtime()

    def stop(self):
        if self.start_timing == False:
            print("Not started yet. Please use start().")
        elif self.end_timing == True:
            print("Already ended.")
        else:
            print("End timing.")
            self.end_timing = True
            self.end_time = time.localtime()

    def cal_time_diff(self):
        print("Assume that start and stop times are in the same day.")
        self.time_difference = (self.end_time.tm_hour * 60 * 60 + self.end_time.tm_min * 60 + self.end_time.tm_sec) - (self.start_time.tm_hour * 60 * 60 + self.start_time.tm_min * 60 + self.start_time.tm_sec) 
        return self.time_difference
    
    def __str__(self):
        if self.start_timing == False and self.end_timing == False:
            return "Not started yet."
        elif self.start_timing == True and self.end_timing == True:
            return "The time is " + str(self.cal_time_diff()) + " seconds."
        elif self.start_timing == False and self.end_timing == True:
            return "Not started yet. Please use start()."
        else:
            return "Not ended yet. Please use end()."
        
    def __repr__(self):
        if self.start_timing == False and self.end_timing == False:
            return "Not started yet."
        elif self.start_timing == True and self.end_timing == True:
            return "The time is " + str(self.cal_time_diff()) + " seconds."
        elif self.start_timing == False and self.end_timing == True:
            return "Not started yet. Please use start()."
        else:
            return "Not ended yet. Please use end()."
        
    def __add__(self, other):
        print("The sum of time is: " + str(self.time_difference + other.time_difference) + " seconds.")

    def reset(self):
        self.__init__()

        

   
                
