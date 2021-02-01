#!/usr/bin/env python3
import sys, os, time, csv, datetime, pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import QDate, QDateTime, QTime, QTimer, QEventLoop, QThread, pyqtSignal
from gui import Ui_MainWindow
from setting import Ui_Dialog
from setdate import Ui_Dialog_1

class MainWindow(QMainWindow):
    sinOut3 = pyqtSignal(int)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread = Worker(self)
        self.thread.sinOut1.connect(self.changestatus)
        self.thread.sinOut2.connect(self.DeviceNotification)

    def StartThread(self):    
        self.thread.start()
        
    def changestatus(self, file_inf):
        _translate = QtCore.QCoreApplication.translate
        self.ui.label.setText(_translate("MainWindow", file_inf))
        # time.sleep(3)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.recovery)
        self.timer2.start(3000)
        # self.recovery()

    def dialogbox(self):
        # self.hide()
        self.myDialog = Dialog()
        self.myDialog.showFullScreen()
        # self.myDialog.setStyleSheet("background-color: black;")
    def datatimebox(self):
        # self.hide()
        self.myDialog = Dialog_1()
        self.myDialog.showFullScreen()
        # self.myDialog.setStyleSheet("background-color: black;")

    def recovery(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.label.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:70pt;color:#ffffff;\">歡迎蒞臨 !</span></p><p><span style=\" font-size:70pt;color:#ffffff;\">請出示QR碼</span></p><p><br/></p><p><span style=\" font-size:70pt;color:#ffffff;\">Welcome!</span></p><p><span style=\" font-size:70pt;color:#ffffff;\">Please show your QRcode</span></p></body></html>"
            ))
        self.timer2.stop()

    def DeviceNotification(self, str):
        self.alert = QMessageBox()
        self.alert.setWindowTitle("Notification")
        self.alert.setText(str)
        self.alert.setStandardButtons(QMessageBox.Ok)
        # self.alert.buttonClicked.connect(self.restart)
        # self.alert.exec_()
        # self.alert.buttonClicked.connect(self.msgButtonClick)
        
        self.sinOut3.emit(self.alert.exec()) # HOLD HERE
        #if returnValue == QMessageBox.Ok:

        # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

class Dialog(QMainWindow):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ut = Ui_Dialog()
        self.ut.setupUi(self)

    def mainv(self):
        self.close()
        # self.MW = MainWindow()
        # self.MW.showFullScreen()
        # self.MW.setStyleSheet("background-color: black;")

class Dialog_1(QMainWindow):
    def __init__(self, parent=None):
        super(Dialog_1, self).__init__(parent)
        self.ud = Ui_Dialog_1()
        self.ud.setupUi(self)

    def mainv(self):
        self.close()
        # self.MW = MainWindow()
        # self.MW.showFullScreen()
        # self.MW.setStyleSheet("background-color: black;")

class Worker(QThread):
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        parent.sinOut3.connect(self.comfirm)
        self.returnValue = None

    def comfirm(self, returnValue):
        self.returnValue = returnValue

    def run(self):
        import evdev, os, sys, rsa, base64
        from evdev import InputDevice, categorize, ecodes
        while True:
            command_sda = 'sudo fdisk -l'
            rep_sda = os.popen(command_sda)
            check_usb = str(rep_sda.readlines())
            if '/dev/sda' in check_usb:
                pass
            else:
                self.sinOut2.emit("請插入隨身碟")
                while self.returnValue != 1024:             # HOLD HERE
                    pass
                self.returnValue = None

            command = 'cat /proc/bus/input/devices | grep -A 5 -i HID | grep event'
            device = os.popen(command).readlines()
            if not device:
                self.sinOut2.emit("請插入條碼機")
                while self.returnValue != 1024:             # HOLD HERE
                    pass
                self.returnValue = None
            else:
                device_event = '/dev/input/' + device[0].split()[-1]
                dev = InputDevice(device_event)
                scancodes = {
                    # Scancode: ASCIICode
                    0: None,
                    1: u'ESC',
                    2: u'1',
                    3: u'2',
                    4: u'3',
                    5: u'4',
                    6: u'5',
                    7: u'6',
                    8: u'7',
                    9: u'8',
                    10: u'9',
                    11: u'0',
                    12: u'-',
                    13: u'=',
                    14: u'BKSP',
                    15: u'TAB',
                    16: u'q',
                    17: u'w',
                    18: u'e',
                    19: u'r',
                    20: u't',
                    21: u'y',
                    22: u'u',
                    23: u'i',
                    24: u'o',
                    25: u'p',
                    26: u'[',
                    27: u']',
                    28: u'CRLF',
                    29: u'LCTRL',
                    30: u'a',
                    31: u's',
                    32: u'd',
                    33: u'f',
                    34: u'g',
                    35: u'h',
                    36: u'j',
                    37: u'k',
                    38: u'l',
                    39: u';',
                    40: u'"',
                    41: u'`',
                    42: u'LSHFT',
                    43: u'\\',
                    44: u'z',
                    45: u'x',
                    46: u'c',
                    47: u'v',
                    48: u'b',
                    49: u'n',
                    50: u'm',
                    51: u',',
                    52: u'.',
                    53: u'/',
                    54: u'RSHFT',
                    56: u'LALT',
                    57: u' ',
                    78: u'+',
                    100: u'RALT'
                }

                capscodes = {
                    0: None,
                    1: u'ESC',
                    2: u'!',
                    3: u'@',
                    4: u'#',
                    5: u'$',
                    6: u'%',
                    7: u'^',
                    8: u'&',
                    9: u'*',
                    10: u'(',
                    11: u')',
                    12: u'_',
                    13: u'+',
                    14: u'BKSP',
                    15: u'TAB',
                    16: u'Q',
                    17: u'W',
                    18: u'E',
                    19: u'R',
                    20: u'T',
                    21: u'Y',
                    22: u'U',
                    23: u'I',
                    24: u'O',
                    25: u'P',
                    26: u'{',
                    27: u'}',
                    28: u'CRLF',
                    29: u'LCTRL',
                    30: u'A',
                    31: u'S',
                    32: u'D',
                    33: u'F',
                    34: u'G',
                    35: u'H',
                    36: u'J',
                    37: u'K',
                    38: u'L',
                    39: u':',
                    40: u'\'',
                    41: u'~',
                    42: u'LSHFT',
                    43: u'|',
                    44: u'Z',
                    45: u'X',
                    46: u'C',
                    47: u'V',
                    48: u'B',
                    49: u'N',
                    50: u'M',
                    51: u'<',
                    52: u'>',
                    53: u'?',
                    54: u'RSHFT',
                    56: u'LALT',
                    57: u' ',
                    78: u'+',
                    100: u'RALT'
                }
                x = ''
                caps = False
                with open('/home/pi/private_1024.key', 'rb') as f:
                    privkey = rsa.PrivateKey.load_pkcs1(f.read())

                try:
                    for event in dev.read_loop():
                        if event.type == ecodes.EV_KEY:
                            data = categorize(event)
                            if data.scancode == 42:
                                if data.keystate == 1:
                                    caps = True
                                if data.keystate == 0:
                                    caps = False
                            if data.keystate == 1:
                                if caps:
                                    key_lookup = u'{}'.format(
                                    capscodes.get(data.scancode)
                                ) or u'UNKNOWN:[{}]'.format(
                                    data.scancode)  # Lookup or return UNKNOWN:XX
                                else:
                                    key_lookup = u'{}'.format(
                                    scancodes.get(data.scancode)
                                ) or u'UNKNOWN:[{}]'.format(
                                    data.scancode)  # Lookup or return UNKNOWN:XX
                                if (data.scancode != 42) and (data.scancode != 28):
                                    x += key_lookup
                                if (data.scancode == 28):
                                    try:
                                        encrypted_str = x
                                        encrypted_str = encrypted_str.encode()
                                        encrypted_str = base64.b64decode(encrypted_str)
                                        decrypted_str = rsa.decrypt(encrypted_str, privkey)
                                    except Exception as e:
                                        file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#de0101;\">INVALID</span></p></body></html>"
                                        self.sinOut1.emit(file_str)
                                        continue
                                    else:
                                        decrypted_str = decrypted_str.decode()
                                        self.checkData(decrypted_str)
                                    finally:
                                        x = ''
                except:
                    self.sinOut2.emit("請插回條碼機")
                    while self.returnValue != 1024:             # HOLD HERE
                        pass
                    self.returnValue = None

        # except OSError:
        #     self.DeviceNotification("Please check QR scanner")

    def checkData(self, msg):
        data = msg
        t = time.time()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        try:
            msg_name, checkNumber,NumberGroup, msg_date, msg_time,msg_serial = msg.split('-')
            msg_datetime = msg_date + "-" + msg_time
            # msg[0:6], msg[7],msg[8], msg[9:28], msg[29:]
        except Exception as e:
            file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#de0101;\">INVALID</span></p></body></html>"
            self.sinOut1.emit(file_str)
        else:
            if (msg_name == 'sinica'):
                msgUnixTime = time.mktime(
                    datetime.datetime.strptime(
                        msg_datetime, "%Y/%m/%d-%H:%M:%S").timetuple())
                surviveTime = msgUnixTime - t
                if (checkNumber == 'Y' and surviveTime > 0):
                    file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#22de01;\">PASS</span></p><p><span style=\" font-size:48pt; color:#7a9bdf;\">通行人數："+ NumberGroup + "</span></p></body></html>"
                    self.sinOut1.emit(file_str)
                    pygame.mixer.music.load('/home/pi/Scan/voice/pass.mp3')
                    pygame.mixer.music.play()
                    self.SaveData(msg_name, checkNumber ,NumberGroup, msg_datetime,
                                  msg_serial)
                elif (checkNumber == 'Y' and surviveTime <= 0):
                    file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#de0101;\">INVALID</span></p><p><span style=\" font-size:48pt; color:#ffa964;\">通行碼逾時</span></p></body></html>"
                    self.sinOut1.emit(file_str)
                    pygame.mixer.music.load('/home/pi/Scan/voice/no.mp3')
                    pygame.mixer.music.play()
                    self.SaveData(msg_name, checkNumber ,NumberGroup, msg_datetime,
                                  msg_serial)
                else:
                    file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#de0101;\">INVALID</span></p></body></html>"
                    self.sinOut1.emit(file_str)
                    pygame.mixer.music.load('/home/pi/Scan/voice/no.mp3')
                    pygame.mixer.music.play()
                    self.SaveData(msg_name, checkNumber, NumberGroup, msg_datetime,
                                  msg_serial)
            else:
                file_str = "<html><head/><body><p><span style=\" font-size:144pt; color:#de0101;\">invalid</span></p></body></html>"
                self.sinOut1.emit(file_str)
                pygame.mixer.music.load('/home/pi/Scan/voice/no.mp3')
                pygame.mixer.music.play()

    def SaveData(self, msg_name, checkNumber, NumberGroup, msg_datetime, msg_serial):
        # node = uuid.getnode()
        # mac = uuid.UUID(int=node)
        # addr = mac.hex[-12:]
        addr = os.popen("ifconfig | grep ether | awk {'print $2'} | sed -r 's/://g'").readline().strip('\n')
        date = datetime.datetime.today()
        date_str = date.strftime("%Y%m%d")
        Datetime = datetime.datetime.now()
        Datetime_str = date.strftime("%Y/%m/%d-%H:%M:%S")
        with open('/home/pi/Scan/DeviceName.txt', 'r') as f:
            DeName = f.readline()
        path = "/home/pi/log/" + date_str + "-" + addr + "-log.csv"
        with open(path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                DeName, addr, Datetime_str, msg_datetime, msg_name,
                checkNumber, NumberGroup, msg_serial
            ])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showFullScreen()
    win.setStyleSheet("background-color: black;")
    win.StartThread()
    sys.exit(app.exec_())
    # test2
