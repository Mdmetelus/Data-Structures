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
                return
            elif current.value > target:
                
            else:
                

  def get_max(self):
    pass

  def for_each(self, cb):
    pass