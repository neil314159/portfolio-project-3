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



class Clinic:

    def __init__(self):
        self.main_menu()
    
    def main_menu(self):
        patient_list = load_patients()
    pb = return_progress_bar(20, "test")
    #print(pb)
    # response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
    os.system('clear')
    print(colored(welcome("View patients"), 'green'))

    #for a in patient_list:
    #    print(getattr(a, 'firstname'))

    #print(pb)
    mainmenu()