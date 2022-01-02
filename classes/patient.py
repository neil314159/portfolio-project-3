from datetime import datetime


class Patient:
    """ Represents patients in the system.
   Main Clinic class stores users a list of
   Patients.
    """

    def __init__(self, user_id, sheet_index, firstname, lastname,
                 date_of_birth, first_dose, second_dose, booster):
        """ Creates Patient object, also keeps
        track of position in Google Sheets
        to allow updates.
        """
        self.id = user_id
        self.sheet_index = sheet_index
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.first_dose = first_dose
        self.second_dose = second_dose
        self.booster_dose = booster

    def age(self):
        """ Age is calculated as a property
        related to the current date and returned
        when needed.
        """
        date_of_birth = self.date_of_birth.split('/')
        days = int(date_of_birth[0])
        months = int(date_of_birth[1])
        years = int(date_of_birth[2])
        today = datetime.today()
        difference = ((today.month, today.day) < (months, days))
        age = today.year - years - int(difference)
        return age

    def get_id(self):
        """ Used to return ID when checking for
        uniqueness before creating a new Patient
        """
        return int(self.id)
