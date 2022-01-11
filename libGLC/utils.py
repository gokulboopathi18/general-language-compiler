
import re

def remove_items(test_list, item):
      
    # remove the item for all its occurrences
    for i in test_list:
        if(i == item):
            test_list.remove(i)
  
    return test_list

def stringsplit(string):
    words = re.split("([ \n\t\(\)\"\'=+*-;:<>\|\&\{\}#\~])", string)
    # remove_items(words, " ")
    remove_items(words, "")
    # remove_items(words, "\t")
    # remove_items(words, "\n")
    return words


def writeArray(code):
    total_code = ""
    for line in code:
        cur_str = ""
        for word in line:
            cur_str +=word

        total_code+=cur_str
    return total_code
