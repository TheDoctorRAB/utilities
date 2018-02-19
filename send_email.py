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
    message['Subject']='Idaho ANS 60th anniversary dinner meeting'
    body='''
For those of you that don't have class on Thursday, please consider attending the Idaho ANS 60th dinner meeting. Mark Peters is speaking, and they're trying to get a lot of past presidents there.

Inexplicably, they told the caterers 100 people would show up, which boggles my mind, since really no one from the other universities attend.

But it would be nice to have a strong UI ANS student showing.

http://www.ansidaho.org/event-calendar
'''
#    part=MIMEApplication(open('flyer.pdf','rb').read())
#    part2=MIMEApplication(open('','rb').read())
#    part.add_header('Content-Disposition','attachment',filename='flyer.pdf')
#    part2.add_header('Content-Disposition','attachment',filename='')
#    message.attach(part)
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
