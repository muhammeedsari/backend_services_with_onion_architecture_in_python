from app.data_access.personDAL import PersonDal
from app.models.mongodb.person_mongodb_model import PersonMongodbModel
from app.models.person_model import PersonModel




class PersonManager:
    def __init__(self):
        self.persondal = PersonDal()

    def create_person(self, person_obj:PersonModel):
                
        person = PersonMongodbModel()
        person.name = person_obj.name          
        person.sex = person_obj.sex
        person.userId = person_obj.userId
        person.birthdate = person_obj.birthdate
        person.current_location = person_obj.current_location
        person.job = person_obj.job
        person.iban = person_obj.iban
        person.currency = person_obj.currency
        person.prefix = person_obj.prefix
        person.race = person_obj.race

        self.persondal.add(person, tag_list=["people"])


#** QUERY
        """[summary]
       
    def get_person_count_by_job(self, query):
        person_job_count = self.persondal.get_by_job(query)
        return person_job_count.count()



    def get_person_count_by_sex(self, query):
        person_sex_count = self.persondal.get_by_sex(query)
        return person_sex_count.count()


    def get_person_count_by_sex_and_country(self, sex, current_location):
        person_sex_and_country = self.persondal.get_sex_and_country(sex=sex, current_location=current_location)
        return person_sex_and_country.count()

       """
