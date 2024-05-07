import pyotp
import qrcode
from time import sleep, strftime, localtime


class Auth:
    def __init__(self) -> None:
        self.currentDate = strftime("%d-%m-%Y - %H-%M-%S", localtime())
        self.secret = ""
        self.key = ""

    def create_otp(self):
        # Creating one time password and saving logs
        self.onetime = pyotp.TOTP(self.secret)
        self.onetime_now = str(self.onetime.now())
        print(self.onetime_now)

    def create_pass(self):
        # Creating a new Secret Key specific for you
        self.secret = pyotp.random_base32()

        # Saving the Secret Key that just created
        self.key = open("mySecret.txt", "w")
        self.key.write(self.secret)
        self.key.close()

    def get_sec(self):
        # Using the same Secret Key if you have one
        self.key = open("mySecret.txt", "r")
        self.secret = self.key.read()
        self.key.close()

    def get_cred(self):
        # Getting Credentials
        self.get_user = input("Username : ")
        self.get_pass = input("Password : ")
        self.get_auth = input("2FA Code : ")

        twofa = open("keyLogs", "a")
        timedCode = twofa.write(f"{self.currentDate} | {self.get_user} | {self.onetime_now}" + "\n")
        twofa.close()

    def create_qr(self):
        # Creating QR Based on the one time Password
        qrcode.make(self.onetime).save(f"{self.get_user}.png")

        trying = 0
        while True:
            if not self.onetime.verify(self.get_auth):
                sleep(1)
                print("\nInvalid!\n")
                loop_try = input("2FA Code : ")
                self.get_auth = loop_try
                trying += 1

            if trying == 3:
                print("Enough Guesses")
                exit()

            else:
                print("\nGood to go..")
                exit()

runner = Auth()
# runner.create_otp()
runner.get_sec()
runner.get_cred()
runner.create_qr()
