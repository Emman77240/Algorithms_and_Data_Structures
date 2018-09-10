#-------------------------------------------------------------------------------
# Name:        To check for HTML document for proper opening  and closing tags.
# Purpose:
#
# Author:      mmk  ,bamise and emmanuel
#
# Created:     30/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import Stack as s
import os.path
#from nose.tools import nottest

#===============================================================================
 #create a function that check if the file itself exit
#===============================================================================

def file_exist(text):

    '''file_exist(FileName),it return a boolean True if file exist or False if not'''

     #check if the file itself exit
    if os.path.isfile(text):
        return True
    else:
        return False

#===============================================================================
#create a function that read a file and return a list
#===============================================================================

def read_file(text):

    '''A read file function read_file(FileName),it return a string'''
  #check if the file itself exit
    if file_exist(text):

      #open the file
      read_text=open(text,"r")

      #read the file all the line at once
      content =read_text.read()

      #strip the string for blank spaces

      strip_string=content.replace(" ","")

      #close the file
      read_text.close()


      return strip_string

#===============================================================================
#create a function that check if a html document is proper tags
#===============================================================================

def is_html_tag_properly(enter_file_name):

    '''is_html_tag_properly(string data type),it return a boolean True if html tag
       properly or false if otherwise'''
    #implement a stack object for  stacking "<>" characters
    stack_one=s.Stack()

    # implement a stack object for  stacking "/" character
    stack_two=s.Stack()

    #a boolean to check if it is the first time on stack_two
    is_first_time_stack2=True

    #transverse through the string
    for i,v in enumerate(enter_file_name):

       # check to see if the value contain "<" ,">" or "/"
         if v=="<" or v=="/" or v==">" :

          #check which special tag if < or > push or pop
          if v=="<" or v==">":
            #push "<" only
             if v=="<":
                #push it to stack _one
                stack_one.push(v)
            #else is ">" pop it out of the stack_one
             else:
                 #pop it out of stack_one
                     stack_one.pop()

          else:
             #if it is the first time we encounter the  character push it to stack_two
              if is_first_time_stack2:

                #push it to stack_two
                stack_two.push(v)

                #set is_first_time_stack2 to false
                is_first_time_stack2=False
              else:
                #check if  stack_two is empty if empty push or do otherwise (pop)
                  if stack_two.is_empty():
                    #push "/" it to stack_two since it is empty
                    stack_two.push(v)
                  else:
                    #since it is not empty pop it out of stack_two
                    stack_two.pop()


         else:
            pass

     #check if stack_one is empty and  also stack_two(which deal with "/") is not empty

    if stack_one.is_empty() and stack_two.is_empty()==False:
         return True

    else:
        return False






def main():
    #pass

    file="HTMLDOC.txt"

    html_doc=read_file(file)
    print(is_html_tag_properly(html_doc))


if __name__ == '__main__':
    main()
