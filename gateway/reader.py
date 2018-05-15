import time
import serial
import os
import requests


def serial_daemon():
    print('Serial thread Started')
    serial1 = serial.Serial('/dev/ttyS2', 9600, timeout=0)
    while True:
        time.sleep(1)
        try:
            s = serial1.readline()
            data = s.decode('utf-8')
            if data and data is not '' and data is not '\n' and data is not '\r' and data is not None:
                serial_data = data.split('*')[1]
                url = 'http://165.227.112.56:5000/api/datos'
                payload = {'data': serial_data}
                r = requests.post(url, json=payload)
        except(KeyboardInterrupt, SystemExit):
            print('Closing...')
            s1.close()
            raise


if __name__ == '__main__':
    print("habilitando serial...")
    os.system('echo BB-UART2 > /sys/devices/platform/bone_capemgr/slots')
    print("cambiando a PAN ID 4566...")
    os.system('echo \'+4566\\n\' > /dev/ttyS2')
    print("leyendo datos")
    serial_daemon()
