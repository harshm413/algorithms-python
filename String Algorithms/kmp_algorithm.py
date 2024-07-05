def get_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def find_all_matches_kmp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    if m == n:
        return [0] if pattern == text else []

    lps = get_lps(pattern)
    i, j = 0, 0
    matches = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

# Example usage
text = "abxabcabcabydhjbjabcabyjfd"
pattern = "abcaby"
result = find_all_matches_kmp(text, pattern)
print(result)  # Output: [6]
