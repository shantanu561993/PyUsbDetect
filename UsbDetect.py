from __future__ import  print_function
__author__ = 'shantanu'
try:
    import dbus
    import gobject
    from dbus.mainloop.glib import DBusGMainLoop
except ImportError:
    print("python d-bus is not installed")
import subprocess



def check_udisks():
    p = subprocess.Popen("whereis udisks", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if "/bin/" in output:
        print("Udisks is installed ")
    else:
        print("Udisks is not installed")

check_udisks()


bus = dbus.SystemBus()

ud_manager_obj = bus.get_object("org.freedesktop.UDisks2", "/org/freedesktop/UDisks")

ud_manager = dbus.Interface(ud_manager_obj, 'org.freedesktop.UDisks')

for device in ud_manager.EnumerateDevices():
            device_obj = bus.get_object("org.freedesktop.UDisks", device)
            device_props = dbus.Interface(device_obj, dbus.PROPERTIES_IFACE)
            print(device_props.Get('org.freedesktop.UDisks.Device', "DriveSerial"), device_props.Get('org.freedesktop.UDisks.Device', "DriveVendor"))