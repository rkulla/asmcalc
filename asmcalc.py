# asmcalc.py
# Assembly Calculator/Conversion cli-tool/library - by Ryan Kulla
#
# Created to help me code Assembler languages more easily.
# It can also be used as a general base converter tool.

import sys


def bin_to_dec(binary_string):
    """ Binary to Decimal converter function """
    # Generate the positions
    position = range(len(binary_string))
    position.reverse()  # For proper bit order
    # For each "1" in the binary string, add in 2**n where "n" is the
    # zero-based position of the binary digit # and store each value in a list:
    add_these = []
    for i, bit in enumerate(binary_string):
        if int(bit) == 1:
            add_these.append(
                int(bit) * 2 ** position[i])  # Convert bits to dec
    # Add each decimal value to itself to generate the sum:
    sum = 0
    for decimal in add_these:
        sum += decimal
    return sum


def dec_to_bin(decimal):
    """ Decimal to Binary converter function """
    bits = []
    while decimal:
        # Double digits AND'd to 1 will append '0' (25&1=0). 9&1=1 though:
        bits.append('01'[decimal & 1])
        # Divide the decimal by 2 until it reaches 0 and the loop stops:
        decimal >>= 1
    bits.reverse()  # it was appended backwards
    binary_string = ''.join(bits) or '0'
    return binary_string


def hex_chart(chart_len):
    """
    Decimal to Hex chart function.

    >>> import asmcalc
    >>> asmcalc.hex_chart(17)
    Decimal) Hex
    0) 0
    1) 1
    2) 2
    3) 3
    4) 4
    5) 5
    6) 6
    7) 7
    8) 8
    9) 9
    10) A
    11) B
    12) C
    13) D
    14) E
    15) F
    16) 10
    """
    print "Decimal) Hex"
    for i in range(chart_len):
        print "%s) %s" % (i, hex(i).split('0x')[1].upper())


def hex_to_dec(h):
    """ Hex to Decimal converter function """
    h = "0x" + h
    return int(eval(h))


def dec_to_hex(d):
    """ Decimal to Hex converter function """
    h = hex(d)
    return h.split('0x')[1].upper()


def add_hex():
    """ Hexadecimal addition function """
    h1 = raw_input("Enter first hex number: ")
    h2 = raw_input("Enter second hex number: ")
    hex2dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
               'F': 15}
    i = 1
    y = '0'
    l = []
    carry_pos = []
    while i <= len(h1):
        if len(y) > 1:  # It's more than a single digit so carry the 1:
            x = hex2dec[h1[-i]] + hex2dec[h2[-i]] + 1  # Carry 1 from last num
            l.append(y[-1])
            carry_pos.append(-i)
            y = 0
        else:
            x = hex2dec[h1[-i]] + hex2dec[h2[-i]]
        y = hex(x).split('0x')[1].upper()
        if len(y) == 1:
            l.append(y)
        i = i + 1
    l.reverse()
    l = ''.join(l)
    carry_list = ' ' * len(h1)
    carry_list = list(carry_list)
    for c in carry_pos:
        carry_list[c] = '1'  # You can only carry the 1 in addition in any base
    c = ''.join(carry_list)
    print " %s\n %s\n+%s\n %s\n %s" % (c, h1, h2, ('-' * len(l)), l)


def hex_to_bin(h):
    """ Hex to Binary converter function """
    hex2dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
               'F': 15}
    h = h.upper()
    l = []
    for hexdigit in h:
        h = hex2dec[hexdigit]
        l.append(dec_to_bin(h).zfill(4))
    return ' '.join(l)


def bin_to_hex(b):
    """ Binary to Hex converter function """
    dec2hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
               15: 'F'}
    # Split the binary into groups of 4 digits for faster processing:
    l = []
    i = 0
    while i <= len(b) - 1:
        if i != 0 and i % 4 == 0:
            l.append('x')  # Mark with an 'x' every 4 bits
        l.append(b[i])
        i = i + 1
    l = ''.join(l).split('x')  # Remove x's and have a list of groups of 4 bits

    l2 = []
    for i in l:
        l2.append(dec2hex[bin_to_dec(i)])
    return ''.join(l2)


def display_help():
    print "Command-line options (b=binary, h=hex, d=decimal:\n"\
          "\t-h, -addhex, -b2d, -b2h, -d2b, -d2h, -h2b, -h2d, -hchart\n\n"\
          "Module methods:\n"\
          "\tbin_to_dec(), bin_to_hex(), dec_to_bin(),\n"\
          "\tdec_to_hex(), hex_to_bin(), hex_to_dec(), hex_chart(n)\n"


def error_check(args):
    if len(args) < 3:
        print "You have to enter a value"
        raise SystemExit
    else:
        return args[2]

if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        sys.stderr.write("%s requires at least one argument\n" % args[0])
        sys.stderr.write("Try: -h, --help\n\n")
        sys.exit()
    if args[1] in ("-h", "--help"):
        display_help()
    if "-b2d" in args:
        print bin_to_dec(error_check(args))
    if "-d2b" in args:
        print dec_to_bin(int(error_check(args)))
    if "-h2d" in args:
        print hex_to_dec(error_check(args))
    if "-d2h" in args:
        print dec_to_hex(int(error_check(args)))
    if "-h2b" in args:
        print hex_to_bin(error_check(args))
    if "-b2h" in args:
        print bin_to_hex(error_check(args))
    if "-hchart" in args:
        hex_chart(int(error_check(args)))
    if "-addhex" in args:
        add_hex()
