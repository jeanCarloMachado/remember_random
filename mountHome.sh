#!/bin/bash

mount -t cifs -o username=shared,password=shared //192.168.0.66/HD /media/homeHd
mount -t cifs -o username=shared,password=shared //192.168.0.66/SHARED /media/homeShared
mount -t cifs -o username=shared,password=shared //192.168.0.66/SAMBA /media/homeShared2
