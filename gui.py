#!/usr/bin/env python
import gi
import sys
import time
gi.require_version('Notify', '0.7')
from gi.repository import GLib,Notify
# One time initialization of libnotify
Notify.init("Remember")

TIME_TO_LIVE_MS = 1000 * 60 * 2

# Create the notification object
# Define a callback function
def hard(foo,bar,baz):
    print("hard")


def easy(foo,bar,baz):
    print("easy")

notification = Notify.Notification.new(sys.stdin.read())
notification.add_action(
    "action_click",
    "Show More",
    hard,
    None # Arguments
)

notification.add_action(
    "action_click",
    "Show Less",
    easy,
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
