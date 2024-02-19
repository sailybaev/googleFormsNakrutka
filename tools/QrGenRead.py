import json
import qrcode
from tools import FileReader
import cv2

class QRScanner:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback

        self.cap = cv2.VideoCapture(0)

        self.scan_qr_code()

    def json_to_qr(self, json_data , output_file='tempImg.png'):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(json.dumps(json_data))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

    def scan_qr_code(self):
        ret, frame = self.cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detector = cv2.QRCodeDetector()
        value, _, _ = detector.detectAndDecode(gray)

        if value:
            self.callback(value)
            self.master.destroy()

        self.master.after(10, self.scan_qr_code)

    def close_scanner(self):
        self.cap.release()
        self.master.destroy()
