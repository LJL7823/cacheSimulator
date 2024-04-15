#from cache_classes import *
import time
import sys

def main():
    print("Cache Simulator by Ruhan, Maya, Key'Mon, and Liam \n\n")
    # Prompts the user for each required input
    """size: int = input("Input the Nominal Size of the cache in Bytes:")
    words_per_block : int = input("Input the number of words per block (1, 2, 4, 8,...):")
    mapping_policy : str = input("Mapping type Direct (D) or Set-Associative (S):")
    if(mapping_policy == 'S' or mapping_policy == 's'):
        blocks_per_set = input("input the number of blocks per set:")
        # Should be replace with the creation of the cache
        print(size,words_per_block, mapping_policy, blocks_per_set)
    else:
        # Should be replaced with the create of the cache
        print(size,words_per_block, mapping_policy)
    """
    
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
    