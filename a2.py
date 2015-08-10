def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    length = len(dna)
    return length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (dna contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence("ATCGGC")
    True
    >>> is_valid_sequence("aTCGGC")
    False
    >>> is_valid_sequence("TCGB")
    False
    """
    validity = True
    for i in dna:
        if i not in "ACTG":
            validity = False
    return validity


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    >>> insert_sequence('CCGG', 'AT',2)
    'CCATGG'
    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(dna):
    """ (str) -> str
    """
    if is_valid_sequence(dna) == True:
        if dna == "A":
            return "T"
        elif dna == "T":
            return "A"
        elif dna == "C":
            return "G"
        else:
            return "C"


def get_complementary_sequence(dna):
    """ (str) -> str
    >>> get_complementary_sequence("AT")
    "TA"
    """
    collect_reverse = ''
    if is_valid_sequence(dna) == True:
        for i in dna:
            collect_reverse = collect_reverse + get_complement(i)
        return collect_reverse



    



    
    
        











    
