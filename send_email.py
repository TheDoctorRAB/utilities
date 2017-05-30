#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
    message['Subject']='PHYSOR 2018' 
    body='''
All,

PHYSOR will be held in Cancun. If anyone wants to work on anything for the conference, please talk to me. 
Regards,
Bob
'''    
    part=MIMEApplication(open('physor2018.pdf','rb').read())
#    part2=MIMEApplication(open('USA_VisitorInformation.doc','rb').read())
    part.add_header('Content-Disposition','attachment',filename='physor2018.pdf')
#    part2.add_header('Content-Disposition','attachment',filename='USA_VisitorInformation.doc')
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
