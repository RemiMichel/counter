import src.constant as constant
from src.counter import Counter

# generate binary table
binary_counter = Counter()
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
binary_counter.strike(constant.BINARY)
# Last unit must be empty to start at the first
binary_counter.start(['0', '0', '0', '0', '0', '0', '0', ''])

iter_binary_counter = iter(binary_counter)
# for word in iter_binary_counter :
#   print(word)

# generate hexadecimal table
hexadecimal_counter = Counter()
hexadecimal_counter.strike(constant.HEXADECIMAL)
hexadecimal_counter.strike(constant.HEXADECIMAL)
# Last unit must be empty to start at the first
hexadecimal_counter.start(['0', ''])
hexadecimal_counter.end(['A', 'E'])

iter_hexadecimal_counter = iter(hexadecimal_counter)
# for word in iter_hexadecimal_counter :
#   print(word)

end = 0
i = 0
while end == 0 :
  try :
    binary_word = next(iter_binary_counter)
    hexadecimal_word = next(iter_hexadecimal_counter)
    print(str(i) + ') ' + binary_word[:4] + ' ' + binary_word[4:] + ' <=> ' + hexadecimal_word)
    i += 1
  except StopIteration :
    end = 1
