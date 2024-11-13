########################################################################
# @TheDoctorRAB
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
import email
from sys import argv
from email.mime.multipart import MIMEMultipart #python3
from email.mime.text import MIMEText #python3
from email.mime.image import MIMEImage #python3
#from email.MIMEMultipart import MIMEMultipart #python2
#from email.MIMEText import MIMEText #python2
#from email.MIMEImage import MIMEImage #python2
from email.mime.application import MIMEApplication
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
server.login(sender,'flqcvwlznmwgjhzh')
#
#######
#
# send the email
#
for j in range(0,email_list_size): #been getting a 'connection unexpectedly closed' error around j=100
    receiver=email_list[j]
    message=MIMEMultipart()
    message['From']='Prof. R. A. Borrelli'
    message['To']=receiver
    message['Subject']='NE529 - News and notes'
    body='''
Hello everyone -
You're getting this email because you're enrolled in NE/TM529. Due to the holidy, We will be starting our first class on Monday, January 22, 7 pm. We will be in TAB320. If you are in Idaho Falls, you're required to show up in person for class. If you are in Moscow, please reply to me and let me know.

For course management and materials, we will be using piazza. I learned Canvas over the last year for other courses, but I just didn't have the time to craft the course website because I don't have a TA. Sign up for a free account on piazza.com. If you took NE585 or NE450, your account should still be valid.

Sign up at -

https://piazza.com/uidaho/spring2024/ne529

Everything needed for the course is there.

Additionally, we will be learning MCNP in the course. It's free for academic use. The information for ordering is on piazza under the MCNP discussion thread. You'll have to create a free account at RSICC. They issue a personal license under the University of Idaho and then send you the installation disks.

You'll be prompted to justify why you're ordering MCNP. Say something like -
MCNP will be used in the NE585 graduate nuclear fuel cycles course at the University of Idaho to study fundamental neutron transport theory and to use for a neutronics modeling design project. Make sure to say you are enrolled as a graduate student at the University of Idaho. If any of you are not US citizens, you should request the online version.

INL employees in the class can typically obtain MCNP through INL. Check with your supervisor. If any of you already have MCNP, you're all set. If you prefer to use Serpent (if you already have it), that's fine too.

Please post any questions and comments at piazza under News, notes, policies for the benefit of the rest of the class.


Prof. R. A. Borrelli
University of Idaho
Department of Nuclear Engineering & Industrial Management
'''
#    part=MIMEApplication(open('flyer.pdf','rb').read())
#    part.add_header('Content-Disposition','attachment',filename='flyer.pdf')
#    message.attach(part)
    message.attach(MIMEText(body,'plain'))
    message_text=message.as_string()
#
    server.sendmail(sender,receiver,message_text)
#   print j,receiver  #python2
    print(j,receiver) #python3
# end j
server.quit()
#
########################################################################
