import math,numpy,sys,pygame

global beat
beat = 12

global sample_rate
sample_rate = 8000

#EXCEPCIONES
class NegativeException(Exception):
	@classmethod
	def check(self,x,funcion):
		if x<=0:
			raise self('Es menor o igual a 0 en la funcion: ',funcion)

#LECTURA DE ARCHIVOS
def leerArchivo(ruta):
	cadena = ""
	fo = open(ruta) 
	for line in fo:	
		limpia = line	
		if ( limpia.find('//') >= 0 ):
			limpia = limpia[0:limpia.find('//')]
		limpia = limpia.strip().strip('/t')
		cadena+=limpia
	fo.close()
	return cadena
	

#GENERADORES
def sin(c,a):
	this_function_name = sys._getframe().f_code.co_name

	NegativeException.check(c,this_function_name)
	NegativeException.check(a,this_function_name)

	buff = [0]*beat
	x = (c*2*(math.pi))/beat
	for i in range(0,beat):
		buff[i] = a* (math.sin(i*x))
	return buff

def lin(a,b):
	this_function_name = sys._getframe().f_code.co_name

	NegativeException.check(a,this_function_name)
	NegativeException.check(b,this_function_name)


	return numpy.linspace(a,b,beat)

def sil():
	return [0]*beat

def noi(a):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(a,this_function_name)

	return numpy.random.random_sample(size=beat)*a



#METODOS
def play(buff,ms):
	pygame.mixer.pre_init(sample_rate, -16, 1) # 44.1kHz, 16-bit signed, mono
	pygame.init()

	buffO = buff

	buff = numpy.array(buff)

	ms = int(round(ms))

	sound = pygame.sndarray.make_sound(buff)
	sound.play(-1)
	pygame.time.delay(ms)
	sound.stop()

	return buffO

def post(buff,p=None):
	#Aca no importa que sea p
	cadena = ""
	for i in range(0,len(buff)):
		cadena= cadena+" " +str(buff[i])
	print cadena

	return buff

def loop(buff,R):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(R,this_function_name) 

	buff_r = []
	while R > 0:
		if R < 1:
			lastItemToAdd = int(round(R*len(buff)))
			buff_r = buff_r + buff[:lastItemToAdd]
			R = 0
		else:
			buff_r = buff_r + buff
			R -= 1
	return buff_r

def resample(buff_a,L):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(L,this_function_name) 

	L = int(round(L))

	buff_b =[0]*L
	for i in range(0,L):
		buff_b[i] = buff_a[i*len(buff_a)//L]
	return buff_b

def tune(buff , P):
	#Acepta negativos, 0 y positivos
	return resample(buff,int(len(buff)*((2**(1.0/beat))**-P)))

def reduce(buff, N):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(N,this_function_name) 

	L = beat*N
	if len(buff)>N:
		return resample ( buff , N)
	else:
		return buff

def expand(buff, N):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(N,this_function_name) 

	L = beat*N
	if len(buff)<N:
		return resample ( buff , N)
	else:
		return buff

def fill(buff,N):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(N,this_function_name) 

	L=beat*int(round(N))

	buff_b = [0]*L
	for i in range(0,L):
		if i < len(buff):
			buff_b[i]=buff[i]
		else:
			buff_b[i] = 0.0
	return buff_b

def resize(buff_a,L):
	this_function_name = sys._getframe().f_code.co_name
	NegativeException.check(L,this_function_name) 

	buff_b = [0]*int(round(L))
	for i in range(0,L):
		buff_b[i] = buff_a[i % len(buff_a)]
	return buff_b


#GENERALIZADORES
def method(op, buff, p):
	return globals()[op](buff,p)

def oper(op, buff_a, buff_b):
	if op == ';' or op == 'con':
		return buff_a+buff_b

	op = function[op]

	if len(buff_a) < len(buff_b):
		a = resize(buff_a, len(buff_b))
		b = buff_b
	else:
		a = buff_a
		b = resize(buff_b, len(buff_a))
	buff = [0]*len(a)

	for i in range(0,len(a)):
		buff[i] = op(a[i], b[i])
	return buff

#OPERADORES
def add(a,b):
	return a + b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def mix(a,b):
	return (a+b)/2

function = {'add':add, '+': add,'sub':sub, '-': sub, 'mul':mul, '*': mul, 'div':div, '/':div, 'mix':mix, '&':mix}
