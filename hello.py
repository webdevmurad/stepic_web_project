# WSGI
def application(environ, start_response)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    queryString = environ['QUERY_STRING'].split('&')
    responseBody = ''
    for i in queryString: 
        responseBody += i + '\n'
    return responseBody