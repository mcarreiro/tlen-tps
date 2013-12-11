import math
import numpy
global beat
beat = 12

#GENERADORES
def sin(c,a):
	buff = [0]*beat
	x = (c*2*(math.pi))/beat
	for i in range(0,beat):
		buff[i] = a* (math.sin(i*x))
	return buff

def lin(a,b):
	return numpy.linspace(a,b,beat)

def sil():
	return [0]*beat

def noi(a):
	return numpy.random.random_sample(size=beat)*a

#METODOS
def post(buff):
	cadena = ""
	for i in range(0,len(buff)):
		cadena= cadena+" " +str(buff[i])
	print cadena

def loop(buff,R):
	buff_r = []
	for i in range(0,R):
		buff_r = buff_r + buff
	return buff_r

			
def resample(buff_a,L):
	buff_b =[0]*L
	for i in range(0,L):
		buff_b[i] = buff_a[i*len(buff_a)//L]
	return buff_b

def tune(buff , P):
	return resample(buff,int(len(buff)*((2**(1.0/beat))**-P)))

def reduce(buff, N):
	L = beat*N
	if len(buff)>N:
		return resample ( buff , N)
	else:
		return buff

def expand(buff, N):
	L = beat*N
	if len(buff)<N:
		return resample ( buff , N)
	else:
		return buff

def fill(buff,N):
	L=beat*N
	buff_b = [0]*L
	for i in range(0,L):
		if i < len(buff):
			buff_b[i]=buff[i]
		else:
			buff_b[i] = 0.0
	return buff_b

def resize(buff_a,L):
	buff_b = [0]*L
	for i in range(0,L):
		buff_b[i] = buff_a[i % len(buff_a)]
	return buff_b

def method(op, buff, p):
	return op(buff,p)

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

funtion = 
	{'add':add, '+': add,
	 'sub':sub, '-': sub,
	 'mul':mul, '*': mul,
	 'div':div, '/':div,
	 'mix':mix, '&':mix
	}

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
