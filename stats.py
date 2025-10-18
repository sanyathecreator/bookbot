def get_words_count(content):
    words = content.split()
    return len(words)

def get_chars_count(content):
    chars = list(content.lower())
    result = {}
    for char in chars:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def sort_on(items):
    return items["num"]

def get_sorted_pairs(chars, nums):
    pairs = []
    for i in range(len(chars)):
        pairs.append({"char" : chars[i], "num" : nums[i]})

    pairs.sort(reverse=True, key=sort_on)
    return pairs
