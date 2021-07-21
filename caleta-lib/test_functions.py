import random
from time import sleep

from CaletaUtils import CaletaUtils

def getBabyJSON(name,lastname,photo):
    data_set = {}
    data_set['name']=name
    data_set['lastname']=lastname
    data_set['photo']=photo
    return data_set

def getEventJSON(name,type,comments,anomaly):
    data_set = {}
    data_set['type']=type
    data_set['comments']=comments
    data_set['anomaly']=anomaly
    data_set['name']=name
    return data_set


token = "WGVutzn9zyFRXXvK23Xu"
def initData():
    #babys
    fun = CaletaUtils("http://vai.uca.es", 5000)

    res=fun.uploadInformation("baby", getBabyJSON("Jon","Doe","https://raisingchildren.net.au/__data/assets/image/0025/49165/premature-birth-feelingsnarrow.jpg"), token)
    fun.uploadInformation("baby", getBabyJSON("Ozan", "Pitt","https://image.sciencenorway.no/1553802.jpg?imageId=1553802&width=1058&height=604"),token)
    fun.uploadInformation("baby",getBabyJSON("Dayna", "Gates", "https://c.stocksy.com/a/eHV400/z9/1073570.jpg"),token)
    fun.uploadInformation("baby", getBabyJSON("Kunal", "Krae","https://cdn.literacytrust.org.uk/media/images/neonatalblog2.5ad7c423.fill-950x365.jpg"),token)
    fun.uploadInformation("baby", getBabyJSON("Ricardo", "Atkins",
                                              "https://i.pinimg.com/originals/f5/fc/a6/f5fca67dd412a7c8d7a0c56ca278aeba.png"),
                          token)

    '''
    fun.uploadInformation2("event", getEventJSON("Evento 1",0,"Comentarios 1",0),token)
    fun.uploadInformation2("event", getEventJSON("Evento 2",0, "Comentarios 2", 1), token)
    fun.uploadInformation2("event", getEventJSON("Evento 3",1, "Comentarios 3", 0), token)
    fun.uploadInformation2("event", getEventJSON("Evento 4",2, "Comentarios 4", 0), token)
    fun.uploadInformation2("event", getEventJSON("Evento 5",2, "Comentarios 5", 1), token)
    '''

def testUploads():
    utils = CaletaUtils("http://vai.uca.es",5000)
    babyid = 100
    i=1

    while i<100:
        stress_random = random.randint(0, 100)
        activity_random_left = random.randint(0, 100)
        activity_random_right = random.randint(0, 100)
        activity_random_down = random.randint(0, 100)
        resp_random = random.randint(50, 95)

        random_anomaly_activity = random.randint(0, 100)
        random_anomaly_stress = random.randint(0, 100)
        random_anomaly_resp = random.randint(0, 100)
        anomaly_stress = anomaly_res = anomaly_act = False
        if random_anomaly_resp>80:
            anomaly_res = True
        if random_anomaly_activity>80:
            anomaly_act = True
        if random_anomaly_stress > 80:
            anomaly_stress = True
        utils.saveStress(stress_random,babyid,token,"","",anomaly_stress)
        utils.saveActivity(activity_random_left,activity_random_right,activity_random_down, babyid, token,"","",anomaly_act)
        utils.saveRespiration(resp_random, babyid, token,"","",anomaly_res)
        i+=1
        sleep(3)


if __name__ == '__main__':
    initData()
    #testUploads()
