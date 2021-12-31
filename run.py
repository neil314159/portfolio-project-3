import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style

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



def main():
    info = SHEET.worksheet('data')

    data = info.get_all_values()        

    response = pyip.inputEmail()
       

   

print("Welcome!")
main()