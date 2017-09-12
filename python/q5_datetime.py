# Hint:  use Google to find python function
from datetime import datetime
"""define function to be called for all 3 problems"""
def days_between(date_start, date_stop, date_format):
  a = datetime.strptime(date_start,date_format)
  b = datetime.strptime(date_stop, date_format)
  c = b - a
  return c.days

####a) 

date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format = '%m-%d-%Y'
print(days_between(date_start, date_stop, date_format))

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format = '%m%d%Y'
print(days_between(date_start, date_stop, date_format))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format = '%d-%b-%Y'
print(days_between(date_start, date_stop, date_format))
