import socket
import subprocess
import tempfile
import traceback
import SocketServer as socketserver
import os
path = os.path.dirname(os.path.abspath(__file__))
print(path)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    allow_reuse_address = True
    def handle(self):
        s = self.request
        s.send(b"HAI! WELCOME TO LOLD: WE HAZ DA BEEEEEEST LOLPYTH INTERPRETER YOU EVER DID SEE!!\n")
        s.send(b"GIMME ONE LOLPYTHON SCRIPT AND MAYB I RUN 4 U!\n")
        inp = s.recv(1024)
        
        with tempfile.NamedTemporaryFile(mode="wb") as lolfd:
            lolfd.write(inp)
            lolfd.flush()
            try:
                out = subprocess.check_output(["python", os.path.join(path,"lolpython.py"), "--convert", lolfd.name]).decode('utf-8').strip()
            except subprocess.CalledProcessError:
                s.send(b"ERMMM NO...SRY....KTHXBYE\n")
                traceback.print_exc()
                s.close()
                return
            try:
                out = subprocess.check_output(["python", lolfd.name + ".py"]).decode('utf-8').strip()
                print(out)
            except subprocess.CalledProcessError:
                s.send(b"ERMMM NO...SRY....KTHXBYE\n")
                traceback.print_exc()
                s.close()
                return
            s.send(out.encode('utf-8'))
            s.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    pass

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 1337
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.serve_forever()