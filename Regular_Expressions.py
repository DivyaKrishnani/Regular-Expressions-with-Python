
# coding: utf-8

# ## REGULAR EXPRESSIONS 
# 
# Regular expressions are a tool for matching patterns in text.Regular expressions are used to sift through text-based data to find things. Regular expressions express a pattern of data that is to be located.
# 
# Some rules in regular expressions:
# 
# Identifiers:
# 
#     \d = any number
#     \D = anything but a number
#     \s = space
#     \S = anything but a space
#     \w = any letter
#     \W = anything but a letter
#     . = any character, except for a new line
#     \b = space around whole words
#     \. = period. must use backslash, because . normally means any character.
# 
# Modifiers:
# 
#     {1,3} = for digits, u expect 1-3 counts of digits, or "places"
#     + = match 1 or more
#     ? = match 0 or 1 repetitions.
#     * = match 0 or MORE repetitions
#     $ = matches at the end of string
#     ^ = matches start of a string
#     | = matches either/or. Example x|y = will match either x or y
#     [] = range, or "variance"
#     {x} = expect to see this amount of the preceding code.
#     {x,y} = expect to see this x-y amounts of the precedng code
# 
# White Space Charts:
# 
#     \n = new line
#     \s = space
#     \t = tab
#     \e = escape
#     \f = form feed
#     \r = carriage return
# 
# Characters to REMEMBER TO ESCAPE IF USED!
# 
#     . + * ? [ ] $ ^ ( ) { } | \
# 
# Brackets:
# 
#     [] = quant[ia]tative = will find either quantitative, or quantatative.
#     [a-z] = return any lowercase letter a-z
#     [1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
#     
#Example - 1 :
#A list of names and their corresponding ages can be obtaine dfrom a text
# In[1]:


import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

ages = re.findall(r'\d{1,3}',exampleString) #2-3 digits
names = re.findall(r'[A-Z][a-z]*',exampleString) #any capital letter followed by any no.of small letters stops when a whilespace/fullstop comes

print(ages)
print(names)


# In[9]:


list = [ "mouse", "cat", "dog", "no-match"]
for element in list:
    m = re.match("(d\w+) \W(d/w+)" , element)  #\w’ means word-character & + (plus) symbol denotes one-or-more
    print(m)


# In[10]:


list = [ "mouse", "cat", "dog", "no-match"]
for element in list:
    m = re.match("(d\w+)" , element)  
    print(m)


# In[11]:


list = [ "mouse", "cat", "dog", "no-match"]
for element in list:
    m = re.match("(d\w+)" , element)
    if m:
        print(m.groups())


# In[14]:


value = "cyberdyne"
g = re.search("(dy.*)",  value)
if g:
    print("search: " ,g.group(1))
s = re.match("(vi.*)", value)
if s:
    print("match:", m.group(1))


# In[25]:


phone = "2004-959-559 # This is Phone Number"

num = re.sub('#.*$', "", phone) #Deletes python style comments
print(num)

# Remove anything other than digits
num = re.sub('\D', "", phone)  #every non-digit replaced by ""
print(num)


# In[30]:


line  = "Python is my favourite programming language"

search = re.search('(.*)',line) 
print(search.group())
#group() returns all matching subgroups


# # Searching an email address 

# In[40]:


email_text = "div.krish@gmail.com is an email address"
search_email = re.search('([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)',email_text)
# email expressed as series of letters ,dots followed by @ sign followed by again a series of letters ,dots
print(search_email.group())


# # Removing an email address

# In[41]:


email_para = "div.krish@gmail.com is an email address also dev.krish@gmail is an email address "
search_email = re.search('([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)',email_para)
removed_email = re.sub('([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)'," ",email_para)
print(removed_email)


# # Remove Hashtag

# In[54]:


hashtag_text = "A wonderful holiday spent at Paris #paris #Holidays #family"
remove_hashtag_list = re.sub("([^0-9A-Za-z \t])","",hashtag_text).split()
remove_hashtag = ' '.join(re.sub("([^0-9A-Za-z \t])","",hashtag_text).split())
print("Removed Hashtag list :")
print(remove_hashtag_list)
print("Removed Hashtag text: " + remove_hashtag)


# # Removing URL, usernames ...
# 

# In[53]:


# Removing website links, # , @..tagging
example = '@divya I love that dress at #Max. https://pythonprogramming.net/# '
#strips of an URL (not just http), any punctuations, User Names or Any non alphanumeric characters

processed_list = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",example).split()
processed = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",example).split())
print("processed list :")
print(processed_list)
print("processed text: " + processed)

