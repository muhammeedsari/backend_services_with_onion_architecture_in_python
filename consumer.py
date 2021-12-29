
#from app.controllers.shopping_controller import ShoppingController
from app.data_access.personDAL import PersonDal
#from app.models.mongodb.person_mongodb_model import PersonMongodbModel
from app.controllers.person_controller import PersonController
from app.helpers.mongodbConnector import Connection

connection=Connection()
connection.connect_mongodb()

person_controller = PersonController()
person_controller.create_person()


# shopping_controller = ShoppingController()
# shopping_controller.create_shopping()




#** Query

# print("Job Count", person_controller.get_person_count_by_job("Dramatherapist"))
# person_controller.get_person_sex_rate(False)
# print("job Rate: ", person_controller.get_person_rate_by_job("Personal assistant"))
# print("Sex and Country Count: ", person_controller.get_person_sex_and_country_count(True, "Indonesia"))

