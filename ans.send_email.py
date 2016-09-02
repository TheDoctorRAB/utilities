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
    message['Subject']='ANS student meeting: 26 August 15.00'
    body='''
Hi Everyone,

We will have the summer meeting this Friday the 26th at 3 pm. We have ongoing tasks, so please check to see if you have to do anything. 

We also have a new task: We might be able to get some money from ANS national for Science Week. The proposal is due in September. For more information: http://www.ans.org/pi/nsw/
Let's get some ideas going for this in the meeting. Jared and I already talked about possibilites, but if we intend to submit a proposal we need to prepare a rough budget.

We also have to address the student conference proposal with KSU. It turns out that ANS moved up the due date for the proposal to October. Neither KSU or us would be able to get everything done in time. However, I suggest we consider going forward with the process for 2018. That would give us a lot more time to prepare. 

We have nominations for officers:

	President: Kelley Verner
	Vice President: Jieun Lee
	Sec/SocMed: Malachi Tolman

If there are other nominees, email me so I can add you. 

I think it would be a good idea for each nominee to put together a briefing for me to circulate to the group. Just a paragraph or two on why you want to work in this position and your background, expertise, etc. 

Please come on by if there is anything else you want to talk about. 

Regards,
Bob
'''    
#    part=MIMEApplication(open('annual_meeting.pdf','rb').read())
#    part2=MIMEApplication(open('cleanup.flyer.pdf','rb').read())
#    part.add_header('Content-Disposition','attachment',filename='annual_meeting.pdf')
#    part2.add_header('Content-Disposition','attachment',filename='cleanup.flyer.pdf')
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
