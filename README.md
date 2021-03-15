# Attendance
#### PURPOSE:
This program enables students to use a unique four-digit code provided by a faculty member in each lecture to sign into that particular course and cohort each day. 

#### REQUIREMENTS
* Create a Google Sheet dedicated to the program 
* Obtain and install Google Sheets API credentials in a .JSON file through https://console.cloud.google.com 
* Obtain client email from credentials file
* Share created Google Sheet with and give editing privileges to the client email
* Fill out google sheet deatils in 'sheets.py' code in 'faculty' folder
```
pip3 install -r requirements.txt

```


#### PROCESS 
##### For Faculty under ‘faculty’ folder: 
###### 
* Run ‘codeGen.py’  
* Give out class code 
*	Run ‘summary.py’ at end of class to generate text files with names of absent and present students.
*	Run ‘reset.py’ to reset system
 
##### For Student under ‘student’ folder: 
* Run ‘Login.py’ 
