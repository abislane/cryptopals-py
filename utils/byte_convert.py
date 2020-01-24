
hex_digits = '0123456789abcdef'
b64_digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def hex_to_bytes(hexstr: str) -> bytes:
    result = []
    for i in range(0, len(hexstr), 2):
        d1 = hex_digits.index(hexstr[i])
        d2 = hex_digits.index(hexstr[i + 1])
        result.append(16 * d1 + d2)
    return bytes(result)

def bytes_to_hex(bytestr: bytes) -> str:
    result = ''
    for b in bytestr:
        result += hex_digits[b // 16] + hex_digits[b % 16]
    return result

def b64_to_bytes(b64str: str) -> bytes:
    result = []
    for i in range(0, len(b64str), 4):
        number = 0
        digits = 0
        for j in range(4):
            number *= 64
            if b64str[i + j] != '=':
                digits += 1
                number += b64_digits.index(b64str[i + j])
        for _ in range(4 - digits):
            number //= 256
        new_bytes = []
        for _ in range(digits - 1):
            new_bytes.insert(0, number % 256)
            number //= 256
        result += new_bytes
    return bytes(result)

def bytes_to_b64(bytestr: bytes) -> str:
    result = ''
    for i in range(0, len(bytestr), 3):
        number = 0
        digits = 0
        for j in range(3):
            number *= 256
            if i + j < len(bytestr):
                digits += 1
                number += bytestr[i + j]
        new_digits = ''
        for _ in range(3 - digits):
            number //= 64
            new_digits += '='
        for _ in range(digits + 1):
            new_digits = b64_digits[number % 64] + new_digits
            number //= 64
        result += new_digits
    return result
