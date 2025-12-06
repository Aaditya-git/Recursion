from collections import Counter, defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

anagrams = defaultdict(list)

for str in strs:
    key = " ".join(sorted(str))
    anagrams[key].append(str)

print(list(anagrams.values()))


