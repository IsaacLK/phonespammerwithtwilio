import os
#PLEASE USE THIS BOT RESPONSIBLY, I AM NOT RESPONSIBLE FOR ANY DAMGES DONE WITH THIS BOT
from twilio.rest import Client


#FILL WITH TWILIO INFO
accountsid = ''
authtoken = ''
#include country code 
yourtwilionumber = '' 
messagereceivernumber = input("Phone number that you are sending message to (Include country code):")
messagebody= input("What message are you sending? ")
times = input("How many times are you sending this message ")
client = Client(accountsid, authtoken)
for i in range(1,int(times),1):

    message = client.messages \
                    .create(
                        body=messagebody,
                        from_=yourtwilionumber,
                        to=messagereceivernumber
                    )
    
