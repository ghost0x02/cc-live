import time
import os
from termcolor import colored

def clear_screen():
    os.system("clear")

def print_header():
    clear_screen()
    print(colored("""
    _________________   _______________________________
    __  ____/_  ____/   ___  /____  _/_ |  / /__  ____/
    _  /    _  /        __  /  __  / __ | / /__  __/
    / /___  / /___      _  /____/ /  __ |/ / _  /___
    \____/  \____/      /_____/___/  _____/  /_____/1.0v""", "magenta"))
    print(colored("CODED BY ENESXSEC AND GHOST0X02 ", "red"))
    print(colored("KART NUMARASI GİRERKEN BOŞLUK BIRAKMAYINIZ", "green"))
    print(colored("-----------------------------------------------------------------", "green"))

def is_valid_credit_card(number):
    digits = [int(x) for x in str(number)]
    checksum = digits.pop()
    digits.reverse()
    doubled = [2 * digit for digit in digits[::2]]
    total = sum(digit if digit < 10 else digit - 9 for digit in doubled) + sum(digits[1::2])
    return (total + checksum) % 10 == 0

def get_card_info(number):
    card_types = {
        "4": "Visa",
        "51": "Mastercard",
        "52": "Mastercard",
        "53": "Mastercard",
        "54": "Mastercard",
        "55": "Mastercard",
        "37": "American Express",
        "97": "Troy",
        "65": "Troy",
        "6011": "Discover",
        "300": "Diners Club",
        "301": "Diners Club",
        "302": "Diners Club",
        "303": "Diners Club",
        "304": "Diners Club",
        "305": "Diners Club",
        "36": "Diners Club",
        "38": "Diners Club",
        "35": "JCB"
    }

    bank_names = {
        "4": "Visa",
        "51": "Mastercard",
        "52": "Mastercard",
        "53": "Mastercard",
        "54": "Mastercard",
        "55": "Mastercard",
        "37": "American Express",
        "97": "Troy",
        "65": "Troy",
        "6011": "Discover",
        "300": "Diners Club",
        "301": "Diners Club",
        "302": "Diners Club",
        "303": "Diners Club",
        "304": "Diners Club",
        "305": "Diners Club",
        "36": "Diners Club",
        "38": "Diners Club",
        "35": "JCB"
    }

    for prefix, card_type in card_types.items():
        if number.startswith(prefix):
            return card_type, bank_names[prefix]

    return "Unknown", "Bilinmeyen"

def main():
    print_header()
    credit_card_number = input(colored("Kredi kartı numarasını girin: ", "yellow")).strip()

    clear_screen()
    print(colored("""
     ██████╗ █████╗ ██████╗ ██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗
    ██║     ███████║██████╔╝██║  ██║
    ██║     ██╔══██║██╔══██╗██║  ██║
    ╚██████╗██║  ██║██║  ██║██████╔╝
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ """, "red"))
    print(colored("-----------------------------------------------------------------", "green"))

    if not credit_card_number:
        print(colored("Kredi kartı numarası girmelisiniz.", "red"))
        return

    if is_valid_credit_card(credit_card_number):
        time.sleep(0.5)
        print(colored("Kart Durumu --> ", "cyan"), colored("Geçerli", "red"))
        print(colored("-----------------------------------------------------------------", "green"))
        card_type, bank_name = get_card_info(credit_card_number)
        time.sleep(0.5)
        print(colored("Kart Tipi: ", "cyan"), colored(card_type, "red"))
        print(colored("-----------------------------------------------------------------", "green"))
        time.sleep(0.7)
        print(colored("Banka: ", "cyan"), colored(bank_name, "red"))
        print(colored("-----------------------------------------------------------------", "green"))
    else:
        print(colored("Kart Geçersiz.", "red"))

if __name__ == "__main__":
    main()
