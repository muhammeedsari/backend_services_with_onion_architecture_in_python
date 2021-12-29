import time
from app.controllers.produce_controller import ProduceController

producer = ProduceController()

while True:
    producer.produce_message()
    #time.sleep(1)

    #producer.produce_shopping()
    


