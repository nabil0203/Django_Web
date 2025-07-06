# Same as 5.03_Collections_Module-3.py
# Change in import sytle


from collections import defaultdict                 # only imported defaultdict of collections module



word_dic = defaultdict(list)                         # as only 'defaultdict' is imported, no need to write-> 'collections.defaultdict(list)' 

word_dic['Python'].append("PROGRAMMING")                
word_dic['Python'].append("LANGUAGE")

word_dic['Name'].append("Nabil")                       
word_dic['Name'].append("Ahmed")


print(word_dic)