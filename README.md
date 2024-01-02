# 2FA-Creator

## Clone
    git clone https://github.com/OldKokoroz/2FA-Creator.git

## Usage
    pip install pyotp
    pip install qrcode
    

String in mySecret is like a user ID, program will create 2FA code for specifically that person (id)


## To create 2FA Codes
   - use the default string to create
   - disable reading section in main.py and enable create section for and create random base32, hex string
   - or manually enter a string yourself (within base32, hex rules)


### Program also will keep the logs of login attempts
