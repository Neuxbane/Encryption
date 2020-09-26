import math
def Seed(a):
	global c
	c += 1
	return round(abs(math.atan(math.cos(a*(a+c))))*(math.cos(c)*10))
while True:
	encryption = ''
	print('Example: C:\\Users\\Banu Chrisnadi\\Desktop\\MyData.txt')
	location = input('Your target location: ')
	location = location.replace("\\","/")
	c = 0
	data = open(location, 'r').read()
	code = []
	encryptioncode = ''
	strLock = ''
	try:
		for x in data:
			code.append(ord(x))
		io = input('Lock(y) or Unlock(n) (y/n): ')
		if io.lower() == 'y':
			lock = input('Set Password: ')
			for x in range(len(lock)):
				encryption += str(ord(lock[x]))
			for x in range(len(code)):
				encryptioncode += str(round((code[x]+(Seed(int(encryption))))))+' '
			print(encryption)
			for x in encryptioncode.split(' ')[:-1]:
				strLock += chr(int(x))
			open(location,"w").write(str(strLock))
		else:
			unlock = input('Password?: ')
			for x in range(len(unlock)):
				encryption += str(ord(unlock[x]))
			for x in range(len(code)):
				encryptioncode += str(math.ceil(code[x]-(Seed(int(encryption)))))+' '
			print(encryption)
			for x in encryptioncode.split(' ')[:-1]:
				strLock += chr(int(x))
			open(location,"w").write(str(strLock))
	except Exception as e:
		print('error', e)
		open(location,"w").write(str(data))