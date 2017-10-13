import sys

if sys.argv[1] == "server":
    from wsgiref.simple_server import make_server
    from .application import application
    with make_server("", 8001, application) as server:
        print("Serving on port 8001...")
        server.serve_forever()
