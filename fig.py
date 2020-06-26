from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if '' not in [a, b]:
	try:
            a, b= int(a), int(b)
	except ValueError:
	    a = error
	    b = 0
    else:
	a, b= 1,1
    x = a+b
    y = a*b
    with open('/var/www/html/img/result.txt','w')as f:
	f.write("sum = {}, multiplied = {}".format(x,y))
		
    response_body = html.replace("TEST","sum = "+str(x)+" multiplied = "+str(y))
    
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
 
