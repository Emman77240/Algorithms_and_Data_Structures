#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk  , bamise and emmanuel
#
# Created:     29/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------

def smallest_num_unsorted_list(unsortlist):

    '''smallest_num_unsorted_list([32,43,5])  and return the smallest number
      A function  that finds the smallest number in an unsorted list in
      O(nlog(n))'''

    #sort() is used because the Big-O for a sort() in a list is O(nlog(n))
    unsortlist.sort()


    return  unsortlist[0]

def main():

    print( "The smallest number in the list is :  ",smallest_num_unsorted_list([32,43,5]))

if __name__ == '__main__':
    main()
