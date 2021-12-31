import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
from datetime import date
import pyinputplus as pyip

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

class Patient:


    def __init__(self):
        self.firstname = "neil"
        self.lastname = "boland"
        self.dob = "1/2/1980"
        self.firstdose = "TRUE"
        self.seconddose = "TRUE"
        self.booster = "TRUE"

    def age(self):
        newdate = self.dob.split('/')
        days = newdate[0]
        months = newdate[1]
        years = newdate[2]
        

        datetime_str = '09/19/18'

        datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')
        return years



def main():
    info = SHEET.worksheet('data')

    data = info.get_all_values()        
    #calculate_ages(data)
    n = Patient()
    print(n.age())
   # response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
       

def calculate_ages(data):
   
    
    newdata = data[-1]
    print(newdata)




print("Welcome!")
main()