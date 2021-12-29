from app.models.shopping_model import ShoppingModel
import simplejson as json
from app.models.person_model import PersonModel
from app.helpers.kafka import Kafka
from faker import Faker
import random


class ProduceController:
    def __init__(self):
        self.fake = Faker()
        self.kafka = Kafka()
        
    def produce_message(self):          
        person = PersonModel(self.fake.job(), self.fake.current_country(), 
        self.fake.iban(), self.fake.name(), 
        self.fake.boolean(chance_of_getting_true=50), self.fake.date(), 
        self.fake.cryptocurrency_name(),
        self.fake.iban(), self.fake.prefix(), self.fake.country())
        person_dict = person.__dict__
        jsonObj = json.dumps(person_dict)

        self.kafka.produce_message(topic = "raw_data7", 
        key = "test_key", value = jsonObj)

    def produce_shopping(self):
        gender = "Male"
        gender_boolean = self.fake.boolean()
        if gender_boolean == True:
            gender = "Female"
        
        
        shopping = ShoppingModel(name = self.fake.name(), gender = gender, 
        barcode = self.fake.ean(length=13), price = random.randint(25, 250))
        shopping_dict = shopping.__dict__
        jsonObj = json.dumps(shopping_dict)

        self.kafka.produce_message(
            topic = "shopping", 
            key = "test_key", 
            value = jsonObj)








