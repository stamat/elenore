#!/usr/bin/env python

import sys, os
import threading


'''
Heartbeat, the impulse of life.

The heartbeat thread of this program will enable it's basic impulse which will
activate sensory (user input) thread and thought thread. Through thought thread
via the module of interpreting the input, "hormonal" (emotional) parameters will
be set influencingfurther thought process.
'''

bpm = 80
bps = float(60)/bpm

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

counter = 0

def heartbeat():
    global counter
    counter += 1
    print "\a"
    print counter

heart = set_interval(heartbeat, bps)

stop = threading.Event()
input_thread = None

def user_input():
    response = raw_input(">")
    print response

def input_wait():
    global input_thread
    input_thread = threading.Thread(target=user_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(2)

    #an event to cancel the thread  > stop.set()
    if stop.is_set():
        pass
