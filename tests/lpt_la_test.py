# See http://youtu.be/Sl6mFk-byJA

# Requires pyparallel, only tested on Windows XP
import parallel
port = parallel.Parallel()
 
def reset():
    port.setData(0)
    toggle_p1()
    toggle_p2()
    toggle_p3()
    toggle_p4()
 
def toggle_p1():
    port.setSelect(0)
    port.setSelect(1)
    port.setSelect(0)
   
def toggle_p2():
    port.setInitOut(0)
    port.setInitOut(1)
    port.setInitOut(0)
   
def toggle_p3():
    port.setAutoFeed(0)
    port.setAutoFeed(1)
    port.setAutoFeed(0)
   
def toggle_p4():
    port.setDataStrobe(0)
    port.setDataStrobe(1)
    port.setDataStrobe(0)
   
reset()
for i in range(256):
    port.setData(i)
    toggle_p1()
    toggle_p2()
    toggle_p3()
    toggle_p4()
reset()
