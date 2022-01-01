from prettytable import PrettyTable
from termcolor import colored, cprint
from tabulate import tabulate

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
            

            new_row.append("YES") if((getattr(a, 'first_dose'))=="TRUE") else new_row.append(colored("NO", 'red', 'on_cyan'))
            new_row.append("YES") if((getattr(a, 'second_dose'))=="TRUE") else new_row.append("N")
            new_row.append("YES") if((getattr(a, 'booster_dose'))=="TRUE") else new_row.append("N")
           
            x.add_row(new_row)
        
        
        # print("+" + ("-")*8 + "+" + ("-")*20 + "+" + ("-")*20 + "+" + ("-")*8 + "+" + ("-")*6 + "+" + ("-")*6 + "+" + ("-")*6 + "+")
        table = [["✅",696000,1989100000],["Earth",6371,5973.6],
                 ["Moon",1737,73.5],["Mars",3390,641.85]]
        headers = ["item", "qty"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))
        print(x)
        #print(x.get_string(start=1,end=6))
        


    
    def next_page(self):
        page_number +=1

