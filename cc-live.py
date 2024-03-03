from colorama import Fore, Style

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

def get_card_type(number):
    if number.startswith("4"):
        return "Visa"
    elif number.startswith(("51", "52", "53", "54", "55")):
        return "Mastercard"
    elif number.startswith("34") or number.startswith("37"):
        return "American Express"
    elif number.startswith("6"):
        return "Discover"
    else:
        return "Bilinmeyen"

def main():

    credit_card_number = input("Kredi kartı numarasını girin: ")

    if is_valid_credit_card(credit_card_number):
        print("Kart geçerli.")

        card_type = get_card_type(credit_card_number)
        print("Kart tipi:", card_type)
    else:
        print("Kart geçersiz.")

if __name__ == "__main__":
    main()
