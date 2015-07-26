import dbus
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)
 
bus = dbus.SystemBus()


# Function which will run when signal is received
def callback_function(*args):
    device_props = args[1].get('org.freedesktop.UDisks2.Drive')
    if device_props:
        device_id = device_props['Serial']
        vendor = device_props['Vendor']
        print device_id,vendor, args[0]
    # print len(args[1])
    # print args[1]
    # for key,value in args[1].iteritems():
    #     print key,value
    #     if key == 'org.freedesktop.UDisks2.Drive':
    #         print "olala"
    # drive_props = args[1].get('org.freedesktop.UDisks2.Drive')
    # print "jshdkjahd" , drive_props
    print args[0]


# Which signal to have an eye for
iface  = 'org.freedesktop.DBus.ObjectManager'
signal = 'InterfacesAdded'
bus.add_signal_receiver(callback_function, signal, iface)
 
# Let's start the loop
import gobject
loop = gobject.MainLoop()
loop.run()
