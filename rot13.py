import sys

def rot(c, n):
    c = ord(c)
    if c >= ord('a') and c <= ord('z'):
        return chr((c - ord('a') + n) % 26 + ord('a'))
    elif c >= ord('A') and c <= ord('Z'):
        return chr((c - ord('A') + n) % 26 + ord('A'))
    else:
        return chr(c)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage %s [-rN] <word1> [word2 [word3 [...]]]")
    else:
        rot_by = 13
        if sys.argv[1].startswith('-r'):
            rot_by = int(sys.argv[1][2:])
            sys.argv[1:] = sys.argv[2:]
        print(''.join([rot(c, rot_by) for c in ' '.join(sys.argv[1:])]))
