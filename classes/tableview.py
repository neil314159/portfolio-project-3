class TableView():
    def __init__(self, patient_data, page_number):
        self.patient_data = patient_data
        self.page_number = page_number
    
    def print_table(self):
        print(self.patient_data[1].age())
    
    def next_page(self):
        page_number +=1

