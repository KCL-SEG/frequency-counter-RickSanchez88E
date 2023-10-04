"""
    Author: HONGYI TU
    Date: 4/Oct/2023
"""
def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item) if not isinstance(item, str) else item
        frequencies[key] = frequencies.get(key, 0)+1
    return frequencies
