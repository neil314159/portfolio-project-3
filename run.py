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

from classes.clinic import Clinic






def welcome(text):
    result = Figlet()
    return result.renderText(text)


def show_instructions():
    os.system('clear')
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
    mainmenu()


def return_progress_bar(progress, label):

    return "     ██████-------------- " + label


def show_dashboard():
    os.system('clear')
    one, two, three = calculate_vaxed()
    #print(one)
    
    print(colored(welcome(" Dashboard"), 'green'))

    print('\n')
    print(return_progress_bar(20, "90% fully vaccinated"))

    print('\n')
    print(return_progress_bar(one, "80% first dose"))

    print('\n')
    print(return_progress_bar(two, "70% second dose"))

    print('\n')
    print(return_progress_bar(three, "60% have booster"))

    print('\n')
    
    input("\n Hit enter key to return to main menu")
    #pause("Press any key to return to the main menu")
    mainmenu()


def add_new_patient():
    #response = pyip.inputDate('Enter DOB', formats=('%d/%m/%y'))
    firstname = pyip.inputStr('Enter First name\n')
    lastname = pyip.inputStr('Enter last name\n')
    email = pyip.inputEmail('Enter email address:')
    day = pyip.inputInt(prompt="Enter day of birth... ", min=0, lessThan=31)
    month = pyip.inputInt(prompt="Enter amonth of birth ", min=0, lessThan=13)
    year = pyip.inputInt(prompt="Enter year of birth ", min=0, lessThan=2020)
    date_of_birth = str(day)+"/" + str(month)+"/" + str(year)
    new_patient = Patient(1, firstname, lastname,
                          date_of_birth, True, True, True)
    info = SHEET.worksheet('data')
    newdata = [1, firstname, lastname, date_of_birth, True, True, True]
    info.append_row(newdata)
    os.system('clear')
    mainmenu()
    #newpatient = Patient(


def load_patients():

    patient_list = []
    info = SHEET.worksheet('data')

    data = info.get_all_values()
    

    for a in data:
      
        patient_list.append(Patient(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))

    

    return patient_list


def calculate_vaxed():
    patient_list = load_patients()
    firstdose = 0
    for a in patient_list:
        if (getattr(a, 'first_dose')) == "TRUE":
            firstdose += 1

    totalfirstdose = (firstdose/len(patient_list))*100

    seconddose = 0
    for a in patient_list:
        if (getattr(a, 'second_dose')) == "TRUE":
            seconddose += 1

    totalseconddose = (seconddose/len(patient_list))*100

    booster = 0
    for a in patient_list:
        if (getattr(a, 'booster_dose')) == "TRUE":
            booster += 1

    totalbooster = (booster/len(patient_list))*100

    return(totalfirstdose, totalseconddose, totalbooster)


def mainmenu():
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


if __name__ == '__main__':
    # patient_list = load_patients()
    # os.system('clear')
    # mainmenu()
    manager = Clinic()


