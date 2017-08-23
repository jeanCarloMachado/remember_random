#!/usr/bin/env python
import gi
import sys
import time
import hashlib
import subprocess
from subprocess import Popen, PIPE, STDOUT
gi.require_version('Notify', '0.7')
from gi.repository import GLib,Notify
Notify.init("Remember")

TIME_TO_LIVE_MS = 1000 * 60 * 2


def show_less(notification,bar,baz):
    m = hashlib.md5()
    m.update(str(notification.get_property('summary')).encode('utf-8'))
    print(m.hexdigest())
    file = open('/home/jean/.config/remember_random/'+m.hexdigest(), 'w')
    file.write("low_recurrence")
    file.close()

def copy(notification,bar,baz):
    p = Popen(['mycopy'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

def listen(notification,bar,baz):
    p = Popen(['/home/jean/projects/personal-scripts/run_function', 'play_cached_voice'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

def google(notification,bar,baz):
    p = Popen(['/home/jean/projects/personal-scripts/google_it'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]


result = subprocess.run(['/home/jean/projects/remember_random/get_remember.sh'], stdout=subprocess.PIPE)
message = result.stdout

notification = Notify.Notification.new(str(message.decode('UTF-8')))
notification.add_action(
    "less",
    "Show Less",
    show_less,
    None
)

notification.add_action(
    "copy",
    "Copy",
    copy,
    None
)

notification.add_action(
    "listen",
    "Listen",
    listen,
    None
)

notification.add_action(
    "google",
    "Google",
    google,
    None
)

notification.set_timeout(TIME_TO_LIVE_MS)
notification.show()

def quit():
    sys.exit(0)
    Notify.uninit()

GLib.timeout_add(TIME_TO_LIVE_MS, quit)
GLib.MainLoop().run()
