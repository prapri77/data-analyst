LOAD DATA
INFILE 'D:\emp1.csv'
INTO TABLE emp
APPEND
FIELDS TERMINATED BY ','
(EMPLOYEE_ID,      
  FIRST_NAME,       
  LAST_NAME,        
  EMAIL,                      
  JOB_ID,          
  SALARY,            
  DEPARTMENT_ID)