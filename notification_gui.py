#!/usr/bin/env python

import gi
import sys
import time
import hashlib
import subprocess
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
gi.require_version('Notify', '0.7')
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GLib,Notify,GdkPixbuf
Notify.init("Remember")

NOTIFICATION_TTL_IN_MS = 1000 * 60 * 2

message = sys.stdin.read()

if len(message) < 500:
    notification = Notify.Notification.new(message)
else:
    notification = Notify.Notification.new('', message)

notification.set_timeout(NOTIFICATION_TTL_IN_MS)

image_path = subprocess.run(['/home/jean/projects/personal-scripts/run_function', 'most_relevant_image', message], stdout=subprocess.PIPE).stdout.decode('UTF-8')

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
    file = open('/home/jean/.config/remember_random/'+m.hexdigest(), 'w')
    file.write("low_recurrence")
    file.close()

notification.add_action(
    "less",
    "Show Less",
    show_less_frequently,
    None
)

def send_notification_to_clippboard(notification,bar,baz):
    global message
    p = Popen(['mycopy'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    "copy",
    "Copy",
    send_notification_to_clippboard,
    None
)

def listen_notification(notification,bar,baz):
    global message
    p = Popen(['/home/jean/projects/personal-scripts/run_function', 'play_cached_voice'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    "listen",
    "Listen",
    listen_notification,
    None
)

def google_notification(notification,bar,baz):
    global message
    p = Popen(['/home/jean/projects/personal-scripts/google_it'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=message.encode('utf-8'))

notification.add_action(
    "google_notification",
    "Google",
    google_notification,
    None
)

def edit_notification(notification,bar,baz):
    global message
    p = Popen(['/home/jean/projects/personal-scripts/run_function', 'terminal_run', 'run_function edit_remember "'+message+'"'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

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
GLib.MainLoop().run()
