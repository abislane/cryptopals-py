from utils import byte_convert as bc

hex_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64_input = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print(bc.b64_to_bytes(b64_input))
assert bc.bytes_to_hex(bc.b64_to_bytes(b64_input)) == hex_input
print(bc.hex_to_bytes(hex_input))
assert bc.bytes_to_b64(bc.hex_to_bytes(hex_input)) == b64_input
print("Challenge 1 complete!")