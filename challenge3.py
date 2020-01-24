from utils import byte_convert as bc
from utils import xor
from utils import character_frequency as cf

in_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
in_bytes = bc.hex_to_bytes(in_str)

lowest_score = 2 ** 30
result = b''
for x in range(256):
    key = bytes([x])
    decoded = xor.xor_decode(in_bytes, key)
    if cf.chars_valid(decoded):
        score = cf.score_english(decoded)
        if score < lowest_score:
            lowest_score = score
            result = decoded
print(result)