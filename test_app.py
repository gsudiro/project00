# unittest for app
import unittest
import os
import sys
from app import autoCompleteRequest 
from auto_complete import autoComplete

class testAutoComplete(unittest.TestCase):

# testing itself.  
   def test(self):         
      self.assertTrue(True) 
if __name__ == '__main__': 
   unittest.main() 

# Checking methods' parameters
def testFunction(self):
   # first right, second right, third right
   self.assertRaises(TypeError,autoCompleteRequest, "complete", "ab", 3 )
   # first right, second right, third wrong
   self.assertRaises(TypeError,autoCompleteRequest, "complete", "ab", "ab" )
   # first right, second wrong, third right
   self.assertRaises(TypeError,autoCompleteRequest, "complete", 3, 3 )
   # first right, second wrong, third wrong
   self.assertRaises(TypeError,autoCompleteRequest, "complete", 3, "ab" )
   # first wrong, second right, third right
   self.assertRaises(TypeError,autoCompleteRequest, 3, "ab", 3 )
   # first wrong, second right, third wrong
   self.assertRaises(TypeError,autoCompleteRequest, 3, "ab", "ab" )
   # first wrong, second wrong, third right
   self.assertRaises(TypeError,autoCompleteRequest, 3, 3, 3 )
   # first wrong, second wrong, third wrong
   self.assertRaises(TypeError,autoCompleteRequest, 3, 3, "ab" )


class testFile(unittest.TestCase):

   def testFileExists(self):
      # check if file exists
      self.assertTrue(os.path.exists("./corpus.txt"))

'''class testComplete(unittest.TestCase):

   def testCompleteCommand(self):
      # check if "command" is specified
      self.assertAlmostEqual(autoComplete("complete".islower(),"ba".isalnum(),"3".isalnum()), True, False, True)'''