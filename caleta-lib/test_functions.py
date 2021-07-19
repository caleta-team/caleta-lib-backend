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

    res=fun.uploadInformation2("baby", getBabyJSON("Frank","Zappa","https://rock101online.mx/wp-content/uploads/2019/12/frank-zappa-840x658.jpg"), token)
    print(res)
    fun.uploadInformation2("baby", getBabyJSON("Brian", "May","https://okdiario.com/img/2020/12/21/brian-may-655x368.jpg"),token)
    fun.uploadInformation2("baby",getBabyJSON("David", "Gilmour", "https://cdns-images.dzcdn.net/images/artist/10ee71ec586e02afb05581c19291a9d9/264x264.jpg"),token)
    fun.uploadInformation2("baby", getBabyJSON("Stevie", "Ray","https://images-na.ssl-images-amazon.com/images/I/91jTocNmWpL._SY450_.jpg"),token)
    fun.uploadInformation2("baby", getBabyJSON("BB", "King",
                                              "https://upload.wikimedia.org/wikipedia/commons/9/97/B.B._King_in_2009.jpg"),
                          token)
    fun.uploadInformation2("baby", getBabyJSON("Eric", "Clapton",
                                              "https://as.com/tikitakas/imagenes/2021/05/18/portada/1621326137_062566_1621326606_noticia_normal_recorte1.jpg"),
                          token)

    fun.uploadInformation2("event", getEventJSON("Evento 1",0,"Comentarios 1",0),token)
    fun.uploadInformation2("event", getEventJSON("Evento 2",0, "Comentarios 2", 1), token)
    fun.uploadInformation2("event", getEventJSON("Evento 3",1, "Comentarios 3", 0), token)
    fun.uploadInformation2("event", getEventJSON("Evento 4",2, "Comentarios 4", 0), token)
    fun.uploadInformation2("event", getEventJSON("Evento 5",2, "Comentarios 5", 1), token)


def testUploads():
    utils = CaletaUtils("http://vai.uca.es",5000)
    babyid = 100
    i=1

    #while i<100:
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
    #initData()
    testUploads()
