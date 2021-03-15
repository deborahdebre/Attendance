#Importing 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

#Creating connection to google sheet and global variable "sheet"
def sheet_data():
    scope=[  "https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope) # Replace credentials.json with name of credentials file
    client = gspread.authorize(creds)

    global sheet
    sheet = client.open("Name of Google Sheet").sheet1 #Put name of google sheet as the parameter
    
#Returning values in column 1
    result = sheet.col_values(1)
    result.append(sheet.col_values(3))
    return result
def sheet_update (email):
    posFinder = sheet_data()
    index=posFinder.index(email)
    pos = index +1
    sheet.update_cell(pos,2,"present")
    
    
#Creating  empty lists for different statuses
def status():
    present= []
    absent= []
    
    
#Checking status of student by looping through emails in database
    data = sheet_data()
    for email in data:
        position = data.index(email)
        
#Appending to different lists based on status
        if sheet.cell(position+1,2).value == "absent":
            absent.append(email)
            
        elif sheet.cell(position+1,2).value == "present":
                present.apppend(email)

        
#Appending to different text files based on status
 #Present
    f1 = open ("present.txt","w")
    for name in present:
        f1.write(name+'\n')
    f1.close()

#Absent
    f2 = open ("absent.txt","w")
    for name in absent:
         f2.write(name+'\n')
    f2.close()
    
#Updating code in cells
def code_updater(code):
    sheet_data()
    sheet.update_cell(1,3,code)
    
#Looping through the emails and return everyone to absent at the end of the class
def reset():
    data = sheet_data()
    for email in data:
        position = data.index(email)
        sheet.update_cell(position+1,2,"absent")



