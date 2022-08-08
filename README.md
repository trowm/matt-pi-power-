# matt-pi-power - badly and maybe well hacked from pi-power

[Much kudos to the penguintutor/pi-power](https://github.com/penguintutor/pi-power) from whence my hacking originated.

Putting this out there, maybe someone will find it useful. Certainly pi-power was to me!
This isn't intended to be anything other than a personal project.

I've got an old Pi-mote with sockets - this - https://energenie4u.co.uk/catalogue/product/ENER002-2PI

My needs are quite simply, a single socket, which I can use to turn on and off a heater in my home office shed.

Nothing more, nothing less. 

As such, the code here is hacked together, [view the repo](https://github.com/penguintutor/pi-power) from where I got part of my solution.

The bad hacking, is the python work - still haven't cleaned that up, but it's pretty much single socket only now.
If I need two sockets, I'll add to it. Some bits of laziness here, but I wasn't keen to go the "whole hog" and remove ALL multi-socket functionality, lest I decide to employ the second socket I got with my kit. Then I'll rewrite it.

The ... possibly ... good hacking, is it's now plain JS, so vastly simplified. No images, no Jquery. But has the concept of a SINGLE switch, which would be relatively easy to modify.

My needs are really that I can use my mobile phone from anywhere in my house, to override the cron job I've setup.
If I decide to start work a little early, in colder months, rather than relying on the cron timer I've setup, the web interface allows me to turn it on remotely, so by the time I've had my breakfast, my shed will be warm.

I've also added the concept of "status" of the switch, by way of writing 'true' or 'false' to a file.
Because the pi-mote is a closed loop, there's NO way to actually get the status of a socket. None. Zip. Nada.

All I wanted, in the web-interface, is to KNOW the status and to be able to overide the cron-job I setup, compliments to [Pengin Tutor - pi-power](http://www.penguintutor.com/raspberrypi/pi-power)

## Some resources

* [penguintutor/pi-power](https://github.com/penguintutor/pi-power)
* [gpiozero/Energenie](https://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=Energenie#gpiozero.Energenie)
* [Product - Pi-mote Control starter kit with 2 sockets](https://energenie4u.co.uk/catalogue/product/ENER002-2PI)
* [Python docs](https://docs.python.org/3/)


# Credits due

[Stewart Watkiss](https://github.com/penguintutor)

