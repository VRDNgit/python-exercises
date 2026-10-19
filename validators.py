def validate_phone_number(number):
    number = number.strip()

    if not number.isdigit():
        raise ValueError("Phone number must contain digits only.")

    if len(number) != 11 or not number.startswith("09"):
        raise ValueError("Phone number must be 11 digits and start with 09.")

    return number


def validate_national_id(code):
    code = code.strip()

    if not code.isdigit():
        raise ValueError("National ID must contain digits only.")

    if len(code) != 10:
        raise ValueError("National ID must be exactly 10 digits long.")

    return code


def validate_bank_card(card):
    card = card.strip()

    if not card.isdigit():
        raise ValueError("Card number must contain digits only.")

    if len(card) != 16:
        raise ValueError("Card number must be exactly 16 digits long.")

    return card


def validate_license_plate(plate):
    plate = plate.strip()

    if len(plate) < 7:
        raise ValueError("License plate must contain at least 7 characters.")
    return plate


def validate_bill_identifier(identifier):
    identifier = identifier.strip()

    if not identifier.isdigit():
        raise ValueError("Bill identifier must contain digits only.")

    if not 8 <= len(identifier) <= 13:
        raise ValueError("Bill identifier must be between 8 and 13 digits.")

    return identifier

