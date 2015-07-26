__author__ = 'shantanu'

import dbus

bus = dbus.SystemBus()

ud_manager_obj = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")

ud_manager = dbus.Interface(ud_manager_obj, 'org.freedesktop.UDisks')

for device in ud_manager.EnumerateDevices():
            device_obj = bus.get_object("org.freedesktop.UDisks", device)
            device_props = dbus.Interface(device_obj, dbus.PROPERTIES_IFACE)
            print(device_props.Get('org.freedesktop.UDisks.Device', "DriveSerial"), device_props.Get('org.freedesktop.UDisks.Device', "DriveVendor"))