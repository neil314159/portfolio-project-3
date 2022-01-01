from prettytable import PrettyTable

class TableView():
    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number
    
    def print_table(self):
        
        x = PrettyTable()
        x.field_names = ["Number", "First Name", "Last Name", "Age", "1st Dose", "2nd Dose", "Booster"]
        x._max_width = {"First Name":20, "Last Name":20 }
        
        for a in self.patient_data[1:]:
            # print(getattr(a, 'firstname'))
            new_row = []
            new_row.append(1234)
            new_row.append(getattr(a, 'firstname'))
            new_row.append(getattr(a, 'lastname'))
            new_row.append(a.age())
            

            new_row.append("✅") if((getattr(a, 'first_dose'))=="TRUE") else new_row.append("❌")
            new_row.append("✅") if((getattr(a, 'second_dose'))=="TRUE") else new_row.append("❌")
            new_row.append("✅") if((getattr(a, 'booster_dose'))=="TRUE") else new_row.append("❌")
           
            x.add_row(new_row)
        
        
        # print("+" + ("-")*8 + "+" + ("-")*20 + "+" + ("-")*20 + "+" + ("-")*8 + "+" + ("-")*6 + "+" + ("-")*6 + "+" + ("-")*6 + "+")
        
        # print(x)
        print(x.get_string(start=1,end=4))
        


    
    def next_page(self):
        page_number +=1

