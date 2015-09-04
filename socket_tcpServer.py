from socket import *
import threading
import time 

class MyServer(object):
  '''initialization socket '''
  def __init__(self,host='',port=20456,bufsize=1024,listen=3):
    self.host = host
    self.port = port
    self.bufsize = bufsize
    self.listen = listen
    
    self.conn = socket(AF_INET,SOCK_STREAM)
    self.conn.bind(self.addr)
    self.conn.listen(self.listen)
  
  def startListen(self):
    obj,addr = self.conn.accept()
    return (obj,addr)
    
  def conmunicate(self,cli):
    tcpCli = cli[0]
    tcpAddr = cli[1]
    
    while True:
      data = tcpCli.recv(self.bufsize)
      if not data:break
      tcpCli.send('[%s] %s'%(time.ctime(),data))
    
    print tcpAddr,'close...'
    tcpCli.close()
    
  def run(self):
    while True:
      print 'waiting to connect...'
      cli = self.startListen()
      print time.ctime(),'connected to:',a[1]
      thread1 = threading.Thread(target=self.conmunicate,args=(cli,))
      thread1.start()
      
      
      
if __name__ == '__main__':
  test = MyServer()
  test.run()
    
