#!/usr/bin/env python

import gi
import sys
import signal
import time
import hashlib
import subprocess
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
gi.require_version('Notify', '0.7')
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GLib,Notify,GdkPixbuf
import os

Notify.init("Remember")

NOTIFICATION_TTL_IN_MS = 1000 * 60 * 2

message = sys.stdin.read()

if len(message) < 100:
    notification = Notify.Notification.new(message)
else:
    notification = Notify.Notification.new('', message)

notification.set_timeout(NOTIFICATION_TTL_IN_MS)

image_path = subprocess.run(['mostRelevantImage.sh', message], stdout=subprocess.PIPE).stdout.decode('UTF-8')

my_file = Path(image_path)
if my_file.is_file():
    image = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            image_path,
            width=200,
            height=200,
            preserve_aspect_ratio=True
            )
    notification.set_image_from_pixbuf(image)

def show_less_frequently(notification,bar,baz):
    global message
    m = hashlib.md5()
    m.update(message)
    print(m.hexdigest())
    file = open(os.path.dirname(os.path.realpath(__file__))+m.hexdigest(), 'w')
    file.write("low_recurrence")
    file.close()

notification.add_action(
    "less",
    "Show Less",
    show_less_frequently,
    None
)

def listen_notification(notification,bar,baz):
    global message
    p = Popen(['playVoice.sh'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    "listen",
    "Listen",
    listen_notification,
    None
)

def google_notification(notification,bar,baz):
    global message
    p = Popen(['googleit.sh'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    "google_notification",
    "Google",
    google_notification,
    None
)

def edit_notification(notification,bar,baz):
    global message
    p = Popen(['editRemember.sh'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    'clicked',
    'Edit',
    edit_notification,
    None
)

notification.show()
def quit():
    sys.exit()

GLib.timeout_add(NOTIFICATION_TTL_IN_MS, quit)

try:
    GLib.MainLoop().run()
except:
    quit()

