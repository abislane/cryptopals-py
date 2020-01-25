from utils import byte_convert as bc
from utils import xor
from utils import character_frequency as cf

import sys

in_strs = []
for line in sys.stdin:
    in_strs.append(line.strip())

lowest_score = 2 ** 30
lowest_score_line = -1
result = b''

for i in range(len(in_strs)):
    in_bytes = bc.hex_to_bytes(in_strs[i])
    for x in range(256):
        key = bytes([x])
        decoded = xor.xor_decode(in_bytes, key)
        if cf.chars_valid(decoded):
            score = cf.score_english(decoded)
            if score < lowest_score:
                lowest_score = score
                lowest_score_line = i
                result = decoded
print("line {} is xor encoded, decodes to:\n{}".format(lowest_score_line, result))