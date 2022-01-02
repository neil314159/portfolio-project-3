from prettytable import PrettyTable
from termcolor import colored
import math


class TableView():
    """ Presents lists of users in a table
    that is printed in a pleasing format.
    The current page number is stored to allow
    paging forward and back through the list
    of records.
    """

    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number
        self.max_pages = math.ceil(len(self.patient_data)/10)

    def print_table(self):
        """ Uses 3rd party library to format
        data for printing as a table to the terminal.

        """
        patient_view = PrettyTable()
        patient_view.field_names = [
            "Number", "First Name", "Last Name",
            "Age", "Dose 1", "Dose 2", "Booster"]
        # Max width for names to prevent tables overflowing screen
        patient_view._max_width = {"First Name": 20, "Last Name": 20}
        yes = colored('Yes', 'green')
        no = colored("NO", 'white', 'on_red')

        start_record = (self.page_number)*10
        end_record = ((self.page_number)*10) + 10

        # Enumerates over the current slice of data
        for i, patient in enumerate(self.patient_data[start_record:end_record],
                                    start_record):
            new_row = []
            new_row.append(i+1)
            new_row.append(getattr(patient, 'firstname'))
            new_row.append(getattr(patient, 'lastname'))
            new_row.append(patient.age())
            new_row.append(yes) if((getattr(patient, 'first_dose')) ==
                                   "TRUE") else new_row.append(no)
            new_row.append(yes) if((getattr(patient, 'second_dose')) ==
                                   "TRUE") else new_row.append(no)
            new_row.append(yes) if((getattr(patient, 'booster_dose')) ==
                                   "TRUE") else new_row.append(no)
            patient_view.add_row(new_row)
        print(colored(f'Page number: {self.page_number+1}', 'yellow'))
        print(patient_view)
