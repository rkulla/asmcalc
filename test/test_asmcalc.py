import asmcalc
import unittest
import doctest


class AsmCalcTests(unittest.TestCase):
    def testBinToDec(self):
        self.assertEqual(asmcalc.bin_to_dec('10'), 2)

    def testDecToBin(self):
        self.assertEqual(asmcalc.dec_to_bin(2), '10')

    def testBinToHex(self):
        self.assertEqual(asmcalc.bin_to_hex('1010'), 'A')

    def testHexToBin(self):
        self.assertEqual(asmcalc.hex_to_bin('A'), '1010')

    def testDecToHex(self):
        self.assertEqual(asmcalc.dec_to_hex(10), 'A')

    def testHexToDec(self):
        self.assertEqual(asmcalc.hex_to_dec('A'), 10)

    def test_doctests(self):
        doctest.testmod(asmcalc)

if __name__ == '__main__':
    unittest.main()
