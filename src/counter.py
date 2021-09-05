from src.unit import Unit

class Counter :

  iter_unit_list = []
  overflow_iteration = 1
  end_word = ''
  word = ''

  def __init__(self) :
    self.iteration = 0
    self.iter_unit_list = []
    self.overflow_iteration = 1
    self.end_word = ''
    self.word = ''

  def __iter__(self) :
    return self

  def __next__(self) :
    self.iteration += 1
    # if end_word is reached
    if (self.end_word != '') & (self.end_word == self.word) :
      raise StopIteration('This is the word of the end !')
    # if last iteration
    if self.overflow_iteration > len(self.iter_unit_list) :
      raise StopIteration('This is the end of the word !')
    try :
      iter_unit = self.iter_unit_list[len(self.iter_unit_list) - self.overflow_iteration]
      next(iter_unit)
    except StopIteration :
      # overflow
      iter_unit.reset()
      self.overflow_iteration += 1
      return next(self)
    else :
      self.overflow_iteration = 1
      self.word = ''
      for incrementation in self.iter_unit_list :
        self.word += incrementation.value
      return self.word

  # function named "strike" only for the joke but it's "append" in fact
  def strike(self, collection) :
    self.iter_unit_list.append(iter(Unit(collection)))
    return self
  # start at the specific position
  def start(self, state) :
    i = 0
    while i < len(self.iter_unit_list) :
      if state[i] != '' :
        unit = self.iter_unit_list[i]
        unit.start(state[i])
      i += 1
    return self
  # end at the specific position
  def end(self, state) :
    i = 0
    self.end_word = ''
    while i < len(self.iter_unit_list) :
      self.end_word += state[i]
      i += 1
    return self