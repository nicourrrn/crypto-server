table = {
    "А": "1",
    "И": "2",
    "Т": "3",
    "Е": "4",
    "С": "5",
    "Н": "6",
    "О": "7",
    "Б": "81",
    "В": "82",
    "Г": "83",
    "Ґ": "84",
    "Д": "85",
    "Є": "86",
    "Ж": "87",
    "З": "88",
    "І": "89",
    "Ї": "80",
    "Й": "91",
    "К": "92",
    "Л": "93",
    "М": "94",
    "П": "95",
    "Р": "96",
    "У": "97",
    "Ф": "98",
    "Х": "99",
    "Ц": "90",
    "Ч": "01",
    "Ш": "02",
    "Щ": "03",
    "Ь": "04",
    "Ю": "05",
    "Я": "06",
    " ": "07",
}


def to_num(text: str) -> str:
    encrypted_text = ""
    for letter in text.upper():
        encrypted_text += table[letter.upper()]
    return encrypted_text


def encrypt_nums(nums: str, key: str) -> str:
    encrypted_nums = ""
    for i, num in enumerate(nums):
        encrypted_nums += str((int(num) + int(key[i % len(key)])) % 10)
    return encrypted_nums


def decrypt_nums(nums: str, key: str) -> str:
    decrypted_nums = ""
    for i, num in enumerate(nums):
        decrypted_nums += str((10 + int(num) - int(key[i % len(key)])) % 10)
    return decrypted_nums


def from_num(nums: str) -> str:
    text = ""
    cursor = 0

    while cursor < len(nums):
        freq_letter = nums[cursor] in [str(i) for i in range(1, 8)]
        range_slice = (
            slice(cursor, cursor + 1) if freq_letter else slice(cursor, cursor + 2)
        )
        for key, value in table.items():
            if value == nums[range_slice]:
                text += key
                break
        cursor += 1 if freq_letter else 2

    return text


def encrypt(text: str, key: str) -> str:
    return encrypt_nums(to_num(text), to_num(key))


def decrypt(text: str, key: str) -> str:
    return from_num(decrypt_nums(text, to_num(key)))
