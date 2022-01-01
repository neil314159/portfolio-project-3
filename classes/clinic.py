#class to manage entire app

import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
from datetime import datetime
import pyinputplus as pyip
import os
from termcolor import colored, cprint
from prettytable import PrettyTable
from pyfiglet import Figlet
from classes.patient import Patient
from classes.tableview import TableView
from random import randint

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
            patient_list2.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

        return patient_list2


    def welcome(self, text):
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
        print(colored(self.welcome("Patient Vaccine Tracker"), 'green'))
        response = pyip.inputMenu(['Guide', 'View At Risk Patients', 'View All Patients',
                                   'Enroll New Patient', 'View Progress Dashboard'], numbered=True)
        
        if response == "Guide":
            self.show_guide()
        if response == "View At Risk Patients":
            self.clear_display()
            new_table = TableView(self.patient_list, 0)
            new_table.print_table()
        if response == "View All Patients":
            self.clear_display()
            new_table = TableView(self.patient_list, 0)
            new_table.print_table()
        if response == "View Progress Dashboard":
            self.show_dashboard()
        if response == "Enroll New Patient":
            self.add_new_patient()
        
    def show_dashboard(self):     
        self.clear_display()
        one, two, three = self.calculate_vaxed()
        #print(one)
    
        print(colored(self.welcome(" Dashboard"), 'green'))

       

        pizzas = ["Booster", "2nd Dose", "1st Dose"]
        percentages = [71, 82, 92]

        plt.bar(pizzas, percentages, orientation = "horizontal") # or shorter orientation = 'h'
        plt.xticks([0,25,75,100])
        plt.xlim(0,100)
        plt.title("Vaccination Status")
        plt.clc() # to remove colors
        plt.plotsize(60, 7) # 4 = 1 for x numerical ticks + 2 for x axes + 1 for title
        plt.show()
    
        input("\n Hit enter key to return to main menu")
        #pause("Press any key to return to the main menu")
        self.main_menu()

    def add_new_patient(self):
        self.clear_display()
        
        are_you_sure = pyip.inputYesNo("Are you sure you want to add a new user? Type Yes(Y) or No(N): ")
        if are_you_sure == 'no': self.main_menu()
        
        new_id = self.generate_new_id()
    
        firstname = pyip.inputStr('Enter First name\n')
        lastname = pyip.inputStr('Enter last name\n')
        
        day = pyip.inputInt(prompt="Enter day of birth... ", min=0, lessThan=31)
        month = pyip.inputInt(prompt="Enter amonth of birth ", min=0, lessThan=13)
        year = pyip.inputInt(prompt="Enter year of birth ", min=0, lessThan=datetime.now().year)
        date_of_birth = str(day)+"/" + str(month)+"/" + str(year)

        first_dose = second_dose = booster = False
        first_dose_prompt = pyip.inputYesNo("Has the patient had their first vaccine dose? Type Yes(Y) or No(N): ")

        if first_dose_prompt == "yes":
            first_dose = True
            second_dose_prompt = pyip.inputYesNo("Has the patient had their second vaccine dose? Type Yes(Y) or No(N): ")
            if second_dose_prompt == "yes":
                second_dose = True
                booster_prompt = pyip.inputYesNo("Has the patient had their booster? Type Yes(Y) or No(N): ")
                if booster_prompt == "yes":
                    booster = True

        new_patient = Patient(new_id, firstname, lastname,
                            date_of_birth, first_dose, second_dose, booster)
        self.patient_list.append(new_patient)
        
        newdata = [new_id, firstname, lastname,
                            date_of_birth, first_dose, second_dose, booster]

        info = SHEET.worksheet('data')
        info.append_row(newdata)
        
        self.main_menu()
        
    def generate_new_id(self):
        new_id = randint(100000, 999999) 
        new_id_found = False
        while new_id_found == False:
            if(len([x for x in self.patient_list if (int(x.get_id()) == new_id)])>0):
                new_id = randint(100000, 999999) 
            else:
                new_id_found = True
        
        return new_id

    def calculate_vaxed(self):
            
        firstdose = 0
        for a in self.patient_list:
            if (getattr(a, 'first_dose')) == "TRUE":
                firstdose += 1

        totalfirstdose = (firstdose/len(self.patient_list))*100

        seconddose = 0
        for a in self.patient_list:
            if (getattr(a, 'second_dose')) == "TRUE":
                seconddose += 1

        totalseconddose = (seconddose/len(self.patient_list))*100

        booster = 0
        for a in self.patient_list:
            if (getattr(a, 'booster_dose')) == "TRUE":
                booster += 1

        totalbooster = (booster/len(self.patient_list))*100

        return(totalfirstdose, totalseconddose, totalbooster)

    def show_guide(self):
        self.clear_display()
        text = colored('Hello, World!', 'red', 'on_cyan')
        print(text)
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
        input("Hot enter key to return")
        self.main_menu()