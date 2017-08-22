#!/usr/bin/env python
import gi
import sys
import time
import hashlib
from subprocess import Popen, PIPE, STDOUT
gi.require_version('Notify', '0.7')
from gi.repository import GLib,Notify
# One time initialization of libnotify
Notify.init("Remember")

TIME_TO_LIVE_MS = 1000 * 60 * 2


def show_less(notification,bar,baz):
    m = hashlib.md5()
    m.update(str(notification.get_property('summary')).encode('utf-8'))
    print(m.hexdigest())

def copy(notification,bar,baz):
    print('copy')
    p = Popen(['mycopy'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

def listen(notification,bar,baz):
    print('listen')

notification = Notify.Notification.new(sys.stdin.read())
notification.add_action(
    "less",
    "Show Less",
    show_less,
    None # Arguments
)

notification.add_action(
    "copy",
    "Copy",
    copy,
    None # Arguments
)

notification.add_action(
    "listen",
    "Listen",
    listen,
    None # Arguments
)
# Actually show on screen
notification.set_timeout(TIME_TO_LIVE_MS)
notification.show()

def quit():
    sys.exit(0)
    Notify.uninit()

GLib.timeout_add(TIME_TO_LIVE_MS, quit)
GLib.MainLoop().run()
