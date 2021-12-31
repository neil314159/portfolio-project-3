#class for patient info

from datetime import date


class Patient:


    def __init__(self):
        self.firstname = "neil"
        self.lastname = "boland"
        self.dob = "1000"
        self.firstdose = "TRUE"
        self.seconddose = "TRUE"
        self.booster = "TRUE"

def age(self):
    return date.today()