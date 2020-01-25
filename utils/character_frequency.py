eng_freq = {
   ord('a') : .08167,
   ord('b') : .01492,
   ord('c') : .02202,
   ord('d') : .04253,
   ord('e') : .12702,
   ord('f') : .02228,
   ord('g') : .02015,
   ord('h') : .06094,
   ord('i') : .06966,
   ord('j') : .00153,
   ord('k') : .01292,
   ord('l') : .04025,
   ord('m') : .02406,
   ord('n') : .06749,
   ord('o') : .07507,
   ord('p') : .01929,
   ord('q') : .00095,
   ord('r') : .05987,
   ord('s') : .06327,
   ord('t') : .09356,
   ord('u') : .02758,
   ord('v') : .00978,
   ord('w') : .02560,
   ord('x') : .00150,
   ord('y') : .01994,
   ord('z') : .00077 
}

def chars_valid(bytestr: bytes) -> bool:
    for x in bytestr:
        if x <= 8 or (x >= 14 and x <= 31) or x > 127:
            return False
    return True


def score_english(bytestr: bytes) -> float:
    freq = {}
    count = 0
    spaces = 0
    for i in range(26):
        freq[ord('a') + i] = 0
    for x in bytestr.lower():
        if x in freq:
            freq[x] += 1
            count += 1
        if x == ord(' '):
            spaces += 1
    if count == 0:
        # should not count this, so give an unnatual high score
        return 2 ** 30
    for x in freq:
        freq[x] /= count

    result = 0
    for x in freq:
        result += (freq[x] - eng_freq[x]) ** 2

    if spaces == 0:
        # probably want stuff with spaces, so weight accordingly
        result += 1
    return result