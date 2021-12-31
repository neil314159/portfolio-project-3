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
    mainmenu()

def return_progress_bar(progress, label):

    return "     ██████-------------- " + label

def show_dashboard():
    os.system('clear')
    one, two, three = calculate_vaxed()
    #print(one)
    
    print('\n')
    print(return_progress_bar(20, "90% fully vaccinated"))
   
    print('\n')
    print(return_progress_bar(one, "80% first dose"))
    
    print('\n')
    print(return_progress_bar(two, "70% second dose"))
   
    print('\n')
    print(return_progress_bar(three, "60% have booster"))
    
    print('\n')
    mainmenu()

def add_new_patient():
    #response = pyip.inputDate('Enter DOB', formats=('%d/%m/%y'))
    firstname = pyip.inputStr('Enter First name\n')
    lastname = pyip.inputStr('Enter last name\n')
    email = pyip.inputEmail('Enter email address:')
    day = pyip.inputInt(prompt = "Enter day of birth... ", min = 0, lessThan = 31)
    month = pyip.inputInt(prompt = "Enter amonth of birth ", min = 0, lessThan = 13)
    year = pyip.inputInt(prompt = "Enter year of birth ", min = 0, lessThan = 2020)
    print(firstname, lastname)

    os.system('clear')
    mainmenu()
    #newpatient = Patient(

def load_patients():
    patient_list = []
    info = SHEET.worksheet('data')

    data = info.get_all_values()        
    #calculate_ages(data)
    
    for a in data:
        #new_patient = Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
       # print(a[3])
        patient_list.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

    #n = Patient(1, "neil", "Boland", "1/1/2000", True, True, False)
    
    return patient_list

def calculate_vaxed():
    patient_list = load_patients()
    firstdose = 0
    for a in patient_list:
        if (getattr(a, 'first_dose')) == "TRUE":
            firstdose +=1

    totalfirstdose = (firstdose/len(patient_list))*100

    seconddose = 0
    for a in patient_list:
        if (getattr(a, 'second_dose')) == "TRUE":
            seconddose +=1

    totalseconddose = (seconddose/len(patient_list))*100

    booster = 0
    for a in patient_list:
        if (getattr(a, 'booster_dose')) == "TRUE":
            booster +=1

    totalbooster = (booster/len(patient_list))*100

    return(totalfirstdose, totalseconddose, totalbooster)


def mainmenu():
    response = pyip.inputMenu(['Home', 'View Patients', 'Add New Patient', 'Update Patient Details', 'View Dashboard', 'View Instructions'], numbered=True)
    if response == "Home":
        os.system('clear')
        print("""
       _____             _      _   _______                 _               
      / ____|            (_)    | | |__   __|               | |              
    | |      ___ __   __ _   __| |    | | _ __  __ _   ___ | | __ ___  _ __ 
    | |     / _ \\ \ / /| | / _` |    | || '__|/ _` | / __|| |/ // _ \| '__|
    | |____| (_) |\ V / | || (_| |    | || |  | (_| || (__ |   <|  __/| |   
     \_____|\___/  \_/  |_| \__,_|    |_||_|   \__,_| \___||_|\_\\___||_|   
                                                                            
                                                                            

                                                            
        """)
        #calculate_vaxed()
        mainmenu()
    
    if response == "View Instructions":
        show_instructions()
    if response == "View Dashboard":
        show_dashboard()
    if response == "Add New Patient":
        add_new_patient()
    if response == "View Patients":
        os.system('clear')
        a="""
+─────────────+─────────────+────────────────+──────────+───────────+──────────+
| First Name  | Last Name   | Date of birth  | 1st Dose | 2nd Dose  | Booster  |
+─────────────+─────────────+────────────────+──────────+───────────+──────────+
| Lewiss      | Falk           | 27/04/1936  |    ✅    | TRUE    | FALSE    |
| Angelia     | Gleader        | 29/06/1945  |    ✅    | TRUE    | TRUE     |
| Rudd        | Howorth        | 14/06/1967  |    ✅    | TRUE    | TRUE     |
| Maryjane    | Carolan        | 30/12/1989  |    ✅    | TRUE    | TRUE     |
| Glenda      | McPhelimey     | 16/03/1993  | TRUE     | TRUE    | TRUE     |
| Alexis      | MacMarcuis     | 21/08/1923  | TRUE     | TRUE    | TRUE     |
| Griffie     | Pero           | 26/11/1982  | TRUE     | TRUE    | TRUE     |
| Moria       | Van der Merwe  | 17/09/1951  | FALSE    | TRUE    | TRUE     |
| Lamont      | Crevagh        | 15/03/2000  | TRUE     | FALS    | FALSE    |
+─────────────+─────────────+────────────────+──────────+───────────+──────────+
"""

        print(a)
        mainmenu()

def main():
    patient_list = load_patients()
    pb = return_progress_bar(20, "test")
    #print(pb)
    # response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
    os.system('clear')
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