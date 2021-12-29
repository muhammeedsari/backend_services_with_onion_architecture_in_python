from app.data_access.personDAL import PersonDal
from app.business.person_manager import PersonManager
from app.models.person_model import PersonModel
from app.helpers.kafka import Kafka
import simplejson as json

class PersonController:

    def __init__(self):
        self.person_manager = PersonManager()

    def create_person(self):
        kafka = Kafka()
        consumer = kafka.create_consumer(topic="raw_data7")

        while True:
            msg = consumer.poll()

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            
        
            json_data = json.loads(msg.value().decode('utf-8'))
            
            print(json_data)
            person_obj = PersonModel(**json_data)
           
            self.person_manager.create_person(person_obj)
            # person_manager is kodlarını barındırır. 
            # manager classları controllerda çagrılır.
            # person_manager is yapar. Controller is yaptırır.


 
 #** QUERIES
        """[summary]
      
    def get_person_count_by_job(self, job_name:any):

        query = self.person_manager.get_person_count_by_job(job_name)
        return query

    def get_person_sex_rate(self, gender:any):
        person_count =PersonDal()
        total = person_count.get_all()
        wanted_gender = self.person_manager.get_person_count_by_sex(gender)
        other_gender = total-wanted_gender
        if gender == False:
            print("Female Counts : ", wanted_gender, "female/male rate : ", 
            wanted_gender/other_gender, "female rate : ", wanted_gender/total)
        else:
            print("Male Counts : ", wanted_gender, "male/female rate : ", wanted_gender/other_gender, 
            "male rate : ", wanted_gender/total)

    
    def get_person_rate_by_job(self, job_name):
        person_count =PersonDal()
        total = person_count.get_all()
        job_count = self.person_manager.get_person_count_by_job(job_name)
        rate = job_count/total
        return rate


    def get_person_sex_and_country_count(self, sex, country):
        query = self.person_manager.get_person_count_by_sex_and_country(sex=sex, current_location=country)
        return query

        """       
        
        