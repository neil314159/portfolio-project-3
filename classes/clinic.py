#class to manage entire app

import gspread
from google.oauth2.service_account import Credentials

import plotext as plt


from datetime import datetime
import pyinputplus as pyip
import os
from classes.mixins import ManageDisplay
from termcolor import colored, cprint
from prettytable import PrettyTable

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
            patient_list2.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

        return patient_list2


    def welcome(self, text):
        result = Figlet()
        return result.renderText(text)
    
    def clear_display(self):
        os.system('clear')

    def __init__(self):
        self.patient_list = self.load_patients()
        os.system('clear')
        
        self.main_menu()
    
    



    def main_menu(self):
        self.clear_display()
        print(colored(self.welcome("Patient Vaccine Tracker"), 'green'))
        response = pyip.inputMenu(['Guide', 'View At Risk Patients', 'View All Patients',
                                   'Enroll New Patient', 'View Progress Dashboard'], numbered=True)
        if response == "Home":
            self.clear_display()
            print(self.welcome("covid! "))

            #calculate_vaxed()
            mainmenu()

        if response == "Guide":
            show_instructions()
        if response == "View Progress Dashboard":
            self.show_dashboard()
        if response == "Add New Patient":
            add_new_patient()
        if response == "View All Patients":
            self.clear_display()

            new_table = TableView(self.patient_list, 0)
            new_table.print_table()

    def show_dashboard(self):     
        os.system('clear')
        # one, two, three = calculate_vaxed()
        #print(one)
    
        print(colored(self.welcome(" Dashboard"), 'green'))

        # print('\n')
        # print(return_progress_bar(20, "90% fully vaccinated"))

        # print('\n')
        # print(return_progress_bar(one, "80% first dose"))

        # print('\n')
        # print(return_progress_bar(two, "70% second dose"))



        # print('\n')
        # print(return_progress_bar(three, "60% have booster"))

        # print('\n')

        pizzas = ["Booster", "2nd Dose", "1st Dose"]
        percentages = [71, 82, 92]

        plt.bar(pizzas, percentages, orientation = "horizontal") # or shorter orientation = 'h'
        plt.xticks([0,25,75,100])
        plt.xlim(0,100)
        plt.title("Vaccination Status")
        # plt.clc() # to remove colors
        plt.plotsize(60, 7) # 4 = 1 for x numerical ticks + 2 for x axes + 1 for title
        plt.show()


        
 
#
    
        input("\n Hit enter key to return to main menu")
        #pause("Press any key to return to the main menu")
        self.main_menu()
