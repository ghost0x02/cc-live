import time
import os
from colorama import Fore, Style

os.system("clear")
print(Fore.MAGENTA + '')
print("""
_________________   ________________    ___________
__  ____/_  ____/   ___  /____  _/_ |  / /__  ____/
_  /    _  /        __  /  __  / __ | / /__  __/
/ /___  / /___      _  /____/ /  __ |/ / _  /___
\____/  \____/      /_____/___/  _____/  /_____/1.0v""")
print("CODED BY ENESXSEC ANG GHOST0X02 ")
print(Style.RESET_ALL)
print(Fore.GREEN + '')

def is_valid_credit_card(number):
    digits = [int(x) for x in str(number)]
    checksum = digits.pop()

    digits.reverse()
    doubled = [2 * digit for digit in digits[::2]]
    total = sum(digit if digit < 10 else digit - 9 for digit in doubled) + sum(digits[1::2])

    return (total + checksum) % 10 == 0

def get_card_info(number):
    card_type = "visa"
    card_type = "Mastercard"
    bank_name = "Bilinmeyen" 

    if number.startswith("4"):
        card_type = "Visa"
    elif number.startswith(("51", "52", "53", "54", "55")):
        card_type = "Mastercard"
    elif number.startswith("34") or number.startswith("37"):
        card_type = "American Express"
    elif number.startswith("6"):
        card_type = "Discover"
    elif number.startswith("46") or number.startswith("1046"):
        card_type = "Akbank"
        bank_name = "Akbank"
    elif number.startswith("67"):
        card_type = "Yapıkredi"
        bank_name = "Yapıkredi"
    elif number.startswith("62"):
        card_type = "Garanti Bankası"
        bank_name = "Garanti Bankası"
    elif number.startswith("6304") or number.startswith(("6706", "6771", "6709")):
        card_type = "Laser"
    elif number.startswith("40") or number.startswith("51") or number.startswith("52") or number.startswith("53"):
        card_type = "Barclays"
        bank_name = "Barclays"
    elif number.startswith("49"):
        card_type = "Deutsche Bank"
        bank_name = "Deutsche Bank"
    elif number.startswith("55"):
        card_type = "ING Bank"
        bank_name = "ING Bank"
    elif number.startswith("62"):
        card_type = "ICBC"
        bank_name = "ICBC"
    elif number.startswith("45"):
        card_type = "SMBC"
        bank_name = "SMBC"
    elif number.startswith("63"):
        card_type = "TEB"
        bank_name = "TEB"
def main():
  credit_card_number = input("Kredi kartı numarasını girin: ")
    print(Fore.RED + '''
 ██████╗ █████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║     ███████║██████╔╝██║  ██║
██║     ██╔══██║██╔══██╗██║  ██║
╚██████╗██║  ██║██║  ██║██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ''')
    print(Fore.GREEN + '')

    if is_valid_credit_card(credit_card_number):
        time.sleep(0.5)
        print("---------------")
        print("Kart Durumu --> geçerli.")
        print("---------------")
        card_type, bank_name = get_card_info(credit_card_number)
        time.sleep(0.5)
        print("---------------")
        print("Kart tipi:", card_type)
        print("---------------")
        time.sleep(0.7)
        print("Banka:", bank_name)
    else:
        print("Kart geçersiz.")

if __name__ == "__main__":
    main()

    return card_type, bank_name



