'''
Bit Manipulation:

  Decimal is Base 10:

    0 1 2 3 4 5 6 7 8 9 => 10 symbols, digits

    23 => 2 x 10 and 3 x 1
    
    147 => 1 x 100, 4 x 10, 7 x 1

    We call it Base_10

  
  Binary Code: https://www.youtube.com/watch?v=jvx-NrILgpE

    The computer iteself does not 'think' in Decimal. It stores values as
    electrical charges that can be measured as either Low or High, Off or On,
    zero or one. 

      [1][0][1][0]


    This system is known as 'Binary', and in binary, each digit is known as a
    bit.

      [1][0][1]  [0] <- bit


    Each place represents a base 2 to a power. We call it Base_2

      101
    -------
    (1) -> 2^2 ~ (0) -> 2^1 ~ (1) -> 2^0

        4   +   0   +   1   =   5

    
    A Byte = 8 bits 

      [1][1][1][1][1][1][1][1]
     1 0  0  0  0  0  0  0  0

    2^8 = 256 - 1 = 255

    (0 - 255)

    (255, 255, 255) => Maxed out bits in each category, giving white


    A bit can hold a maximum value of 1, in order to represent more than 1 we
    we need to add another bit. So a 2 binary looks like this ...

         [1] = 1

      [1][0] = 2


    And a three will look like this ...

      [1][1] = 3


    As we keep counting up to ten, you will notice that binary uses up a lot 
    more space compared to good old decimal notation.

      [1][0][0] = 4

      [1][0][1] = 5

      [1][1][0] = 6

      [1][0][0][0] = 8

      [1][0][1][0] = 10


    And that is just a 4-bit value, most computers nowdays work with binary 
    values of 32-bit length ...

      32-bit value
      [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


    Some even use 64-bit values ...

      64-bit value
      [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]      
      [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]      


    At this point, even if we displayed these values in decimal notation, they
    are just rediculously long and unwieldy. So when writing code, it is helpful
    to have a more convenient way to represent them. A that is where
    'Hexadecimal' notation comes in handy.

      0xFF301B


  Hexidicimal is Base 16:

    Hexadecimal, or simply 'hex' as it is known to friends, uses 16 characters
    to represent a number value. Like decimal, it uses the classics. But it also
    uses letters, to represent values 10 through 15 it uses letters like so ...
                        
      0 = zero
      1 = one
      2 = two
      3 = three
      4 = four
      5 = five
      6 = six
      7 = seven
      8 = eight
      9 = nine
      A = ten
      B = eleven
      C = twelve
      D = thirteen
      E = fourteen
      F = fifteen


    Bc of those extra characters, hexadecimal notation takes up less space in
    text. Making it easier for us humans to type out or even simply remember a
    specific value.

      Binary = 11111100

      Decimal = 256

      Hex = FC


      Binary = 11101111 11001111 11111010

      Decimal = 15716346

      Hex = EFCFFA


    Oh but wait - that is not all! Hex also syncs up nicely with the way we 
    group Binary bits. In Binary - a group of four bits is called a 'nybble'.

      [1][1][0][0] <- nybble


    And a nybble can conveniently be represented by a single character in
    hexadecimal. 

      Binary  
      [1][1][0][0]      

      Hex
      [C]


    A group of 8 bits in Binary is called a 'byte', and can be represented using
    only 2 hex characters.

      Binary
      [1][1][0][0][1][1][1][0] <- byte

      Hex
      [C][E]


    In order to clearly specify when we are using hexadecimal in code, we add a
    '0x' at the beginning of the value. This makes sure we do not mistake it for
    decimal notation. 

    But in the end - no matter what system we use to represent a value in code.
    It will always be converted to binary and use the same amount of space 
    within digital memory. So regardless of what we see on the screen, 
    underneath it all - it is bits all the way down. 


    8 bits in a byte, max 255

      0x8 is 8
      0x9 is 9
      0xa is 10
      0x63 is 99
      0xFF is 100
      0xFE is 254
      OxFF is 255


    Decimal is using 3 digits, hex only 2! So, 2 digits, OxFF, is a full Byte

      16 bits, 2 bytes, max 65535
      0xFFFE is 65534
      0xFFFF is 65535


    So 4 digits, 0xFFFF, is 2 bytes (16 bits)


                    Ox AF

          A                     F

    1    0    1    0      1    1    1    1  

    2^3  2^2  2^1  2^0    

    8 +  4 +  2 +  1 = 15

    (0 - 15)   


    FF    FF    00 => Yellow
    --------------
    R     G     B
    (255, 255,  0)


    3 Bytes, 1 Byte per color channel
    
    # FF FF 00



Decimal To Hex:

  Divide decimal by 16 and write own remainder in hex:

  121 / 16 = 7 remainder 9:         9

  7 can not be divided by 16:       7

    So... 121 is 0x79

  
  3002 / 16 = 187 remainder 10:     A

  187 / 16 = 11 remainder 11:       B

  11 can not be divided by 16:      B

    So... 3002 is 0xBBA


Hex To Decimal:

  0x79 is

    = (7 * 16) + 9
    = 112 + 9 = 121

  NB (Latin for 'note well'): Technically it is (7 * 16^1) + (9 * 16^0)


  0xBBA is

    = (11 * 16^2) + (11 * 16^1) + 10
    = (11 * 256) + (11 * 16) + 10
    = 2816 + 176 + 10

    = 3002

''' 

'''
Operations:

  The result equals one or not one:

    AND = Both values are 1 = 1

    OR = Either values are 1 = 1

    LSHIFT = Shifts to the left (add space to right)

    RSHIFT = Shifts to the right (delete space to right)

    XOR = Both values different = 1


  AND           OR           LSHIFT          RSHIFT          XOR

  &             |            <<              >>              ^

  101           101      5 = 101 << 1    5 = 101 >> 1        101
  011           011          =               =               011
  ---           ---     10 = 1010        2 = 10              ---
  001           111                                          110

  1&1 = 1   1|1 = 1          multiply        divide         -> 1^1 = 0
  0&1 = 0   0|1 = 1          by 2            by 2            0^0 = 0
                                                             1^0 = 1
  checks    turns on                                        -> 0^1 = 1   

                                                            toggle


  Okay, so if we were to try to see this in action, let us pretend we have the
  bits one, one, zero, one, and we want to switch off this second bit.

    [1][1][0][1]
        ^

  We want to conver this number into one, zero, zero, one. How do we do that?

    [1][0][0][1]


  Well, what you could do is you could take the number, we will represent it by
  N and we will say, let us toggle this second bit. So, we need to toggle it 
  with essentially the representation of zero, one, zero, zero. How do we get 
  that?

    n ^ (0100)


  Well, you can say, let us take the number one and shift it over by two. 

    1 << 2


  So this is actually going to look like n XOR one shifted by two, right? This 
  is what it is going to look like. 

    n ^ (1 << 2)


  And so this is essentially the formula for just toggling that second bit.
  Okay. so let us try writing this in code. 

'''


# Three Lights
l1 = 0b001
l2 = 0b010
l3 = 0b100

print(l1) # 1
print(l2) # 2
print(l3) # 4

# What does it look like to toggle all the lights on?
print('')
print(l1 | l2 | l3) 
  # -> gets you the value 7


# Let us say that the current state of the light is going to be light one or 
# light two. So, I have turned both of these on, and now I want to check is 
# light three on?
state = l1 | l2 
print('')
print(state)


# Well what you can do is AND that state with one zero, to see if that value is
# on. 
print('')
print(state & 0b1)
  # -> No, it was off. And so the AND operator is often used to check whether a
  # bit is on or off.


# Now the OR operator can be used to toggle a state. So I can say state OR 
# equals l3 and then if I print that I get the value 7, which represents 111. 
# Now the lights are on.
state |= l3 
print('')
print(state)


# And then the XOR operator kind of acts like a toggle. So I can say, let me
# turn off the second light. So I will say XOR equals 010. So that should only
# turn off the second light. If I have to print the state, then you see I am 
# getting five, which is 101.
state ^= 0b010
print('')
print(state)


'''
More Advanced

'''

# Let us say we want to take a number and convert it into the bit representation
# and see what that looks like. So, we want say print(num2bits(5)) and we want
# this to show the value of one, zero, one. What does this code look like? 
def num2bits(num): 
  result = ''
  # going through number
  while num: 
    # the result is equal to the string value of the number and one. So we are
    # taking that far right bit value and we are checking if it is one or not, 
    # and then we are just going to add it to that result
    result = str(num & 1) + result
    # then we are going to shift the number over by one and we just keep doing
    # that until we have shifted away all of the bits. 
    num = num >> 1
    # get the value 101, so that is correct 
  return result 

print('')
print(num2bits(5)) # 101

# In Python they have the built in method called 'bin'
print('')
print(bin(5)) # 0b101 


# We can also do this in reverse by taking a string and converting it to bits.
# And we want this to print the value five. So, let us see what that is going to
# look like?
def bits2num(bits):
  num = 0
  # for each bit in bits
  for bit in bits:
    # take the current number and shift it over by one. So we are making room 
    # for this new bit
    num = num << 1
    # if the bit value is equal to one, then we will just say that the number 
    # plus equals one and we will just keep going through all of the bits unitl
    # we get to the end
    if bit == '1':
      num += 1 
  return num

print('')
print(bits2num('101')) # 5

# In Python does have a handy dandy built in method that is known as 0b
print(0b101) # 5


# Another exercise we can do is count the total number of one bits in a series
def countbits(num):
  # the number of bits is equal to zero
  num_bits = 0
  # while the number is not zero
  while num:
    # we are just going to start shifting it. So, we will say num_bits plus 
    # equals to check whether the number has a value of one or zero on the far 
    # right side, THEN we add that value to num_bits
    num_bits += num & 1
    # then the num >>= acts like i -= 1 for the while loop and slices off the 
    # last bit till there are no more 
    num >>= 1
  # return the total number of bits that we were able to count so far to run 
  # this which you see that I am getting the value two, which is correct. 
  return num_bits

pirnt('')
print(countbits(5)) # 2


# And there is one more common interview exercise which I thought I should show 
# you. So here is how it works. Let us say you have an array like say, four, 
# one, four, two, two. And so the idea is that our numbers appear twice in this 
# array except for one number. And that one number only appears once, find that 
# number.
#
#   [4, 1, 4, 2, 2] 
#
# Well if you think about it, what you can do here is you can actually just go 
# through this whole array and use the XOR operator to XOR the numbers together
# bc a number XOR'd by iteself is going to equal 0. And the reason is that as we
# mentioned, the result of a XOR operation is only one when both bits are 
# different
# 
# But, when you XOR a number with itself, all of the bits are going to be the 
# same. And so all of the bits would be zero. We can go through the array and 
# just XOR everything together. 
#
# And then the last value that is there is going to be the single number XOR'd 
# by zero, which is essentially still just that same number, bc all of the bits 
# remained on toggle that they do not switch. 


# 