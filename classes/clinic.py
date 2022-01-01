#class to manage entire app

import gspread
from google.oauth2.service_account import Credentials

from datetime import datetime
import pyinputplus as pyip
import os
from classes.mixins import ManageDisplay
from termcolor import colored, cprint
from prettytable import PrettyTable

from pyfiglet import Figlet
from classes.patient import Patient
from classes.progressbar import ProgressBar

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

    def __init__(self):
        self.patient_list = self.load_patients()
        os.system('clear')
        
        self.main_menu()
    
    



    def main_menu(self):

        print(colored(self.welcome(" Covid Vaccine Manager"), 'green'))
        response = pyip.inputMenu(['Guide', 'View At Risk Patients', 'View All Patients',
                                   'Enroll New Patient', 'View Progress Dashboard'], numbered=True)
        if response == "Home":
            os.system('clear')
        print(welcome("covid! "))

        #calculate_vaxed()
        mainmenu()

        if response == "Guide":
            show_instructions()
        if response == "View Progress Dashboard":
            show_dashboard()
        if response == "Add New Patient":
            add_new_patient()
        if response == "View All Patients":
            os.system('clear')

            x = PrettyTable()
            x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
            x.add_row(["Adelaide", 1295, 1158259, 600.5])
            x.add_row(["Brisbane", 5905, 1857594, 1146.4])
            x.add_row(["Darwin", 112, 120900, 1714.7])
            x.add_row(["Hobart", 1357, 205556, 619.5])
            x.add_row(["Sydney", 2058, 4336374, 1214.8])
            x.add_row(["Melbourne", 1566, 3806092, 646.9])
            x.add_row(["Perth", 5386, 1554769, 869.4])

            print(x)
            mainmenu()
