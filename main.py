import pyotp
import qrcode
from time import sleep, strftime, localtime


# Creating a new Secret Key specific for you
# everyone has to have different one
# secret = pyotp.random_base32()

# Saving the Secret Key that just created
# key = open("mySecret", "w")
# secret_save = key.write(secret)
# key.close()

# Using the same Secret Key if you have one
key = open("mySecret", "r")
secret = key.read()
key.close()

# Creating one time password and saving logs
onetime = pyotp.TOTP(secret)
onetime_now = str(onetime.now())

currentDate = strftime("%d-%m-%Y - %H-%M-%S", localtime())

# Getting Credentials
get_user = input("Username : ")
get_pass = input("Password : ")
get_auth = input("2FA Code : ")

twofa = open("keyLogs", "a")
timedCode = twofa.write(f"{currentDate} | {get_user} | {onetime_now}" + "\n")
twofa.close()

# Creating QR Based on the one time Password
qrcode.make(onetime).save(f"{get_user}.png")

trying = 0
while True:
    if not onetime.verify(get_auth):
        sleep(1)
        print("\nInvalid!\n")
        loop_try = input("2FA Code : ")
        get_auth = loop_try
        trying += 1

    if trying == 3:
        print("Enough Guesses")
        exit()

    else:
        print("\nGood to go..")
        exit()
