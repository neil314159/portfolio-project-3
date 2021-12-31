#class for patient info

from datetime import datetime


class Patient:


    def __init__(self, id,firstname, lastname, date_of_birth, first_dose, second_dose, booster):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.first_dose = first_dose
        self.seconddose = second_dose
        self.booster = booster

    def age(self):
        newdate = self.date_of_birth.split('/')
        days = int(newdate[0])
        months = int(newdate[1])
        years = int(newdate[2])
            
        today = datetime.today()

        difference = ((today.month, today.day) < (months, days))
            
        bday = today.year - years - int(difference)
        #print(bday)
        
        return bday