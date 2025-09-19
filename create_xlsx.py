
import pandas as pd
import os

def take_user_data():
    name = input('Enter your name: ')
    roll_number = input('Enter your roll number: ')
    class_name = input('Enter your class name: ')
    total_fees = input('Enter your total fees: ')
    balance = input('Enter your balance: ')
    print("Data Added Successfully")
    return name, roll_number, class_name, total_fees, balance





class StudentData:
    def __init__(self,name,roll_number,class_name,total_fees,balance):
        self.name = name
        self.roll_number = roll_number
        self.class_name = class_name
        self.total_fees = total_fees
        self.balance = balance

    def add_profile(self):
        data_set = pd.DataFrame([{
            'Name': self.name,
            'Roll Number': self.roll_number,
            'Class Name': self.class_name,
            'Total Fees': self.total_fees,
            'Balance': self.balance
        }])
        return data_set
    @staticmethod
    def update_excel(data_set_new, filename="student_data.xlsx"):
        if os.path.exists(filename):
            # Read Existing file
            df_existing = pd.read_excel(filename)
            # Append New Data
            df_combined = pd.concat([df_existing,data_set_new], ignore_index=True)
        else:
            df_combined = data_set_new
        df_combined.to_excel(filename, sheet_name="Students", index=False)
        print("Data saved to Excel successfully")


if __name__ == "__main__":
    user_data = take_user_data()
    student = StudentData(*user_data)
    new_df = student.add_profile()
    StudentData.update_excel(new_df)






