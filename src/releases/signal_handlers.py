import logging
logger = logging.getLogger("project")

def Device_datagram_reception_handler(sender, **kwargs):
    timestamp=kwargs['timestamp']
    deviceName=kwargs['DeviceName']
    datagramID=kwargs['DatagramId']
    values=kwargs['values']
    print("SIGNALS: The device "+ deviceName+" responded OK to the datagram " + str(datagramID)+" with values= "+str(values))
    
def Device_datagram_exception_handler(sender, **kwargs):
    deviceName=kwargs['DeviceName']
    datagramID=kwargs['DatagramId']
    HTMLCode=kwargs['HTMLCode']
    print("SIGNALS: The device "+ deviceName+" responded to the datagram " + str(datagramID)+" with the code "+str(HTMLCode))
    logger.error("SIGNALS: The device "+ deviceName+" responded to the datagram " + str(datagramID)+" with the code "+str(HTMLCode))
    
def Device_datagram_timeout_handler(sender, **kwargs):
    deviceIP=kwargs['DeviceIP']
    deviceName=kwargs['DeviceName']
    datagramID=kwargs['DatagramId']
    print("SIGNALS: The device "+ deviceName+" at "+ deviceIP +" did not respond to the datagram " + str(datagramID))
    logger.warning ("SIGNALS: The device "+ deviceName+" at "+ deviceIP +" did not respond to the datagram " + str(datagramID))

def Device_datagram_format_error_handler(sender, **kwargs):
    deviceName=kwargs['DeviceName']
    datagramID=kwargs['DatagramId']
    values=kwargs['values']
    print("SIGNALS: The device "+ deviceName+" responded with a wrong format to the datagram " + str(datagramID)+" with values= "+str(values))
    logger.warning("SIGNALS: The device "+ deviceName+" responded with a wrong format to the datagram " + str(datagramID)+" with values= "+str(values))