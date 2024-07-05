def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Iterate through each possible starting position in text
    for i in range(n - m + 1):
        # Check for pattern match starting at position i
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:
            # If inner loop completes without breaking, a match is found
            print(f"Pattern found at index {i}")

# Example usage:
text = "ababcababcabcabc"
pattern = "abc"
brute_force_string_match(text, pattern)
