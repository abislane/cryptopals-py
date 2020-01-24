from utils import byte_convert as bc
from utils import xor

in1 = '1c0111001f010100061a024b53535009181c'
in2 = '686974207468652062756c6c277320657965'
expected_out = '746865206b696420646f6e277420706c6179'

bytes1 = bc.hex_to_bytes(in1)
bytes2 = bc.hex_to_bytes(in2)

out_bytes = xor.xor_decode(bytes1, bytes2)
print(out_bytes)
out = bc.bytes_to_hex(out_bytes)
assert expected_out == out
print("Challenge 2 complete!")
