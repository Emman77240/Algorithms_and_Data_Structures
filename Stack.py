#-------------------------------------------------------------------------------
# Name: Stack Implementation
# Purpose:
#
# Author:      mmk  ,bamise and emmanuel
#
# Created:     30/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
#Completed implementation of stack Abstract Data Type assuming the end of the list
#to be the exit(the entry point) while the base is at list index[0]

class Stack:

   def __init__(self):

      self.items = []

   def is_empty(self):

      return self.items == []

   def push(self, item):

     self.items.append(item)

   def pop(self):

      return self.items.pop()

   def peek(self):

     return self.items[len(self.items)-1]

   def size(self):

      return len(self.items)



def main():
    pass


if __name__ == '__main__':
    main()
