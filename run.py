import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
from datetime import datetime
import pyinputplus as pyip
import os
from classes.mixins import ManageDisplay

from classes.patient import Patient
from classes.progressbar import ProgressBar

colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cpm_data')



def show_instructions():
    os.system('clear')
    print(
            'The Covid Vacination Manager wallows you to keep track \n'
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
    mainmenu()

def return_progress_bar(progress, label):
    return "██████-------------- 40% complete"

def show_dashboard():
    os.system('clear')
    print('\n')
    print('\n')
    print('\n')
    print(return_progress_bar(20, "test"))
    print('\n')
    print('\n')
    print(return_progress_bar(20, "test"))
    print('\n')
    print('\n')
    print(return_progress_bar(20, "test"))
    print('\n')
    print('\n')
    mainmenu()

def load_patients():
    patient_list = []
    info = SHEET.worksheet('data')

    data = info.get_all_values()        
    #calculate_ages(data)
    
    for a in data:
        new_patient = Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
       # print(a[3])
        patient_list.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

    n = Patient(1, "neil", "Boland", "1/1/2000", True, True, False)
    #print(n.age())

    #for p in patient_list:
        #print(p.id)

    return patient_list

def mainmenu():
    response = pyip.inputMenu(['View Instructions', 'Add New Patient', 'Update Patient Details', 'View Dashboard'], numbered=True)
    if response == "View Instructions":
        show_instructions()
    if response == "View Dashboard":
        show_dashboard()

def main():
    patient_list = load_patients()
    pb = return_progress_bar(20, "test")
    print(pb)
    # response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
    #os.system('clear')
    print("""
       _____             _      _   _______                 _               
     / ____|            (_)    | | |__   __|               | |              
    | |      ___ __   __ _   __| |    | | _ __  __ _   ___ | | __ ___  _ __ 
    | |     / _ \\ \ / /| | / _` |    | || '__|/ _` | / __|| |/ // _ \| '__|
    | |____| (_) |\ V / | || (_| |    | || |  | (_| || (__ |   <|  __/| |   
     \_____|\___/  \_/  |_| \__,_|    |_||_|   \__,_| \___||_|\_\\___||_|   
                                                                            
                                                                            

                                                            
    """)

    #for a in patient_list:
    #    print(getattr(a, 'firstname'))


    #print(pb)
    mainmenu()








main()