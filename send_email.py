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
script,email_list=argv
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
message=MIMEMultipart()
message['From']=sender
message['Subject']='ANS student section revival'
body='''
Good afternoon,

I'm a *brand* new faculty member in the nuclear engineering program. I'm interested in reviving the American Nuclear Society (ANS) student branch here at UI. I recently was at the nation ANS conference in Washington, D.C. There was no student representation of UI at all. There was plenty of UC-Berkeley, Wisconsin, Penn State, and Texas A&M, and all those students know each other. When they graduate and are looking for jobs and research collaborators, they're going to remember their own friends and colleagues that they met at conferences like this. Clearly, developing a UI presence at these conferences is highly beneficial and valuable. Additionally, there is a student ANS conference in Madison, Wisonsin at the end of March. Any student can still submit a paper to present there as well. 

At the ANS conference, I spoke with the Executive Committee of the student branches about my interest in reviving our group. There is some work to do, but it is not overwhelming. First, I'd like to complile a list of students who are interested in actively participating in a student branch. Once I do that, we can get together for a meeting a discuss the next steps. Please reply if you are interested, and if you have any other questions.

Regards,
Bob Borrelli
'''
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
for j in range(0,email_list_size):
    receiver=email_list[0]
    message['To']=receiver
    message.attach(MIMEText(body,'plain'))
    message_text=message.as_string()
#
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
