import requests
#import os
from datetime import datetime

api_key = '9b7a849e18e426a4bed9504c45675652'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print("-------------------------------------------------------------")
f=open("text.txt","r")
lines=f.readlines()
s0=lines[0].replace('\n','')
s1=lines[1].replace('\n','')
s2=lines[2].replace('\n','')
s3=lines[3].replace('\n','')
s4=lines[4].replace('\n','')
s5=lines[5].replace('\n','')

print(s0+location.upper() +" | "+date_time)
print(s1)
print(s2+" {:.2f} deg C".format(temp_city))
print(s3+ weather_desc)
print(s4+ str(hmdt)+"%")
print(s5+ str(wind_spd)+"kmph")




# print("-------------------------------------------------------------")
# print("Weather stats for {} | {}".format(location.upper(),date_time))
# print("-------------------------------------------------------------")

# print("Current temperature is {:.2f} deg C".format(temp_city))
# print("Current weather desc is :",weather_desc)
# print("Current Humidity        :",hmdt,'%')
# print("Current wind speed      :",wind_spd,'kmph')


