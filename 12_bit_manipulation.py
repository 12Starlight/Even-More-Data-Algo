'''
Bit Manipulation:

  Decimal is Base 10:

    0 1 2 3 4 5 6 7 8 9 => 10 symbols, digits

    23 => 2 x 10 and 3 x 1
    
    147 => 1 x 100, 4 x 10, 7 x 1

    We call it Base_10

  
  Binary Code: https://www.youtube.com/watch?v=jvx-NrILgpE

    The computer iteself does not 'think' in Decimal.









    Each place represents a base 2 to a power

      101
    -------
    (1) -> 2^2 ~ (0) -> 2^1 ~ (1) -> 2^0

        4   +   0   +   1   =   5

    We call it Base_2

    
    A Byte = 8 bits 

      [1][1][1][1][1][1][1][1]
     1 0  0  0  0  0  0  0  0

    2^8 = 256 - 1 = 255

    (0 - 255)

    (255, 255, 255) => Maxed out bits in each category, giving white


  Hexidicimal is Base 16:

    0 1 2 3 4 5 6 7 8 9 a b c d e f => 16 symbols

    8 bits in a byte, max 255

      0x8 is 8

      0x9 is 9

      0xa is 10

    We call it Base_16

      0x63 is 99

      0xff is 100

      0xfe is 254
      
      Oxff is 255

    Decimal is using 3 digits, hex only 2! So, 2 digits, Oxff, is a full Byte

      16 bits, 2 Bytes, max 65535

      0xfffe is 65534

      0xffff is 65535

    So 4 digits, 0xffff, is 2 Bytes (16 bits)


                    Ox af

          a                     f

    1    0    1    0      1    1    1    1  

    2^3  2^2  2^1  2^0    

    8 +  4 +  2 +  1 = 15

    (0 - 15)   


    FF    FF    00 => Yellow
    --------------
    R     G     B
    (255, 255,  0)


    3 Bytes, 1 Byte per color channel
    
    # ff ff 00


Decimal To Hex:

  Divide decimal by 16 and write own remainder in hex:

  121 / 16 = 7 remainder 9:         9

  7 can not be divided by 16:       7

    So... 121 is 0x79

  
  3002 / 16 = 187 remainder 10:     a

  187 / 16 = 11 remainder 11:       b

  11 can not be divided by 16:      b

    So... 3002 is 0xbba


Hex To Decimal:

  0x79 is

    = (7 * 16) + 9

    = 112 + 9 = 121

  NB (Latin for 'note well'): Technically it is (7 * 16^1) + (9 * 16^0)


  0xbba is



    = (11 * 16^2) + (11 * 16^1) + 10

    = (11 * 256) + (11 * 16) + 10

    = 2816 + 176 + 10

    = 3002

''' 