import pip._vendor.requests as requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
people = json['people']

print("The people currently in the space are:")
for person in people:
    print(person['name'])
