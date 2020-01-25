from . import character_frequency as cf

def xor_decode(encoded: bytes, key: bytes) -> bytes:
    """decodes an encoded string by xor. if key is shorter than encoded,
    it wraps. 
    """
    result = []
    for i in range(len(encoded)):
        result.append(encoded[i] ^ key[i % len(key)])
    return bytes(result)

def crack_single_byte_xor(encoded: bytes) -> (bytes, int, float):
    """Given an encoded English message encoded with a one char key, decodes it

    Return type is (the decoded message, the key, the score)
    """
    lowest_score = 2 ** 30
    result = ''
    result_key = -1
    for x in range(256):
        key = bytes([x])
        decoded = xor_decode(encoded, key)
        if cf.chars_valid(decoded):
            score = cf.score_english(decoded)
            if score < lowest_score:
                lowest_score = score
                result = decoded
                result_key = x
    return result, result_key, lowest_score