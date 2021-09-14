import os
import math
import random
import smtplib

# Go to google account and get password
# Characters that are available for verification
digits="0123456789"

# Create password OTP and input here 1-9
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

#Asks user to enter google email and password
s.login("Your Gmail Account", "Your App Password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check Your OTP again")
