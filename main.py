#from cache_classes import *
from gettext import find
import time
import sys
import math as m
from cache import *

def main():
    """Main Method of the program does the I/O
    """
    print("Cache Simulator by Ruhan, Maya, Key'Mon, and Liam \n\n")
    # Prompts the user for each required input
    nom_size: int = input("Input the Nominal Size of the cache in Bytes:") # type: ignore
    words_per_block : int = input("Input the number of words per block (1, 2, 4, 8,...):") # type: ignore
    mapping_policy : str = input("Mapping type Direct (D) or Set-Associative (S):")
    if(mapping_policy == 'S' or mapping_policy == 's'):
        theN : int = input("input the number of blocks per set:") # type: ignore
        bytesPerBlock : int = 4 * words_per_block # solves for the number of the bytes per block
        num_block : int = (nom_size//bytesPerBlock)   # number of blocks 
        num_set : int = (num_block//theN)
        index_bits :int = int(m.log2(num_set))
        offset_bits :int  = int(m.log2(bytesPerBlock))  # the offset in bits 
        tag : int = 32 - (index_bits + offset_bits)   # the tag in bits
        stat : int = 1 + int(m.log2(theN))
        realSize : int = (nom_size + num_block*((tag + stat)//8))//(2^10)  # solves for the real size in kilobytes
        # Should be replace with the creation of the cache
        print(nom_size,words_per_block, mapping_policy, num_set)
    else:
        # Should be replaced with the create of the cache
        bytesPerBlock : int = 4 * words_per_block # solves for the number of the bytes per block
        num_block : int = (nom_size//bytesPerBlock)   # number of blocks 
        index_bits : int = int(m.log2(num_block))   # the index in bits 
        offset_bits :int  = int(m.log2(bytesPerBlock))  # the offset in bits 
        tag : int = 32 - (index_bits + offset_bits)   # the tag in bits
        realSize : int = (nom_size + num_block*((tag + 1)//8))//(2^10)  # solves for the real size in kilobytes
        print(nom_size,words_per_block, mapping_policy, bytesPerBlock, num_block, index_bits, offset_bits, tag, realSize)


    if(1==int(input("Input '1' for Prompt mode, '2' to do simulate mode"))):
        promptMode()
    else:
        simMode()

    
    
    # This is me f*ing around with the input loop

def promptMode():
    while (True):
        temp = input("Input a word")
        try:
            int(temp)
            ## call program
        except ValueError:
            sys.stdout.write("Exiting Program...")
            print("\nThank You :)")
            exit(99)
    
def simMode():
    return 0

if __name__ == '__main__':
    main()
    