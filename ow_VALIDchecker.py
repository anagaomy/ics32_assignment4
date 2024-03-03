from OpenWeather import OpenWeather
import json

zipcode = "92697"
ccode = "US"
apikey = "071481e600ad1194c116a0b9e95d56a8"

open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
dict = open_weather.load_data()

file_out = open('open_weather.json', "w")
json.dump(dict, file_out, indent=4)
file_out.close()

print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")