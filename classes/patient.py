# class for patient info

from datetime import datetime


class Patient:

    def __init__(self, user_id, sheet_index, firstname, lastname, date_of_birth, first_dose, second_dose, booster):
        self.id = user_id
        self.sheet_index = sheet_index
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.first_dose = first_dose
        self.second_dose = second_dose
        self.booster_dose = booster

    def age(self):
        date_of_birth = self.date_of_birth.split('/')
        days = int(date_of_birth[0])
        months = int(date_of_birth[1])
        years = int(date_of_birth[2])
        today = datetime.today()
        difference = ((today.month, today.day) < (months, days))
        age = today.year - years - int(difference)
        return age

    def get_id(self):
        return int(self.id)
