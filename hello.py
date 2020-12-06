# WSGI

def app(env, start_response)
    data = ''
    data = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return data