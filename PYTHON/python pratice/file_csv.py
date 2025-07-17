#getting open csv file
# EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,JOB_ID,SALARY,DEPARTMENT_ID
# 103,Alexander,Hunold,AHUNOLD,IT_PROG,9000,60
# 104,Bruce,Ernst,BERNST,IT_PROG,6000,60
# 105,David,Austin,DAUSTIN,IT_PROG,4800,60
data = open("textfile\\employees_adm.csv", "r")
s=data.read()
print(type(s))
print(s) #csv format

import csv
data = open("textfile\\employees_adm.csv", "r")
f = csv.reader(data)

for r in f:
    print(r) #list format with csv type is str
print(type(r))

data = open("textfile\\employees_adm.csv", "r")
f = csv.DictReader(data)

for r in f:
    print(r) #dict format with csv type is str
print(type(r))

#this for single row insertion in file list type
with open("textfile\\emp1.csv", 'w') as f:
    w = csv.writer(f)
    b = w.writerow(['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','JOB_ID','SALARY','DEPARTMENT_ID'])
    # w.writerow(['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','JOB_ID','SALARY'])
    # print(b)

#this is for multiple rows insertion list type
with open("textfile\\emp1.csv", 'w') as f:
    w = csv.writer(f)
    b = w.writerows((['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','JOB_ID','SALARY','DEPARTMENT_ID'],
                    ['103','Alexander','Hunold','AHUNOLD','IT_PROG','9000','60'],
                    ['104','Bruce','Ernst','BERNST','IT_PROG','6000','60'],
                    ['105','David','Austin','DAUSTIN','IT_PROG','4800','60']
                    ))
#this based on dict type multirows insertion    
with open("textfile\\emp1.csv", 'w') as p:
    g= csv.DictWriter(p, fieldnames=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY','COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID'])
    g.writeheader() #it will take header by this function
    g.writerows((
        # {'EMPLOYEE_ID':'EMPLOYEE_ID','FIRST_NAME':'FIRST_NAME','LAST_NAME':'LAST_NAME','EMAIL':'EMAIL','PHONE_NUMBER':'PHONE_NUMBER','HIRE_DATE':'HIRE_DATE','JOB_ID':'JOB_ID','SALARY':'SALARY','COMMISSION_PCT':'COMMISSION_PCT','MANAGER_ID':'MANAGER_ID','DEPARTMENT_ID':'DEPARTMENT_ID'},
        {'EMPLOYEE_ID': '100', 'FIRST_NAME': 'Steven', 'LAST_NAME': 'King', 'EMAIL': 'SKING', 'PHONE_NUMBER': '515.123.4567', 'HIRE_DATE': '17-Jun-03', 'JOB_ID': 'AD_PRES', 'SALARY': '24000', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': ' - ', 'DEPARTMENT_ID': '90'},
        {'EMPLOYEE_ID': '101', 'FIRST_NAME': 'Neena', 'LAST_NAME': 'Kochhar', 'EMAIL': 'NKOCHHAR', 'PHONE_NUMBER': '515.123.4568', 'HIRE_DATE': '21-Sep-05', 'JOB_ID': 'AD_VP', 'SALARY': '17000', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '100', 'DEPARTMENT_ID': '90'},
        {'EMPLOYEE_ID': '102', 'FIRST_NAME': 'Lex', 'LAST_NAME': 'De Haan', 'EMAIL': 'LDEHAAN', 'PHONE_NUMBER': '515.123.4569', 'HIRE_DATE': '13-Jan-01', 'JOB_ID': 'AD_VP', 'SALARY': '17000', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '100', 'DEPARTMENT_ID': '90'},
        {'EMPLOYEE_ID': '103', 'FIRST_NAME': 'Alexander', 'LAST_NAME': 'Hunold', 'EMAIL': 'AHUNOLD', 'PHONE_NUMBER': '590.423.4567', 'HIRE_DATE': '03-Jan-06', 'JOB_ID': 'IT_PROG', 'SALARY': '9000', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '102', 'DEPARTMENT_ID': '60'},
        {'EMPLOYEE_ID': '104', 'FIRST_NAME': 'Bruce', 'LAST_NAME': 'Ernst', 'EMAIL': 'BERNST', 'PHONE_NUMBER': '590.423.4568', 'HIRE_DATE': '21-May-07', 'JOB_ID': 'IT_PROG', 'SALARY': '6000', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '103', 'DEPARTMENT_ID': '60'}
        ))
    
#this will append the data
with open("textfile\\emp1.csv", 'a') as p:
    g= csv.DictWriter(p, fieldnames=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY','COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID'])
    # g.writeheader() #it will take header by this function
    g.writerows((
        {'EMPLOYEE_ID': '105', 'FIRST_NAME': 'David', 'LAST_NAME': 'Austin', 'EMAIL': 'DAUSTIN', 'PHONE_NUMBER': '590.423.4569', 'HIRE_DATE': '25-Jun-05', 'JOB_ID': 'IT_PROG', 'SALARY': '4800', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '103', 'DEPARTMENT_ID': '60'},
{'EMPLOYEE_ID': '106', 'FIRST_NAME': 'Valli', 'LAST_NAME': 'Pataballa', 'EMAIL': 'VPATABAL', 'PHONE_NUMBER': '590.423.4560', 'HIRE_DATE': '05-Feb-06', 'JOB_ID': 'IT_PROG', 'SALARY': '4800', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '103', 'DEPARTMENT_ID': '60'},
{'EMPLOYEE_ID': '107', 'FIRST_NAME': 'Diana', 'LAST_NAME': 'Lorentz', 'EMAIL': 'DLORENTZ', 'PHONE_NUMBER': '590.423.5567', 'HIRE_DATE': '07-Feb-07', 'JOB_ID': 'IT_PROG', 'SALARY': '4200', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '103', 'DEPARTMENT_ID': '60'},
{'EMPLOYEE_ID': '108', 'FIRST_NAME': 'Nancy', 'LAST_NAME': 'Greenberg', 'EMAIL': 'NGREENBE', 'PHONE_NUMBER': '515.124.4569', 'HIRE_DATE': '17-Aug-02', 'JOB_ID': 'FI_MGR', 'SALARY': '12008', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '101', 'DEPARTMENT_ID': '100'}

    ))

#JSON - java script object notation

obj = open("textfile\\mtcars-parquet.json",'r') 
t=obj.read()
print(t)
print(type(t)) #str type

import json

try:
    with open("textfile\\mtcars-parquet.json", 'r') as ob:
        e = ob.readlines()
        f = [json.loads(line) for line in e]
        print(f)
        print(type(f)) #list type
except Exception as err:
    print("Error:", err)

payload = [{'model': 'Mazda RX4', 'mpg': 21, 'cyl': 6, 'disp': 160, 'hp': 110, 'drat': 3.9, 'wt': 2.62, 'qsec': 16.46, 'vs': 0, 'am': 1, 'gear': 4, 'carb': 4}, 
           {'model': 'Mazda RX4 Wag', 'mpg': 21, 'cyl': 6, 'disp': 160, 'hp': 110, 'drat': 3.9, 'wt': 2.875, 'qsec': 17.02, 'vs': 0, 'am': 1, 'gear': 4, 'carb': 4}, 
           {'model': 'Datsun 710', 'mpg': 22.8, 'cyl': 4, 'disp': 108, 'hp': 93, 'drat': 3.85, 'wt': 2.32, 'qsec': 18.61, 'vs': 1, 'am': 1, 'gear': 4, 'carb': 1}
            ]
file_obj = open("sample.json",'w')
json.dump(payload,file_obj) #dumping data in new file
file_obj.close()
