#from cache_classes import *
import time
import sys
import math as m

def main():
    print("Cache Simulator by Ruhan, Maya, Key'Mon, and Liam \n\n")
    # Prompts the user for each required input
    size: int = input("Input the Nominal Size of the cache in Bytes:")
    words_per_block : int = input("Input the number of words per block (1, 2, 4, 8,...):")
    mapping_policy : str = input("Mapping type Direct (D) or Set-Associative (S):")
    if(mapping_policy == 'S' or mapping_policy == 's'):
        blocks_per_set = input("input the number of blocks per set:")
        # Should be replace with the creation of the cache
        print(size,words_per_block, mapping_policy, blocks_per_set)
    else:
        # Should be replaced with the create of the cache
        bytesPerBlock = 4 * words_per_block # solves for the number of the bytes per block
        num_block = (size/bytesPerBlock)   # number of blocks 
        index_bits = m.log2(num_block)   # the index in bits 
        offset_bits = m.log2(bytesPerBlock)  # the offset in bits 
        tag = 32 - (index_bits + offset_bits)   # the tag in bits
        realSize = (size + num_block*((tag + 1)/8))/(2^10)  # solves for the real size in kilobytes
        print(size,words_per_block, mapping_policy, bytesPerBlock, num_block, index_bits, offset_bits, tag, realSize)


    
    
    # This is me f*ing around with the input loop
    while (True):
        temp = input("Input a word")
        try:
            int(temp)
        except ValueError:
            sys.stdout.write("Exiting Program")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.6)
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.7)
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
            print("\nThank You :)")
            exit(99)
    

if __name__ == '__main__':
    main()
    