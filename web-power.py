#!/usr/bin/env python3
# Web remote for the Energenie Pi remote
# see http://www.penguintutor.com/
# Copyright Stewart Watkiss 2014-2015


# web-power is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>

import time
from gpiozero import Energenie
import bottle
from bottle import request, static_file

sockets = [None]
sockets.append(Energenie(1))

# allow on all ip addresses
HOST = ''
# port 80 - standard web port (assumes no other web server installed)
# If using apache or another browser then change this to a different value
PORT = 80

# Folder where this is installed and the index.html file is located
# The index.html file is exposed to the webserver as well as any files in a subdirectory called public (ie. /home/pi/pi-power/public) 
DOCUMENT_ROOT = '/home/pi/matt-pi-power-'

# Create the bottle web server
app = bottle.Bottle()

def write_status(status):
    f = open(DOCUMENT_ROOT+'/state.txt', 'w', encoding="utf-8")
    f.write(status)

# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD BY ANYONE CONNECTED TO THE SAME NETWORK ***
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")

# Handle switch request
@app.route ('/switch')
def switch():
    socket = int(request.query.socket)
    # If single socket requested
    if (socket > 0 and socket <= 4) :
        #print 'Switching on {}'.format(socket)
        if (sockets[socket].value == True) :
            time.sleep(0.5)
            sockets[socket].off()
            time.sleep(0.5)

            # Set switch "status"
            # the pi-mote is a closed loop - one way only, so it's impossible to get the real
            # status of a socket, so this just writes it to a file
            # Currently, this has no functionality for anything other than a single socket,
            # because that's all I use. 
            write_status('false')
            return 'off'
        else :
            time.sleep(0.5)
            sockets[socket].on()
            time.sleep(0.5)
            write_status('true')
        return 'on'
    else :
        return 'Invalid request'

# Get switch "status"
# the pi-mote is a closed loop - one way only, so it's impossible to get the real
# status of a socket. 
@app.route ('/status')
def get_status():
    f = open(DOCUMENT_ROOT+'/state.txt', 'r', encoding="utf-8")
    return f.readline()


# Serve up the default index.html page
@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT)

app.run(host=HOST, port=PORT)