def words_count(text):
    words = text.split()
    return len(words)

def char_counts(text):
    words = text.lower()
    counts = {}
    for abc in words:
        if abc not in counts:
            counts[abc] = 1
        else:
            counts[abc] = counts[abc] + 1
    return counts

def sorted(dict):
    sorted_list = []
    for word in dict:
        entry = {"char": word, "num" : dict[word]}
        sorted_list.append(entry)
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]
