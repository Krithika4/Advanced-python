#Extracting year,month and date

from datetime import datetime
#creating sample date object
date_obj = datetime(1997,11,10)
extract_date = lambda date : (date.year, date.month, date.day)
print(extract_date(date_obj))