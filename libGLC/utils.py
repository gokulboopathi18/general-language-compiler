
import re

def remove_items(test_list, item):
      
    # remove the item for all its occurrences
    for i in test_list:
        if(i == item):
            test_list.remove(i)
  
    return test_list

def stringsplit(string):
    words = re.split("([ \n\t\(\)\"\'=+*-;:]|==)", string)
    remove_items(words, " ")
    remove_items(words, "")
    remove_items(words, "\t")
    remove_items(words, "\n")
    return words
