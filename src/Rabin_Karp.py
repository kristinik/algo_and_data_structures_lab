def rabin_karp(haystack, needle, base=3, divisor=101):
    if not haystack or not needle:
        return []

    haystack_len = len(haystack)
    needle_len = len(needle)
    result = []


    pattern_mask = 0
    for i in range(needle_len):
        pattern_mask = (base * pattern_mask + ord(needle[i])) % divisor

    haystack_mask = 0
    for i in range(needle_len):
        haystack_mask = (base * haystack_mask + ord(haystack[i])) % divisor

    for i in range(haystack_len - needle_len + 1):
        if haystack_mask == pattern_mask and haystack[i:i + needle_len] == needle:
            result.append(i)

        if i < haystack_len - needle_len:
            haystack_mask = (base * (haystack_mask - ord(haystack[i]) * (base ** (needle_len - 1))) + ord(
                haystack[i + needle_len])) % divisor

    return result
