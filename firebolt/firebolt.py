from wsgiref.simple_server import make_server

def application(environment, start_response):
    start_response("200 OK", [])
    return [b"Hello World!"]


with make_server("", 8000, application) as server:
    print("Serving on port 8000...")
    server.serve_forever()
