from prettytable import PrettyTable
from termcolor import colored, cprint
from tabulate import tabulate
from rich.table import Table
from rich import print

class TableView():
    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number
    
    def print_table(self):
        
        x = PrettyTable()
        x.field_names = ["Number", "First Name", "Last Name", "Age", "Dose 1", "Dose 2", "Booster"]
        x._max_width = {"First Name":20, "Last Name":20 }
        
        for a in self.patient_data[1:11]:
            # print(getattr(a, 'firstname'))
            new_row = []
            new_row.append(1234)
            new_row.append(getattr(a, 'firstname'))
            new_row.append(getattr(a, 'lastname'))
            new_row.append(a.age())
            

            new_row.append("YES") if((getattr(a, 'first_dose'))=="TRUE") else new_row.append("NO")
            new_row.append("YES") if((getattr(a, 'second_dose'))=="TRUE") else new_row.append("N")
            new_row.append("YES") if((getattr(a, 'booster_dose'))=="TRUE") else new_row.append("N")
           
            x.add_row(new_row)
        
        
        # print("+" + ("-")*8 + "+" + ("-")*20 + "+" + ("-")*20 + "+" + ("-")*8 + "+" + ("-")*6 + "+" + ("-")*6 + "+" + ("-")*6 + "+")
        

        table = Table(title="Star Wars Movies")

        table.add_column("Released", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Box Office", justify="right", style="green")

        table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
        table.add_row("May 25, 2018", "✅", "$393,151,347")
        table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
        table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

        print(table)
       
        print(x)
        #print(x.get_string(start=1,end=6))
        


    
    def next_page(self):
        page_number +=1

