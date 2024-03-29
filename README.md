
asmcalc is a general base converter tool that I originally created to help me
code in Assembly languages more easily. It can be used as a CLI tool or a module.

Aside from base conversion it can also show useful outputs and charts.

### Usage

Command-line options (b=binary, h=hex, d=decimal):

    -h,--help, -addhex, -b2d, -b2h, -d2b, -d2h, -h2b, -h2d, -hchart

Module methods available:

    bin(), bin(), dec_to_bin(), dec_to_hex(), hex_to_bin(), hex_to_dec(),
    hex_chart(n)

when entering binary or hex, enclose in quotes:

    >>> asmcalc.bin_to_hex('1010')
    'A'

Adding two hex numbers example:

    $ python asmcalc.py -addhex
    Enter first hex number: 9
    Enter second hex number: 1

the resulting output will look like you wrote out the math on paper:

     9
    +1
     -
     A

Conversion example:

    $ python asmcalc.py -d2h 10

outputs 10 in hex: 

    A

or as a module:

    $ python
    >>> import asmcalc
    >>> asmcalc.dec_to_hex(10)
    A

Display a decimal to hex chart up to the number specified:

    $ python asmcalc.py -hchart 20

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
    17) 11
    18) 12
    19) 13

### Unit tests

Make sure the file runtests.base is in the root of the project.

cd to the root of the project and run as:

    $ chmod u+x runtests.bash
    $ ./runtests.bash
