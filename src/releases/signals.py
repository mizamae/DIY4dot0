import django.dispatch

from . import signal_handlers

Device_datagram_reception= django.dispatch.Signal(providing_args=["timestamp","DeviceName","DatagramId","values"])
Device_datagram_reception.connect(Devices.signal_handlers.Device_datagram_reception_handler)

Device_datagram_exception= django.dispatch.Signal(providing_args=["DeviceName","DatagramId","HTMLCode"])
Device_datagram_exception.connect(Devices.signal_handlers.Device_datagram_exception_handler)

Device_datagram_timeout= django.dispatch.Signal(providing_args=["DeviceIP","DeviceName","DatagramId"])
Device_datagram_timeout.connect(Devices.signal_handlers.Device_datagram_timeout_handler)

Device_datagram_format_error= django.dispatch.Signal(providing_args=["DeviceName","DatagramId","values"])
Device_datagram_format_error.connect(Devices.signal_handlers.Device_datagram_format_error_handler)
