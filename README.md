# counter
A simple incrementer in python

## Usage
Use as a simple incrementer of word
```
binary_counter = Counter()
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.start(['0', ''])
iter_binary_counter = iter(binary_counter)
print(next(iter_binary_counter))
# output => '00'
print(next(iter_binary_counter))
# output => '01'
```