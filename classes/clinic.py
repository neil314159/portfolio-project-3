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

# Used Code Institute tutorial code to connect to Google Sheets API
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
    """ Main class which handles all menus and data
    operations. Uses a list of Patients and can update
    data back to Google Sheets.
    """
    def load_patients(self):
        """ Gets all values from Google Sheets and
        stores them in a list.
        """
        try:
            patient_list = []
            info = SHEET.worksheet('data')
            data = info.get_all_values()
        except:
            print("Something went wrong loading the database.")
        # Gives an index that reflects the position in spreadsheet
        for index, a in enumerate(data):
            patient_list.append(
                Patient(a[0], index+1, a[1], a[2], a[3], a[4], a[5], a[6]))

        return patient_list

    def header(self, text):
        """ Converts text into a large ASCII code
        representation for page headers.
        """
        result = Figlet()
        return result.renderText(text)

    def clear_display(self):
        """ Clears screen after menu operations.
        """
        os.system('clear')

    def __init__(self):
        """ List of patients are loaded in
        when the object is constructed.
        """
        self.patient_list = self.load_patients()
        self.clear_display()
        self.main_menu()

    def main_menu(self):
        """ Presents main menu to user, this
        function is called when other operations
        are finished.
        """
        self.clear_display()
        print(colored(self.header("Vaccine Clinic Tracker"), 'green'))
        # 3rd Party library used for input validation on menu
        response = pyip.inputMenu(['Guide', 'View At Risk Patients',
                                   'View All Patients',
                                   'Enroll New Patient',
                                   'View Progress Dashboard'], numbered=True)

        if response == "Guide":
            self.show_guide()
        if response == "View At Risk Patients":
            self.view_at_risk_patients()
        if response == "View All Patients":
            self.view_all_patients()
        if response == "View Progress Dashboard":
            self.show_dashboard()
        if response == "Enroll New Patient":
            self.add_new_patient()

    def show_dashboard(self):
        """ Shows a bar chart of overall vaccination levels
        among all patients, listing first, second and booster doses.
        Uses a 3rd party library to output chart.
        """
        self.clear_display()
        print(colored(self.header("Dashboard"), 'green'))
        # Get total numbers calculated
        first_dose, second_dose, booster = self.calculate_vaxed()
        # Create chart
        bar_chart = ["Booster", "2nd Dose", "1st Dose"]
        percentages = [booster, second_dose, first_dose]
        # Set parameters for chart output, based on plotext docs
        plt.bar(bar_chart, percentages, orientation="horizontal")
        plt.xticks([0, 25, 75, 100])
        plt.xlim(0, 100)
        plt.title("Vaccination Status")
        plt.clc()
        plt.plotsize(60, 7)
        plt.show()

        input("\n Hit the enter key to return to main menu: ")
        self.main_menu()

    def add_new_patient(self):
        """ Gets input from user and creates
        a new Patient in the system.
        """
        self.clear_display()
        print(colored(self.header("New Patient"), 'green'))
        # Validated user input
        are_you_sure = pyip.inputYesNo(
            "Are you sure you want to add a new user? "
            "Type Yes (Y) or No (N): ")
        if are_you_sure == 'no':
            self.main_menu()

        # Create unique new ID
        new_id = self.generate_new_id()

        firstname = pyip.inputStr('Enter First name\n')
        lastname = pyip.inputStr('Enter Last name\n')

        day = pyip.inputInt(
            prompt="Enter day of birth... ", min=0, lessThan=31)
        month = pyip.inputInt(
            prompt="Enter month of birth ", min=0, lessThan=13)
        year = pyip.inputInt(prompt="Enter year of birth ",
                             min=0, lessThan=datetime.now().year)
        date_of_birth = str(day)+"/" + str(month)+"/" + str(year)

        first_dose = second_dose = booster = False
        first_dose_prompt = pyip.inputYesNo(
            "Has the patient had their first dose? Type Yes(Y) or No(N): ")

        if first_dose_prompt == "yes":
            first_dose = True
            second_dose_prompt = pyip.inputYesNo(
                "Has the patient had their second dose? "
                "Type Yes(Y) or No(N): ")
            if second_dose_prompt == "yes":
                second_dose = True
                booster_prompt = pyip.inputYesNo(
                    "Has the patient had their booster?"
                    " Type Yes (Y) or No (N): ")
                if booster_prompt == "yes":
                    booster = True
        try:
            # Add new Patient object to user list
            new_patient = Patient(new_id, len(self.patient_list)+1,
                                  firstname, lastname,
                                  date_of_birth, str(first_dose).upper(),
                                  str(second_dose).upper(),
                                  str(booster).upper())
            self.patient_list.append(new_patient)

            # Construct data and add to Google Sheet
            newdata = [new_id, firstname, lastname,
                       date_of_birth, first_dose, second_dose, booster]
            info = SHEET.worksheet('data')
            info.append_row(newdata)
            input("New patient added! Hit the enter "
                  "key to return to the main menu: ")
        except:
            input("Something went wrong! Hit the enter "
                  "key to return to the main menu: ")

        self.main_menu()

    def generate_new_id(self):
        """ Generates a new 6-digit Patient ID number.
        Checks for uniqueness against existing ID numbers.
        """
        new_id = randint(100000, 999999)
        new_id_found = False
        while new_id_found is False:
            # Compiles a list of all matching IDs and checks it's length
            if(len([x for x in self.patient_list if (
               int(x.get_id()) == new_id)]) > 0):
                new_id = randint(100000, 999999)
            else:
                new_id_found = True

        return new_id

    def calculate_vaxed(self):
        """ Calculates total vaccination levels
        for all patients in database. This data is
        used in the bar chart on the dashboard page.
        It sums the Booleans over all users.
        """

        firstdose = sum(1 for p in self.patient_list if p.first_dose == "TRUE")
        totalfirstdose = (firstdose/len(self.patient_list))*100

        seconddose = sum(
            1 for p in self.patient_list if p.second_dose == "TRUE")
        totalseconddose = (seconddose/len(self.patient_list))*100

        booster = sum(1 for p in self.patient_list if p.booster_dose == "TRUE")
        totalbooster = (booster/len(self.patient_list))*100

        return(totalfirstdose, totalseconddose, totalbooster)

    def show_guide(self):
        """ Presents list of instructions to user
        """
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
        """ Presents a view of all patients sorted by those
        most at risk. They are ordered first by number of vaccinations
        received and then by age. No vaccines are highlighted in coloured
        text for emphasis.
        """
        self.clear_display()
        print(colored("*** At Risk Patients ***\n", 'green'))

        # sort table here
        self.patient_list.sort(key=lambda x: x.age(), reverse=True)
        self.patient_list.sort(key=lambda x: (
            x.first_dose + x.second_dose + x.booster_dose))

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
        """ Shows all patients sorted alphabetically,
        allows for users to be updated and deleted.
        Multiple pages of results can be clicked through.
        """
        self.clear_display()
        print(colored("*** View All Patients ***\n", 'green'))

        # sort table here
        self.patient_list.sort(key=lambda x: x.lastname)

        patient_table = TableView(self.patient_list, 0)
        patient_table.print_table()

        viewing_page = True
        while viewing_page is True:

            if patient_table.page_number < 1:
                menu = ['Next Page', 'Update Vaccination Status',
                        'Delete Patient', 'Main Menu']
            elif patient_table.page_number + 1 == patient_table.max_pages:
                menu = ['Previous Page', 'Update Vaccination Status',
                        'Delete Patient', 'Main Menu']
            else:
                menu = ['Next Page', 'Previous Page',
                        'Update Vaccination Status',
                        'Delete Patient', 'Main Menu']
            # Different menu shown depending on first/last page
            response = pyip.inputMenu(menu, numbered=True)

            if response == "Main Menu":
                viewing_page = False
            if response == "Next Page":
                self.clear_display()
                print(colored("*** View All Patients ***\n", 'green'))
                patient_table.page_number += 1
                patient_table.print_table()
            if response == "Delete Patient":
                self.delete_patient(patient_table)
            if response == "Update Vaccination Status":
                self.update_patient_status(patient_table)
            if response == "Previous Page":
                self.clear_display()
                print(colored("*** View All Patients ***\n", 'green'))
                patient_table.page_number -= 1
                patient_table.print_table()

        self.main_menu()

    def update_patient_status(self, patient_table):
        """ If a Patient has been vaccinated
        this allows their status to be updated
        in the database.
        """
        self.clear_display()
        print(colored("*** View All Patients ***\n", 'green'))
        patient_table.print_table()
        are_you_sure = pyip.inputYesNo(
                    "Are you sure you want to update a patient's status?"
                    " Type Yes(Y) or No(N): ")
        if are_you_sure == 'no':
            self.main_menu()

        # Get reference from screen of user to update
        update = pyip.inputInt(
                                  prompt="Enter the number of the "
                                  "patient you want to update: ",
                                  min=1, lessThan=len(self.patient_list)+1)

        first_dose = second_dose = booster = False
        # Nested if's since each dose depends on previous one
        first_dose_prompt = pyip.inputYesNo(
            "Has the patient had their first dose? Type Yes(Y) or No(N): ")
        if first_dose_prompt == "yes":
            first_dose = True
            second_dose_prompt = pyip.inputYesNo(
                "Has the patient had their second dose? "
                "Type Yes(Y) or No(N): ")
            if second_dose_prompt == "yes":
                second_dose = True
                booster_prompt = pyip.inputYesNo(
                    "Has the patient had their booster? "
                    "Type Yes(Y) or No(N): ")
                if booster_prompt == "yes":
                    booster = True

        try:
            # Use string of boolean to be compatible with Google Sheets
            self.patient_list[update-1].first_dose = str(first_dose).upper()
            self.patient_list[update-1].second_dose = str(second_dose).upper()
            self.patient_list[update-1].booster_dose = str(booster).upper()

            data = SHEET.worksheet('data')
            data.update_cell(self.patient_list[int(update)-1].sheet_index,
                             5, str(first_dose).upper())
            data.update_cell(self.patient_list[int(update)-1].sheet_index,
                             6, str(second_dose).upper())
            data.update_cell(self.patient_list[int(update)-1].sheet_index,
                             7, str(booster).upper())

            input("The update was successful! Hit the "
                  "enter key to return to the main menu: ")
        except:
            input("There was a problem updating the user. Hit the "
                  "enter key to return to the main menu: ")
        self.main_menu()

    def delete_patient(self, patient_table):
        """ Removes patient from list
        of users and also deletes their
        record from Google Sheets.
        """
        self.clear_display()
        # Menu reprinted so user can see the ID they want to delete
        print(colored("*** View All Patients ***\n", 'green'))
        patient_table.print_table()
        are_you_sure = pyip.inputYesNo(
               "Are you sure you want to delete a patient from"
               " the system? Type Yes (Y) or No (N): ")
        if are_you_sure == 'no':
            self.main_menu()
        # Takes on screen reference and links to the Patient object
        to_delete = pyip.inputInt(
            prompt="Enter the number of the patient you want to delete: ",
            min=1, lessThan=len(self.patient_list)+1)
        try:
            # Row is deleted from Google Sheets
            info = SHEET.worksheet('data')
            info.delete_row(
                            self.patient_list[int(to_delete)-1].sheet_index)
            # Object deleted from user list
            del self.patient_list[int(to_delete)-1]
            input("Deletion was successful! Hit "
                  "the enter key to return to the main menu: ")
        except:
            input("Something went wrong! Hit the "
                  "enter key to return to the main menu: ")
        self.main_menu()
