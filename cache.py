'''
    This file uses the byte address inputs to find the word addresses and spot in cache
    based on the number of ways. It also populates the cache memory with the data and it's place in memory.
'''

# cache memory to store the data and it's place in memory
cache = [[]]
hit = 0
miss = 0

def initCache(num_blocks, N):
    ''' 
        initialize the cache memory with the number of blocks and ways
        cache = 2D array rows = num_blocks // N, columns = N
        @vars
        num_blocks = the number of blocks in cache
        N = the number of ways

        @return
        cache = 2D array rows = num_blocks // N, columns = N
    '''
    global cache
    cache = [[None for i in range(N)] for j in range(num_blocks // N)]
    return cache

def populateCache(data, spot):
    ''' 
        populate the cache memory with the data and it's place in memory
        cache = dict() with key = int, value = data
        @vars
        data = dict() with key = block_address value = word_addresses[]
        spot = spot in memory to place the data

        if the spot is full, replaces the least recently used data in cache
        with the new data

        @return
        cache = dict() with key = int, value = data
    '''
    global cache
    global hit, miss

    # if the data is already in the cache, don't add it again
    # otherwise, add the data to the cache
    for i in range(len(cache[spot])):
        if cache[spot][i] == data:
            hit += 1
            return cache
        elif cache[spot][i] == None:
            cache[spot][i] = data
            miss += 1
            return cache
    
    temp = cache[spot].pop(0)
    cache[spot][0] = data
    cache[spot].append(temp)
    miss += 1
    return cache


def findWordAddresses(word_address, words_per_block, N):
    ''' 
        find the word addresses in cache based on the number of ways
        @vars
        block_address = the block address
        word_address = the word address
        words_per_block = the number of words per block
        N = the number of ways

        @return
        data = dict() with key = block_address value = word_addresses[]
    '''
    data = dict()

    # find the block address
    block_address = word_address // words_per_block

    # get the word addresses in cache based on the number of ways
    word_addresses = []
    
    match N:
        case 1:
            word_addresses = [word_address]
        case 2:
            if word_address % 2 == 0:
                word_addresses = [word_address, word_address + 1]
            else:
                word_addresses = [word_address - 1, word_address]
        case 4:
            if word_address % 2 == 0:
                word_addresses = [word_address, word_address + 1, word_address + 2, word_address + 3]
            else:
                word_addresses = [word_address - 1, word_address, word_address + 1, word_address + 2]
        case 8:
            if word_address % 2 == 0:
                word_addresses = [word_address, word_address + 1, word_address + 2, word_address + 3, word_address + 4, word_address + 5, word_address + 6, word_address + 7]
            else:
                word_addresses = [word_address - 1, word_address, word_address + 1, word_address + 2, word_address + 3, word_address + 4, word_address + 5, word_address + 6]
        case 16:
            if word_address % 2 == 0:
                word_addresses = [word_address, word_address + 1, word_address + 2, word_address + 3, word_address + 4, word_address + 5, word_address + 6, word_address + 7, word_address + 8, word_address + 9, word_address + 10, word_address + 11, word_address + 12, word_address + 13, word_address + 14, word_address + 15]
            else:
                word_addresses = [word_address - 1, word_address, word_address + 1, word_address + 2, word_address + 3, word_address + 4, word_address + 5, word_address + 6, word_address + 7, word_address + 8, word_address + 9, word_address + 10, word_address + 11, word_address + 12, word_address + 13, word_address + 14]
        case _:
            print("Number of ways not supported")

    if data.get(block_address) is None:
        data = {block_address: word_addresses}

    return data, block_address


def findIndex(block_address, num_blocks, N):
    ''' 
        find the spot in cache based on the number of ways
        @vars
        block_address = the block address
        num_blocks = the number of blocks in cache
        N = the number of ways

        @return
        spot = the spot in cache to place the data
    '''

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
