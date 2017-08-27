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

def configure_notification(notification):
    result = subprocess.run(['/home/jean/projects/remember_random/get_remember.sh'], stdout=subprocess.PIPE)
    message = str(result.stdout.decode('UTF-8'))
    notification.update(message)

    result = subprocess.run(['/home/jean/projects/personal-scripts/run_function', 'most_relevant_image', message], stdout=subprocess.PIPE)
    image_path = str(result.stdout.decode('UTF-8'))

    my_file = Path(image_path)
    if my_file.is_file():
        image = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                image_path,
                width=200,
                height=200,
                preserve_aspect_ratio=True
                )
        notification.set_image_from_pixbuf(image)
    return notification



notification = Notify.Notification.new('')
notification = configure_notification(notification)

def show_less_frequently(notification,bar,baz):
    m = hashlib.md5()
    m.update(str(notification.get_property('summary')).encode('utf-8'))
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
    p = Popen(['mycopy'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

notification.add_action(
    "copy",
    "Copy",
    send_notification_to_clippboard,
    None
)

def listen_notification(notification,bar,baz):
    p = Popen(['/home/jean/projects/personal-scripts/run_function', 'play_cached_voice'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

notification.add_action(
    "listen",
    "Listen",
    listen_notification,
    None
)

def google_notification(notification,bar,baz):
    p = Popen(['/home/jean/projects/personal-scripts/google_it'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p.communicate(input=str(notification.get_property('summary')).encode('utf-8'))[0]

notification.add_action(
    "google_notification",
    "Google",
    google_notification,
    None
)

notification.set_timeout(NOTIFICATION_TTL_IN_MS)
notification.show()

def new_notification():
    notification = configure_notification(notification)
    notification.show()
    return True

GLib.timeout_add(NOTIFICATION_TTL_IN_MS * 5, new_notification)
GLib.MainLoop().run()
