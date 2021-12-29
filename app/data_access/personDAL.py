from typing import List
from app.models.mongodb.person_mongodb_model import PersonMongodbModel
from mongoengine.queryset.visitor import Q


class PersonDal:
    
    def get(self, filter:any):
        query = PersonMongodbModel.objects(filter)
        return query

    def get_by_job(self, job:str):
        query = PersonMongodbModel.objects(job=job)
        return query


    def get_by_sex(self, sex:str):
        query = PersonMongodbModel.objects(sex=sex)
        return query
   
    def get_all(self):
        count = PersonMongodbModel.objects.count()
        return count

    def get_sex_and_country(self, sex:str, current_location:str):
        query = PersonMongodbModel.objects(Q(sex=sex) & Q(race=current_location))
        return query
    
    def delete(self, filter:any):
        person = PersonMongodbModel.objects(filter)
        person.delete()

    
    def update(self, filter:any, update_object:any):
        person = PersonMongodbModel.objects(filter)
        person.update(update_object)

    
    def add(self, person:PersonMongodbModel, tag_list:List[str]):
        person.tags = tag_list
        person.save()