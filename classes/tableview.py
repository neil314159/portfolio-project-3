from prettytable import PrettyTable

class TableView():
    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number
    
    def print_table(self):
        
        x = PrettyTable()
        x.field_names = ["First Name", "Last Name", "Age", "First Dose"]
        for a in self.patient_data[1:11]:
            # print(getattr(a, 'firstname'))
            x.add_row([getattr(a, 'firstname'), getattr(a, 'lastname'), a.age(), getattr(a, 'second_dose')])
        
        
        print("+" + ("-")*8 + "+" + ("-")*20 + "+" + ("-")*20 + "+" + ("-")*8 + "+" + ("-")*6 + "+" + ("-")*6 + "+" + ("-")*6 + "+")
        
        print(x)
        


    
    def next_page(self):
        page_number +=1

