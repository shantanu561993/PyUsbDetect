import dbus
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)
 
bus = dbus.SystemBus()


# Function which will run when signal is received
def callback_function(*args):
    print len(args[1])
    print args[1]
# Which signal to have an eye for
iface  = 'org.freedesktop.DBus.ObjectManager'
signal = 'InterfacesAdded'
bus.add_signal_receiver(callback_function, signal, iface)
 
# Let's start the loop
import gobject
loop = gobject.MainLoop()
loop.run()
