# Import necessary modules and classes
from gettext import find
import time
import sys
import math as m
import cache
from cache import initCache
from params import parameterClass
import random

def main():
    """Main Method of the program does the I/O"""
    print("Cache Simulator by Ruhan, Maya, Key'Mon, and Liam \n\n")
    
    # Prompt the user for each required input
    nom_size: int = int(input("Input the Nominal Size of the cache in Bytes:")) # type: ignore
    words_per_block : int = int(input("Input the number of words per block (1, 2, 4, 8,...):")) # type: ignore
    mapping_policy : str = input("Mapping type Direct (D) or Set-Associative (S):")
    
    # If the mapping policy is Set-Associative
    if(mapping_policy == 'S' or mapping_policy == 's'):
        theN : int = int(input("Input the number of blocks per set:")) # type: ignore
        bytesPerBlock : int = 4 * words_per_block # Calculate the number of bytes per block
        num_block : int = (nom_size//bytesPerBlock)   # Calculate the number of blocks 
        num_set : int = (num_block//theN) # Calculate the number of sets
        index_bits :int = int(m.log2(num_set)) # Calculate the index bits
        offset_bits :int  = int(m.log2(bytesPerBlock))  # Calculate the offset bits 
        tag : int = 32 - (index_bits + offset_bits)   # Calculate the tag bits
        stat : int = 1 + int(m.log2(theN)) # Calculate the stat
        realSize : int = (nom_size + num_block*((tag + stat)//8))//(2^10)  # Calculate the real size in kilobytes
        
        # Create an instance of parameterClass with the calculated parameters
        our_Cache = parameterClass( nom_size, words_per_block, \
                                   mapping_policy, theN, bytesPerBlock, num_block,\
                                        num_set, index_bits, offset_bits, tag,\
                                           stat, realSize)
        print(nom_size,words_per_block, mapping_policy, num_set)
    else:
        # If the mapping policy is Direct
        bytesPerBlock : int = 4 * words_per_block # Calculate the number of bytes per block
        num_block : int = int(nom_size//bytesPerBlock)   # Calculate the number of blocks 
        index_bits : int = int(m.log2(num_block))   # Calculate the index bits 
        offset_bits :int  = int(m.log2(bytesPerBlock))  # Calculate the offset bits 
        tag : int = 32 - (index_bits + offset_bits)   # Calculate the tag bits
        realSize : int = (nom_size + num_block*((tag + 1)//8))  # Calculate the real size in kilobytes
        
        # Create an instance of parameterClass with the calculated parameters
        our_Cache = parameterClass( nom_size, words_per_block, mapping_policy, \
                                    1, bytesPerBlock, num_block,\
                                   num_block, index_bits, offset_bits, \
                                   tag, 1, realSize)        
        print(nom_size,words_per_block, mapping_policy, bytesPerBlock, num_block, index_bits, offset_bits, tag, realSize)

    print(our_Cache)
    
    # Ask the user to choose between Prompt mode and Simulate mode
    if(1==int(input("Input '1' for Prompt mode, '2' to do simulate mode: "))):
        promptMode(our_Cache)
    else:
        simMode(our_Cache)

# Function for Prompt mode
def promptMode(clss : parameterClass ):
    initCache(clss.num_block, clss.theN)
    while (True):
        temp = int(input("Input a word: "))
        try:
            currentData, block_address = cache.findWordAddresses(temp, clss.words_per_block, clss.theN)
            # print(cache.cache)
            index = cache.findIndex(block_address, clss.num_set, clss.theN)
            cache.populateCache(currentData, index, clss.num_set, clss.mapping_policy)
            ## call program
            print(cache.cache)
        except ValueError:
            sys.stdout.write("Exiting Program...")
            print("\nThank You :)")
            exit(99)
    
# Function for Simulate mode
def simMode(clss : parameterClass):
    x = int(input("Input max number of simulations tested: "))
    y = int(input("Input the highest word address you would like tested: "))
    initCache(clss.num_block, clss.theN)
    for i in range(x):
        try:
            temp = random.randint(0,y)
            currentData, block_address = cache.findWordAddresses(temp, clss.words_per_block, clss.theN)
            print(cache.cache)
            index = cache.findIndex(block_address, clss.num_block, clss.theN)
            cache.populateCache(currentData, index, clss.num_set, clss.mapping_policy)
            print(cache.cache)
        except ValueError:
            sys.stdout.write("Exiting Program...")
            print("\nThank You :)")
            exit(99)

# Call the main function
if __name__ == '__main__':
    main()
