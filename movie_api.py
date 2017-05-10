import requests


print "Welcome to our cool movie console app" 

title = raw_input("Enter movie name: ")

parameters = {'t':title}

response = requests.get("http://omdbapi.com/",params=parameters)

print response.json()
