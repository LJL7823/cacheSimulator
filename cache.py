# This file uses the byte address inputs to find the word addresses and spot in cache

# cache memory 
# data type is a dictionary with the key = int, value = list[N]
# key is the block address, value is a list of N elements
cache = [dict(int, [])]

''' populate the cache memory with the data and it's place in memory
    cache = dict() with key = int, value = data
    @vars
    data = dict() with key = block_address value = word_addresses
    spot = spot in memory to place the data

    @return
    cache = dict() with key = int, value = data
'''
def populateCache(data, spot):
    global cache
    cache[spot] = data
    return cache

''' find the word addresses in cache based on the number of ways
    @vars
    block_address = the block address
    word_address = the word address
    words_per_block = the number of words per block
    N = the number of ways

    @return
    word_addresses = the word addresses in cache based on the number of ways'''
def findWordAddresses(block_address, word_address, words_per_block, N):

    # find the block address
    block_address = word_address // words_per_block

    # get the word addresses in cache based on the number of ways
    word_addresses = []
    
    match N:
        case 1:
            word_addresses = [block_address]
        case 2:
            if block_address % 2 == 0:
                word_addresses = [block_address, block_address + 1]
            else:
                word_addresses = [block_address - 1, block_address]
        case 4:
            if block_address % 2 == 0:
                word_addresses = [block_address, block_address + 1, block_address + 2, block_address + 3]
            else:
                word_addresses = [block_address - 1, block_address, block_address + 1, block_address + 2]
        case 8:
            if block_address % 2 == 0:
                word_addresses = [block_address, block_address + 1, block_address + 2, block_address + 3, block_address + 4, block_address + 5, block_address + 6, block_address + 7]
            else:
                word_addresses = [block_address - 1, block_address, block_address + 1, block_address + 2, block_address + 3, block_address + 4, block_address + 5, block_address + 6]
        case 16:
            if block_address % 2 == 0:
                word_addresses = [block_address, block_address + 1, block_address + 2, block_address + 3, block_address + 4, block_address + 5, block_address + 6, block_address + 7, block_address + 8, block_address + 9, block_address + 10, block_address + 11, block_address + 12, block_address + 13, block_address + 14, block_address + 15]
            else:
                word_addresses = [block_address - 1, block_address, block_address + 1, block_address + 2, block_address + 3, block_address + 4, block_address + 5, block_address + 6, block_address + 7, block_address + 8, block_address + 9, block_address + 10, block_address + 11, block_address + 12, block_address + 13, block_address + 14]
        case _:
            print("Number of ways not supported")
    return word_addresses

''' find the spot in cache based on the number of ways
    @vars
    block_address = the block address
    num_blocks = the number of blocks in cache
    N = the number of ways

    @return
    spot = the spot in cache to place the data'''
def findSpotInCache(block_address, num_blocks, N):

    # get the spot in cache based on the number of ways
    spot = -1

    match N:
        case 1:
            spot = block_address % num_blocks
        case 2:
            spot = block_address % (num_blocks // 2)
        case 4:
            spot = block_address % (num_blocks // 4)
        case 8:
            spot = block_address % (num_blocks // 8)
        case 16:
            spot = block_address % (num_blocks // 16)
        case _:
            print("Number of ways not supported")
    return spot


