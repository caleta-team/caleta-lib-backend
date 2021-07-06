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
    fun = CaletaUtils("http://localhost", 5000)

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
    utils = CaletaUtils("http://localhost",5000)

    utils.saveStress(17,5,token)
    utils.saveActivity(86, 6, token)
    utils.saveRespiration(98, 7, token)


if __name__ == '__main__':
    initData()
    #testUploads()
