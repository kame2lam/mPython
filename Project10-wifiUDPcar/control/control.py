import pgzrun
import socket

def UDP_send(MESSAGE):
    UDP_IP = "192.168.4.1"
    UDP_PORT = 100
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

WIDTH = 600
HEIGHT = 600
bg=Actor('bg')
up=Actor('up',(300,100))
stop=Actor('stop',(300,300))
left=Actor('left',(100,300))
right=Actor('right',(500,300))
down=Actor('down',(300,500))

def draw():
    bg.draw()
    up.draw()
    stop.draw()
    left.draw()
    right.draw()
    down.draw()

def update():
    pass

def on_mouse_down(pos):
    if up.collidepoint(pos):
        UDP_send("f")
    if stop.collidepoint(pos):
        UDP_send("s")
    if left.collidepoint(pos):
        UDP_send("l")
    if right.collidepoint(pos):
        UDP_send("r")
    if down.collidepoint(pos):
        UDP_send("b")

pgzrun.go()