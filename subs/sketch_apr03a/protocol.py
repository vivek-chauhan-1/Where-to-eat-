import time
import serial
import automation as py
banlist = ['kamine','kamini']
devlist = ['led1','led2','temp1']

def ban(recipient):
    recipient=raw_input("Ban recipient list : \n")
    banlist=banlist.append(recipient)
    print banlist
    #for i in recipient:
     #   recipient[i].remove()
def encode(name,msg,recipient):
    ticks=time.time()
    print "the time is:",ticks
    se=str(ticks)
    
    s=':'
    bla =(name,msg,recipient,se)
    f=s.join(bla)

    print "the username"+name+"whose messageis "+msg+" has sent it to the recipient"+recipient+"at time "+se
    return f 
    
def decode(name,msg):
    comment  = "nothing"
    a  = msg.split(":")
    print len(a)
     
    if len(a)>2 :    
        username  = a[0]
        new_msg = a[1]
        recp =  a[2]
        time = a[3]
        if recp  ==  name:
            comment  =  "kudh ko msg beja : "+new_msg+" at "+time
        else :
            if recp in devlist:
                if new_msg == "temp":
                    py.temp(recp)
                if new_msg == "on":
                    py.on(recp)
                if new_msg == "off":
                    py.off(recp)
                else:
                    comment  =  "ye device "+recp+" to  hai nahi  !!"
                    
                
                
            if recp in banlist:
                comment  =  "ye banda "+recp+" to ban hai !!"

            else :
                comment  = recp+ " said  :"+new_msg+" @ "+time
        return comment
    else:
        return comment

    

    
def send(name,msg):
   
   recipient=raw_input("Who's your recipient ? \n")
   f = encode(name,msg,recipient)
   return f  
  
def device(name,msg):
 
   recipient=raw_input("Your device name: ")
   f = encode(name,msg,recipient)
   return f  


    










    
    
