# class to manage entire app

import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
from datetime import datetime
import pyinputplus as pyip
import os
from termcolor import colored
from random import randint
from pyfiglet import Figlet
from classes.patient import Patient
from classes.tableview import TableView


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cpm_data')


class Clinic:

    def load_patients(self):

        patient_list2 = []
        info = SHEET.worksheet('data')
        data = info.get_all_values()

        for a in data:
            patient_list2.append(
                Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

        return patient_list2

    def header(self, text):
        result = Figlet()
        return result.renderText(text)

    def clear_display(self):
        os.system('clear')

    def __init__(self):
        self.patient_list = self.load_patients()
        self.clear_display()

        self.main_menu()

    def main_menu(self):
        self.clear_display()
        print(colored(self.header("Vaccine Clinic Tracker"), 'green'))
        response = pyip.inputMenu(['Guide', 'View At Risk Patients', 'View All Patients',
                                   'Enroll New Patient', 'View Progress Dashboard'], numbered=True)

        if response == "Guide":
            self.show_guide()
        if response == "View At Risk Patients":
            self.clear_display()
            self.view_at_risk_patients()
        if response == "View All Patients":
            self.clear_display()
            self.view_all_patients()()
        if response == "View Progress Dashboard":
            self.show_dashboard()
        if response == "Enroll New Patient":
            self.add_new_patient()

    def show_dashboard(self):
        self.clear_display()

        print(colored(self.header("Dashboard"), 'green'))

        first_dose, second_dose, booster = self.calculate_vaxed()

        bar_chart = ["Booster", "2nd Dose", "1st Dose"]
        percentages = [booster, second_dose, first_dose]

        # or shorter orientation = 'h'
        plt.bar(bar_chart, percentages, orientation="horizontal")
        plt.xticks([0, 25, 75, 100])
        plt.xlim(0, 100)
        plt.title("Vaccination Status")
        plt.clc()  # to remove colors
        plt.plotsize(60, 7)
        plt.show()

        input("\n Hit the enter key to return to main menu: ")
        #pause("Press any key to return to the main menu")
        self.main_menu()

    def add_new_patient(self):

        self.clear_display()
        print(colored(self.header("New Patient"), 'green'))

        are_you_sure = pyip.inputYesNo(
            "Are you sure you want to add a new user? Type Yes(Y) or No(N): ")
        if are_you_sure == 'no':
            self.main_menu()

        new_id = self.generate_new_id()

        firstname = pyip.inputStr('Enter First name\n')
        lastname = pyip.inputStr('Enter last name\n')

        day = pyip.inputInt(
            prompt="Enter day of birth... ", min=0, lessThan=31)
        month = pyip.inputInt(
            prompt="Enter amonth of birth ", min=0, lessThan=13)
        year = pyip.inputInt(prompt="Enter year of birth ",
                             min=0, lessThan=datetime.now().year)
        date_of_birth = str(day)+"/" + str(month)+"/" + str(year)

        first_dose = second_dose = booster = False
        first_dose_prompt = pyip.inputYesNo(
            "Has the patient had their first vaccine dose? Type Yes(Y) or No(N): ")

        if first_dose_prompt == "yes":
            first_dose = True
            second_dose_prompt = pyip.inputYesNo(
                "Has the patient had their second vaccine dose? Type Yes(Y) or No(N): ")
            if second_dose_prompt == "yes":
                second_dose = True
                booster_prompt = pyip.inputYesNo(
                    "Has the patient had their booster? Type Yes(Y) or No(N): ")
                if booster_prompt == "yes":
                    booster = True

        new_patient = Patient(new_id, firstname, lastname,
                              date_of_birth, first_dose, second_dose, booster)
        self.patient_list.append(new_patient)

        newdata = [new_id, firstname, lastname,
                   date_of_birth, first_dose, second_dose, booster]

        info = SHEET.worksheet('data')
        info.append_row(newdata)

        # need success condition, message

        self.main_menu()

    def generate_new_id(self):
        new_id = randint(100000, 999999)
        new_id_found = False
        while new_id_found is False:
            if(len([x for x in self.patient_list if (int(x.get_id()) == new_id)]) > 0):
                new_id = randint(100000, 999999)
            else:
                new_id_found = True

        return new_id

    def calculate_vaxed(self):

        firstdose = sum(1 for p in self.patient_list if p.first_dose == "TRUE")
        totalfirstdose = (firstdose/len(self.patient_list))*100

        seconddose = sum(
            1 for p in self.patient_list if p.second_dose == "TRUE")
        totalseconddose = (seconddose/len(self.patient_list))*100

        booster = sum(1 for p in self.patient_list if p.booster_dose == "TRUE")
        totalbooster = (booster/len(self.patient_list))*100

        return(totalfirstdose, totalseconddose, totalbooster)

    def show_guide(self):
        self.clear_display()
        print(colored(self.header("User Guide"), 'green'))

        print(
            'The Covid Vacination Manager allows you to keep track \n'
            'of the vaccination status of a list of patients \n'
            '\n'
            'You can view a list of all patients and see at a glance\n'
            'their status.'
            '\n You can also add new patients or update the status of \n'
            'current ones \n'
            'There is a dashboard which provides graphical representation\n'
            'of the entire patient body and allows you to compile lists'
            '\n of those most at risk'
            '\n'
            '\n'

        )
        input("Hit the enter key to return to the main menu: ")
        self.main_menu()

    def view_at_risk_patients(self):
        self.clear_display()
        # print(colored(self.header("*** At Risk Patients*** \n"), 'green'))
        print(colored("*** At Risk Patients ***\n", 'green'))

        # sort table here 

        patient_table = TableView(self.patient_list, 0)
        patient_table.print_table()
        
        viewing_page = True
        while viewing_page is True:

            if patient_table.page_number < 1:
                menu = ['Next Page', 'Main Menu']
            elif patient_table.page_number + 1 == patient_table.max_pages:
                menu = ['Previous Page', 'Main Menu']
            else:
                menu = ['Next Page', 'Previous Page', 'Main Menu']

            response = pyip.inputMenu(menu, numbered=True)

            if response == "Main Menu":
                print("here")
                viewing_page = False
            if response == "Next Page":
                self.clear_display()
                print(colored("*** At Risk Patients ***\n", 'green'))
                patient_table.page_number += 1
                patient_table.print_table()
            if response == "Previous Page":
                self.clear_display()
                print(colored("*** At Risk Patients ***\n", 'green'))
                patient_table.page_number -= 1
                patient_table.print_table()
            
        
        self.main_menu()

    def view_all_patients(self):
        self.clear_display()
        # print(colored(self.header("*** At Risk Patients*** \n"), 'green'))
        print(colored("*** View All Patients ***\n", 'green'))

        # sort table here 

        patient_table = TableView(self.patient_list, 0)
        patient_table.print_table()
        
        viewing_page = True
        while viewing_page is True:

            if patient_table.page_number < 1:
                menu = ['Next Page', 'Update Patient Details', 'Delete Patient', 'Main Menu']
            elif patient_table.page_number + 1 == patient_table.max_pages:
                menu = ['Previous Page', 'Update Patient Details', 'Delete Patient', 'Main Menu']
            else:
                menu = ['Next Page', 'Previous Page', 'Update Patient Details', 'Delete Patient','Main Menu']

            response = pyip.inputMenu(menu, numbered=True)

            if response == "Main Menu":
                print("here")
                viewing_page = False
            if response == "Next Page":
                self.clear_display()
                print(colored("*** View All Patients ***\n", 'green'))
                patient_table.page_number += 1
                patient_table.print_table()
            if response == "Previous Page":
                self.clear_display()
                print(colored("*** View All Patients ***\n", 'green'))
                patient_table.page_number -= 1
                patient_table.print_table()
            
        
        self.main_menu()
