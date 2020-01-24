def xor_decode(encoded: bytes, key: bytes) -> bytes:
    """decodes an encoded string by xor. if key is shorter than encoded,
    it wraps. 
    """
    result = []
    for i in range(len(encoded)):
        result.append(encoded[i] ^ key[i % len(key)])
    return bytes(result)