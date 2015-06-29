import explorerhat
from time import sleep

def rotateleft(channel, event):
    explorerhat.light.red.blink(0.5,0.5)
    duration = 0.5
    explorerhat.motor.one.forward(100)
    sleep(duration)
    explorerhat.motor.one.stop()
    explorerhat.light.off()

def rotateright(channel, event):
    explorerhat.light.green.blink(0.5,0.5)
    duration = 0.5
    explorerhat.motor.one.backward(100)
    sleep(duration)
    explorerhat.motor.one.stop()
    explorerhat.light.off()

def winchdown(channel, event):
    explorerhat.light.yellow.blink(0.5,0.5)
    duration = 0.5
    explorerhat.motor.two.forward(100)
    sleep(duration)
    explorerhat.motor.two.stop()
    explorerhat.light.off()

def winchup(channel, event):
    explorerhat.light.blue.blink(0.5,0.5)
    duration = 0.5
    explorerhat.motor.two.backward(100)
    sleep(duration)
    explorerhat.motor.two.stop()
    explorerhat.light.off()

 def magnet(channel, event):
 	explorerhat.output.one.toggle()

explorerhat.touch.one.pressed(rotateleft)
explorerhat.touch.two.pressed(rotateright)
explorerhat.touch.three.pressed(winchdown)
explorerhat.touch.four.pressed(winchup)
explorerhat.touch.eight.pressed(magnet)

  
