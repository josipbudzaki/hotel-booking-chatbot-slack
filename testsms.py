#pip3 install twilio
#python3 testsms.py

import os
from twilio.rest import Client
 
def sendingsms (textmsg, receiver):
    account_sid = "ACc3a1cc658d00cbca3e611eeea8cc9bbb"
    auth_token = "80f8e06e0a5832d7e81b81773de7a119"
    twilio_number = +13254844034
    
    client = Client(account_sid, auth_token)
    
    client.messages.create(from_=twilio_number,
                        to=receiver,
                        body=textmsg)

if __name__ == "__main__":
    sendingsms("Hello from Python!", "+16572305796")

#twilio phone number : +13254844034
#Sannisth phone number : +16572305796
#Account Sid : ACc3a1cc658d00cbca3e611eeea8cc9bbb
#Auth Token : 80f8e06e0a5832d7e81b81773de7a119