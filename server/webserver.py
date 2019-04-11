#create a simple web server

import SimpleHTTPServer
import SocketServer

eventHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

myhttpserver = SocketServer.TCPServer(("0.0.0.0", 8080), eventHandler)

print "My server is now running (Ctrl-c to stop)..."

myhttpserver.serve_forever()
