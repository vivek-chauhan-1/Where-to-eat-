import paho.mqtt.client as mqtt
import time
import protocol
name="vivek1"
address="test.mosquitto.org"
recipient=[]
def on_connect(client,userdata,flags,rc):
    print "I am connected to broker "
    client.subscribe("chat/encypher/apna",1)
    client.publish("chat/encypher/apna","Hey i am connected ",1)
def on_message(client,userdata,msg):
    a = protocol.decode(name,msg.payload)
    print a 
          
         
  #  print "new msg "+ str(msg.payload)+" in topic "+str(msg.topic)
def on_disconnect(client,userdata,rc):
    print "Disconnected from broker "

client=mqtt.Client()
client.on_connect= on_connect
client.on_message= on_message
client.on_disconnect= on_disconnect
while True:
    
    address=raw_input("input broker ip address : ")
    print address
    e=raw_input("are you sure,type yes or no : ") 
    if(e=="yes"):
        break
    elif(e=="no"):
        continue
client.connect("test.mosquitto,org",1883,120) 
client.loop_start()

while True:
    name=raw_input("What's your name : ")
    print name
    b=raw_input("Are you sure? type yes or no")
    if(b=="yes"):
        break
    elif(b=="no"):
        continue
while True:
     action=raw_input ("What  action you want to take? \n")
     print action
     msg=raw_input("Enter msg : \n")
  
     if (action=="send"):
        new_msg = protocol.send(name,msg)
        print "Encoded msg : " + new_msg+"\n" 
        client.publish("chat/encypher/apna",new_msg,1)
     if (action=="device"):
        new_msg = protocol.device(name,msg)
        print "encoded msg : " + new_msg+"\n" 
        client.publish("chat/encypher/apna",new_msg,1)

        
         
'''
     if(action=="ban"):
         protocol.ban(recipient)
    
 '''   
