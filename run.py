import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
from datetime import datetime
import pyinputplus as pyip
import os

from classes.patient import Patient

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



class ProgressBar:
    def __init__(self):
        self.percent_complete = 1
    
    def print_progress():
        #
        return ""

def main():
    patient_list = load_patients()
   
    # response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
    #os.system('clear')
    print("""
      _____              _      _    _____        _    _               _   
     / ____|            (_)    | |  |  __ \      | |  (_)             | |  
    | |      ___ __   __ _   __| |  | |__) |__ _ | |_  _   ___  _ __  | |_ 
    | |     / _ \\ \ / /| | / _` |  |  ___// _` || __|| | / _ \| '_ \ | __|
    | |____| (_) |\ V / | || (_| |  | |   | (_| || |_ | ||  __/| | | || |_ 
     \_____|\___/  \_/  |_| \__,_|  |_|    \__,_| \__||_| \___||_| |_| \__|
                                                                           
                                                                           
                    _______                 _               
                   |__   __|               | |              
                      | | _ __  __ _   ___ | | __ ___  _ __ 
                      | || '__|/ _` | / __|| |/ // _ \| '__|
                      | || |  | (_| || (__ |   <|  __/| |   
                      |_||_|   \__,_| \___||_|\_\\___||_|   
                                                            
                                                            
    """)
       

def load_patients():
    patient_list = []
    info = SHEET.worksheet('data')

    data = info.get_all_values()        
    #calculate_ages(data)
    
    for a in data:
        #new_patient = Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        patient_list.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

    #n = Patient(1, "neil", "Boland", "1/1/2000", True, True, False)
    # print(n.age())

    #for p in patient_list:
        #print(p.id)

    return patient_list





print("Welcome!")
main()