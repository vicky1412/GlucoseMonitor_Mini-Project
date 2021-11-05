from . import mysqldb
import random
import threading
import time

class tempglucose:
    def __init__(self):
        self.number = 0
        self.total_patient = []
        self.views = []
        self.t1 = threading.Thread(target=self.get_db)
        self.t2 = threading.Thread(target=self.update_db)

    def get_db(self):
        while True:
            try:
                time.sleep(10)
                self.views = mysqldb.view()
                self.total_patient.clear()
                for i in self.views:
                    if i['need_glucose'] == "Yes":
                        self.total_patient.append(str(i['first_name']))
                self.number = len(self.total_patient)
            except Exception:
                pass

    def update_db(self):
        while True:
            try:
                time.sleep(20)
                for i in self.views:
                    # x = i['glucose']
                    x = random.randrange(0,10,1)
                    if x<=3:
                        i['need_glucose'] = "Yes"
                    else:
                        i['need_glucose'] = "No"
                    mysqldb.update(i['first_name'],i['last_name'],i['gender'],i['age'],i['contact'],i['address'],i['room_no'],i['bed_no'],x,i['need_glucose'])
            except Exception:
                pass


globject = tempglucose()

globject.t1.start()
globject.t2.start()






