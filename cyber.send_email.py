########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.19.November.2015
# v1.0
########################################################################
#
# Read in a csv file with each email address on a line
# Send an email to each email address
#
########################################################################
#
# imports
#
import smtplib
import numpy
from sys import argv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.application import MIMEApplication
from email.MIMEBase import MIMEBase
from email import Encoders
script,email_list=argv #add a CSV file with email addresses (one on each line) as command line argument
#
########################################################################
#
# email sender
#
sender='r.angelo.borrelli@gmail.com'
#
#######
#
# read in the email addresses
#
email_list=numpy.loadtxt(email_list,dtype=str)
#
#######
#
# loop through the csv to count the email addresses
#
i=0
for line in email_list:
    i=i+1
    email_list_size=i
# end line
#
#######
#
#
#######
#
# SMTP client session start 
#
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,'hrgntcsdnwchgvsk')
#
#######
#
# send the email
#
for j in range(0,email_list_size): #been getting a 'connection unexpectedly closed' error around j=100 
    receiver=email_list[j]
    message=MIMEMultipart()
    message['From']='Bob Borrelli'
    message['To']=receiver
    message['Subject']='INCR@CAES: Presentation slides'
    body='''
Hi Everyone,

On behalf of Michael, I'd like to thank you all for coming to our meeting last Friday, and for the full day of tours on Thursday. Michael and I are putting together our own action items to build on the great momentum generated from this effort. I'll also be sending out links to the documents I prepared based on the afternoon breakout session once Michael reviews them. These will include email addresses of everyone attending last Friday too. 

I'll also be sending out emails periodically that can help up move forward with research. In the meanwhile, I have attached the presentation slides from the meeting in compressed .rar format. 

We will be seeing some of you at the Intermountain Energy Summit, the intern poster session at EIL, and then at the ANS conference in September in Santa Fe. We're also trying to connect with some key people that were not able to attend the meeting to see if they can come up for a symposium in the fall semester. Finally, I'll be at the ANS conference in November. We're keeping busy.

Please also submit any other people who you think might be interested in contributing to our efforts. 


Regards,
Bob
'''    
    part=MIMEApplication(open('cyber.presentations.rar','rb').read())
#    part2=MIMEApplication(open('cleanup.flyer.pdf','rb').read())
    part.add_header('Content-Disposition','attachment',filename='cyber.presentations.rar')
#    part2.add_header('Content-Disposition','attachment',filename='cleanup.flyer.pdf')
    message.attach(part)
#    message.attach(part2)
    message.attach(MIMEText(body,'plain'))
    message_text=message.as_string()
#
    server.sendmail(sender,receiver,message_text)
    print j,receiver
# end j
server.quit()
#
########################################################################
#
# EOF
#
########################################################################
