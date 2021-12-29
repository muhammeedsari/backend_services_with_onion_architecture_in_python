import datetime
from faker import Faker

deneme = {
    "_id": {
        "$oid": "613f3d7dcb462a385d2c9a0c"
    },
    "job": "Freight forwarder",
    "current_location": "United States",
    "userId": "GB17VZHL16780473249299",
    "name": "Andrea Fernandez",
    "sex": True,
    "birthdate": {
        "$date": "2005-07-28T00:00:00.000Z"
    },
    "currency": "DigitalNote",
    "iban": "GB87NGMT73296406854173",
    "prefix": "Mr.",
    "race": "Sri Lanka",
    "tags": ["people"]
}
# input =deneme["birthdate"]["$date"]
# format = "%Y-%m-%dT%H:%M:%S.%fZ"
# datetime = datetime.datetime.strptime(input, format)
# print(datetime.year)


# def get_people_by_birthdate_year(self, birthdate):
#     input =deneme["birthdate"]["$date"]
#     format = "%Y-%m-%dT%H:%M:%S.%fZ"
#     datetime = datetime.datetime.strptime(input, format)
#     return datetime.year
#     print(datetime.year)


fake = Faker()
date = fake.date()
print(date)

def get_people_by_birthdate_year(input):
    format = "%Y-%m-%d"
    datet = datetime.datetime.strptime(input, format)
    return datet.year

result = get_people_by_birthdate_year(date)
print(result)


