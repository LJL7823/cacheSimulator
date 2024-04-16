from dataclasses import dataclass


@dataclass
class parameterClass:
    nom_size : int
    words_per_block : int
    mapping_policy : int
    theN : int
    bytesPerBlock : int
    num_block : int
    num_set : int
    index_bits : int
    offset_bits : int
    tag : int
    stat : int
    realSize : int
    address_size : int = 32 
    word_size : int = 32
    

    def __init__(self, nom_size, words_per_block, mapping_policy, theN, \
        bytesPerBlock, num_block, num_set, index_bits, offset_bits, tag, \
        stat, realSize, address_size=32, word_size=32):
        self.nom_size = nom_size
        self.words_per_block = words_per_block
        self.mapping_policy = mapping_policy
        self.theN = theN
        self.bytesPerBlock = bytesPerBlock
        self.num_block = num_block
        self.num_set = num_set
        self.index_bits = index_bits
        self.offset_bits = offset_bits
        self.tag = tag
        self.stat = stat
        self.realSize = realSize
        self.address_size = address_size
        self.word_size = word_size