from prettytable import PrettyTable
from termcolor import colored


class TableView():
    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number

    def print_table(self):

        patient_view = PrettyTable()
        patient_view.field_names = [
            "Number", "First Name", "Last Name", "Age", "Dose 1", "Dose 2", "Booster"]
        patient_view._max_width = {"First Name": 20, "Last Name": 20}

        green_yes = colored('Yes', 'green')
        red_no = colored("NO", 'white', 'on_red')

    #     for i, elm in enumerate(test_list[7:40], 7):
    # print i, elm stack overflow
    
        for i, patient in enumerate(self.patient_data[21:31], 21):
            new_row = []
            new_row.append(i)
            new_row.append(getattr(patient, 'firstname'))
            new_row.append(getattr(patient, 'lastname'))
            new_row.append(patient.age())

            new_row.append(green_yes) if((getattr(patient, 'first_dose'))
                                         == "TRUE") else new_row.append(red_no)
            new_row.append(green_yes) if((getattr(patient, 'second_dose'))
                                         == "TRUE") else new_row.append(red_no)
            new_row.append(green_yes) if(
                (getattr(patient, 'booster_dose')) == "TRUE") else new_row.append(red_no)

            patient_view.add_row(new_row)

        print(patient_view)

    def next_page(self):
        self.page_number += 1
