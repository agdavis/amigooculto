import smtplib
import os
from email.mime.text import MIMEText
import time
import random

participantes = {
1: ['Tia Yolanda', 'XXX', '1'],
2: ['Tio Mauricio', 'XXX', '1'],
3: ['Marina', 'XXX', '1'],
4: ['Mauri', 'XXX', '1'],

5: ['Tio Dudu', 'XXX', '2'],
6: ['Soraya', 'XXX', '2'],
7: ['Cecilia', 'XXX', '2'],
8: ['Aninha', 'XXX', '2'],

9: ['Vo Catharina', 'XXX', '3'],
10: ['Vo Veveu', 'XXX', '3'],

11: ['Tio Clodo', 'XXX', '4'],
12: ['Tia Beth', 'XXX', '4'],
13: ['Xande', 'XXX', '4'],
14: ['Paula', 'XXX', '4'],
}

def print_config(to):
	for (ffrom, tto) in enumerate(to):
		print ffrom+1, participantes[ffrom+1][0], '->', participantes[tto][0]

def validate_config(to):
	for (ffrom, tto) in enumerate(to):
		ffrom += 1 # indexed by 1
		if (ffrom == tto):
			return False
		# Check if belongs to the same house
		if  participantes[ffrom][2] == participantes[tto][2]:
			return False
	
	cycle_detect = set()
	curr = 0
	for i in range(1, len(participantes)+1):
		tto = to[curr]
		cycle_detect.add(curr + 1)
		cycle_detect.add(tto)
		curr = tto - 1

	if len(cycle_detect) != len(participantes):
		return False
	return True

def set_to_vector():
	to = [i for i in range(1, len(participantes)+1)]
	random.shuffle(to)
	return to

def Sorteio():
	to = set_to_vector()
	test = 1
	while not validate_config(to):
		to = set_to_vector()
		test += 1
	print test
	#print_config(to)
	SendEmail(to, test=True)

def SendEmail(sorteio, test=True):
	
	raw_input()
	for (ffrom, tto) in enumerate(sorteio):
		msg = MIMEText("TESTE TESTE O seu amig@ oculto eh " + participantes[tto][0] + ". Um oferecimento do maravilhoso sistema de sorteio Alexandre Davis :)")
		if (test):
			if ((ffrom+1) <= 10):
				continue
			msg['Subject'] = "TESTE TEST O seu amig@ oculto dos Davis de 2018 eh"
			msg['From'] = "amigoocultodavis@gmail.com"
			msg['To'] =  participantes[ffrom+1][1]
		else:
			msg = MIMEText("O seu amig@ oculto eh " + participantes[tto][0] + ". Um oferecimento do maravilhoso sistema de sorteio Alexandre e Paula Davis :)")
			msg['Subject'] = "O seu amig@ oculto dos Davis de 2018 eh"
			msg['From'] = "amigoocultodavis@gmail.com"
			msg['To'] =  participantes[ffrom+1][1]

		print "SEND", ffrom+1, participantes[ffrom+1][0]
		# Send the message via our own SMTP server, but don't include the
		# envelope header.
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()  
		s.login("amigoocultodavis","password")
		#s.sendmail("amigoocultodavis@gmail.com", [participantes[ffrom+1][1]], msg.as_string())
		s.quit()

Sorteio()


