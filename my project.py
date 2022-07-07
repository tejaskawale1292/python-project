from cProfile import label
from tkinter import Label 
import twilio
import random 
OTP=random.randint(100000,999999)
from twilio.rest import Client
account_sid ='AC531eaceaa24fa8fc634bfbfa9b15ab78' 
auth_token ='61bf9dfb181a0d59941232977f595855' 
client = Client(account_sid, auth_token)
message = client.messages.create(
body="Your OTP is ::"+str(OTP), 
from_='+12312416250', 
to='+917385326237'
)
print(" ")
print(" ") 
print("Successfully sent")
print(" ")
print(" ") 
a=input("Enter your OTP ")
print(" ")
print(" ")
9 
if a==str(OTP): 
print("verified")
print(" ")
print(" ")
else:
print("Please enter Valid OTP") 
print(" ")
print(" ")