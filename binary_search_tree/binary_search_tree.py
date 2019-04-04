class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      current = self
      given = value
      complete = False
      while not complete:
          if given < current.value:
              # add value to the left node
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(given)
                    complete = True
              if given > current.value:
                  # add value to the left node
                  if current.right:
                      current = current.right
                  else:
                      current.right = BinarySearchTree(given)
                      complete = True

  def contains(self, target):
      current = self
        complete = False
        while not complete:
            if not current:
                return False
            if current.value == target:
                return True
            elif current.value > target:
                current = current.left
            else:
                current = current.right
                

  def get_max(self):
      current = self
      while current.right is not None:
          current = current.right
      return current.value


  def for_each(self, cb):
      if self.right is None and self.left is None:
          return cb(self.value)
      else:
          if self.right:
              cb(self.value)
              self.right.for_each(cb)
          if self.left:
              cb(self.value)
              self.left.for_each(cb)