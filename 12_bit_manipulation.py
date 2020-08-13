'''
Bit Manipulation:

  Decimal is Base 10:

    0 1 2 3 4 5 6 7 8 9 => 10 symbols, digits

    23 => 2 x 10 and 3 x 1
    
    147 => 1 x 100, 4 x 10, 7 x 1

    We call it Base_10

  
  Binary Code:

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

    0x8 is 8

    0x9 is 9

    0xA is 10

    We call it Base_16


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



'''