from utils import byte_convert as bc
from utils import xor
from utils import character_frequency as cf

in_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
in_bytes = bc.hex_to_bytes(in_str)

result, _, _ = xor.crack_single_byte_xor(in_bytes)
print(result)