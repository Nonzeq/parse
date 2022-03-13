# parse

parse.sh = #!/bin/bash
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
export DISPLAY=:0 && /usr/bin/python /home/bogdan/parse/parse.py

crontab -e =  */30 17 * * * export DISPLAY=:0.0 && /home/name/parse.sh >> /home/name/log 2>&1
