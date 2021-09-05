class Unit :

  value = ''
  end_value = ''
  start_value = ''

  def __init__(self, collection):
    self.collection = collection
    self.start_value = collection[0]

  def start(self, value) :
    self.value = value
    self.start_value = value
    return self

  def end(self, value) :
    self.end_value = value
    return self

  def reset(self) :
    self.value = self.start_value
    return self

  def __iter__(self) :
    return self

  def __next__(self) :
    if(self.value != '') :
      value_index = self.collection.index(self.value)
    else :
      value_index = -1
    next_value_index = value_index + 1
    if next_value_index == len(self.collection) :
      raise StopIteration('end of the collection !')
    self.value = self.collection[next_value_index]
    if(self.value == self.end_value) :
      raise StopIteration('end value reached !')
    return self.value