#!/usr/bin/python3

'''
A minimal gtk application demo.
'''

import gtk  # for Button, Window, main, main_quit


def clicked_callback(b):
    b.set_label('Hello World!' + str(b.num))
    b.num += 1


def quit_callback(window, event):
    gtk.main_quit()

b = gtk.Button('Click me')  # create a button
b.num = 0  # attache some data to it
b.connect('clicked', clicked_callback)  # attach it to the callback

w = gtk.Window()  # create a new window
w.add(b)  # put it inside the window
w.connect('delete-event', quit_callback)
w.show_all()  # must do this in GTK

'''
The try/except is needed so that if you CTRL+C the application you will not get an exception
with stack trace
'''
try:
    gtk.main()  # main loop. Will only quit if you call 'gtk.main_quit()'
except:
    pass
