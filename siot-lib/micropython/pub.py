from siot import iotimport timeSERVER = "192.168.0.129"        #MQTT服务器IPCLIENT_ID = ""                  #在SIoT上，CLIENT_ID可以留空IOT_pubTopic  = 'xzr/001'       #“topic”为“项目名称/设备名称”IOT_UserName ='siot'            #用户名IOT_PassWord ='dfrobot'         #密码def WIFIconnect():  import network  ssid = "dfrobotYanfa"  password =  "hidfrobot"  station = network.WLAN(network.STA_IF)  if station.isconnected() == True:    print("Wifi already connected")    return  station.active(True)  station.connect(ssid, password)  while station.isconnected() == False:      pass  print("Connection successful")  print(station.ifconfig())siot = iot(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)WIFIconnect()#mpysiot.connect()siot.loop()tick = 0try:    while True:        siot.publish(IOT_pubTopic, "value %d"%tick)        time.sleep(1)         tick = tick+1except:    siot.stop()    print("disconnect seccused")