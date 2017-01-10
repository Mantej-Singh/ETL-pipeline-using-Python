import pandas as pd
import os
from  datetime import datetime
import time
import Email
ufo=pd.read_csv('http://bit.ly/uforeports')

#print (ufo.head())
##print(ufo.describe())

#print(ufo['Time'].head())
time_list=ufo['Time'].values.tolist()

#print(time_list[0:5])
current_time=time.strftime("%I-%M-%S")
print("Adding timestamp as ",current_time)
def optfile(text):
    file=open('cleaned_data_'+str(current_time)+'.txt','a')
    file.write(text)
    file.write('\n')
    file.close()

print("Extracting....")

for i in time_list:
    ###date=i
    cleaned_data=datetime.strptime(i,'%m/%d/%Y %H:%M').date()
    cleaned_data=cleaned_data.strftime("%d/%m/%Y")
    optfile((cleaned_data))
    
print("Done!")
Email.send()
