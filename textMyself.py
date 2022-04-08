accountSID = 'AC13057a787d635c6bba6a0b5c90ca3862'
authToken = '536c7dba3ed6460cc88836163075c17c'
myTwilioNumber = '+1415801-8199'
myCellPhone = '+5567981807658'
import twilio
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)
    