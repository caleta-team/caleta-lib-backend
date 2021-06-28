import json

import requests

class CaletaUtils():
    TYPE_STRESS="stress"
    TYPE_ACTIVITY="activity"
    TYPE_RESPIRATION="respiration"

    def __init__(self, server, port):
        self.servername = server
        self.serverport = port

    def __getInformation(self,endpoint,token):
        headers = {'token': token}
        r = requests.get(self.servername+":"+str(self.serverport)+"/"+endpoint, headers=headers)
        return r.text

    def __uploadInformation(self,endpoint,jsondata,token):
        headers = {'token': token,'Content-Type':'application/json'}
        print(str(jsondata) + " -- "+str(self.servername+":"+str(self.serverport)+"/"+endpoint))
        r = requests.post(self.servername+":"+str(self.serverport)+"/"+endpoint,data=json.dumps(jsondata), headers=headers)
        return r.text

    def saveStress(self,value,babyid,token):
        data={}
        data['name']=""
        data['comments']=""
        data['anomaly']=False
        data['type'] = self.TYPE_STRESS
        data['value'] = value
        data['babyid'] = babyid
        self.__uploadInformation("event", data ,token)