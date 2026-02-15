import sys
import time
import re
from collections import Counter, defaultdict
import numpy as np

filename = '/Users/dmitryromanov/Desktop/web/web lb7/sopranos.txt'

# top n words
def top_n_words(file_path, n=3):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = re.findall(r'\w+', text.lower())
    long_words = [w for w in words if len(w) >= 3]
    counts = Counter(long_words)
    print(counts.most_common(n))

# merge dicts
def merge_dicts(data):
    result = defaultdict(int)
    for item in data:
        try:
            user = item.get('user')
            money = item.get('sum')
            if isinstance(user, str) and isinstance(money, (int, float)):
                result[user] += money
        except:
            continue
    print(dict(result))

# timer
class Timer:
    def __init__(self, name, stream=sys.stdout):
        self.name = name
        self.stream = stream
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() - self.start) * 1000
        print(f"[{self.name}] took {round(elapsed,3)} ms", file=self.stream)


if __name__ == "__main__":
    top_n_words(filename, n=5)
    print("\t")
    users_data = [{'user': 'Tony', 'sum': 1000},{'user': 'Paulie', 'sum': 500},
                  {'user': 'Tony', 'sum': 200}, {'user': 'Chris', 'sum': 'error'},  # type error
                  {'missing_key': 123}] # key ignore
    merge_dicts(users_data)
    print("\t")
    size = 10_000_000
    py_list = list(range(size))
    np_array = np.arange(size)
    with Timer("Python List sum"):
        sum(py_list)
    with Timer("Numpy sum"):
        np_array.sum()
