import pyperclip
from random import randint

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encrypted_message = ''
decrypted_message = ''

def encrypt_message(toencrypt):
	global encrypted_message
	for symbol in toencrypt:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			num+=key
			if num >=len(LETTERS):
				num -=len(LETTERS)
			elif num<0:
				num +=len(LETTERS)
			encrypted_message = encrypted_message + LETTERS[num]
		else:
			encrypted_message +=symbol
	pyperclip.copy(encrypted_message)
	print(encrypted_message)

def decrypt_message(todecrypt):
	global decrypted_message
	print(todecrypt)
	key = int(raw_input('Input key: '))
	for symbol in todecrypt:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			num-=key
			if num >=len(LETTERS):
				num = num-len(LETTERS)
			elif num <0:
				num +=len(LETTERS)
			decrypted_message = decrypted_message + LETTERS[num]
		else:
			decrypted_message +=symbol
	pyperclip.copy(decrypted_message)
	print(decrypted_message)

def brute_force(encrypted_message):
	global decrypted_message
	print(decrypted_message)
	for key in range(len(LETTERS)):
		decrypted_message = ''
		for symbol in encrypted_message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol)
				num-=key
				if num<0:
					num+=len(LETTERS)
				decrypted_message+=LETTERS[num]
			else:
				decrypted_message+=symbol
		if decrypted_message == message:
			print('Key #%s: %s' % (key, decrypted_message))	

while True:
	key = randint(0,len(LETTERS))
	print(key)
	encrypted_message = ''
	decrypted_message = ''
	message = raw_input('Input your message: ')
	message = message.upper()
	mode = raw_input('Hit \'en\' to encrypt message: ')
	if mode == 'en':
		encrypt_message(message)
		next_action = raw_input('Your message is encrypted. If you want to decrypt it hit \'de\'or Enter to skip it: ')
		if next_action=='de':
			decrypt_message(encrypted_message)
			result = raw_input('Encryption successfull? (y/n)')
			if result == 'y':
				continue
			else:
				result = raw_input('Do you want to use brute-force technic to encrypt it? (y/n)')
				if result == 'y':
					decrypted_message = ''
					brute_force(encrypted_message)
				else:
					continue
		else:
			break
	else:
		print('Please make your decision, en OR de? ')