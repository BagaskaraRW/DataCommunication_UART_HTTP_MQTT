import serial
import time
import paho.mqtt.client as paho
import requests

i = 0
t = 0
ip = "192.168.1.5" #IP LAPTOP 2
topik = "komdat/fungames/6.1/data"


def dataAwal(p,b):
    com = serial.Serial(p,b)
    while(com.inWaiting()==0):
        pass
    data = str(com.readline(),"utf-8")
    com.close()
    return data

def dataLanjutan(ip,topik,data):
    Host = paho.Client(".")
    Host.connect(ip)
    Host.loop_start()
    Host.publish("komdat/data",data)
    Host.loop_stop()
    Host.disconnect()

def dataAkhir():
    url = "http://192.168.1.5:5000/komdat/fungames/6.1/data"
    data = requests.request("GET",url)
    return(data.json()['data'])
    
while(i < 61):
    ta = time.time()
    data = dataAwal('COM7',9600)
    dataLanjutan(ip,topik,data)
    print("=========================================================================")
    print("Data yang dikirim adalah: "+str(data))
    print("Data yang diterima adalah: ",dataAkhir())
    ts = (time.time()-ta)*1000    
    print("Waktu eksekusi program: "+str(ts)+" ms")
    print("Total waktu yang telah berjalan: "+str(t)+" ms")
    print("=========================================================================")
    i+=1
    t+=ts
