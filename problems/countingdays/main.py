# Include the necessary header file
include "countingdays.h"

class ProgrammingDaysCounter:
    def __init__(self):
        self.days = 1
        self.last_hours = 0
        self.last_minutes = 0
    
    def lookAtClock(self, hours, minutes):
        if hours < self.last_hours or (hours == self.last_hours and minutes < self.last_minutes):
            self.days += 1
        self.last_hours = hours
        self.last_minutes = minutes
    
    def getDay(self):
        return self.days

# Create an instance of the ProgrammingDaysCounter class
counter = ProgrammingDaysCounter()