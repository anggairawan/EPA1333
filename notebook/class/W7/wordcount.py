#!/opt/local/bin/python3

# import system library
import sys

# fucntion that counts words
def count_words(data):
   words = data.split(" ")
   num_words = len(words)
   return num_words

# function that count lines
def count_lines(data):
   lines = data.split("\n")
   for l in lines:
      if not l:
         lines.remove(l)
   return len(lines)

# This is the default function that is called when the program is executed
if __name__ == "__main__":
    # If there is more then one argument we quit 
    if len(sys.argv) < 2:
        print("Usage: python wordcount.py <file>")
        exit(1)
    # otherwise we open the file that was passed as argument
    filename = sys.argv[1]
    f = open(filename, "r")
    data = f.read()
    f.close()

# count the words and lines
num_words = count_words(data)
num_lines = count_lines(data)

# and print them on screen
print("The number of words: ", num_words)
print("The number of lines: ", num_lines)
 
