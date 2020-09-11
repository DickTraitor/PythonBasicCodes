import re

#raw strings
print("\t hello world")
print(r"\t hello world")

text = '''
    abcdfasdt asdg
    abc trwa abc dadd asdf 
    abcbcbcbbcabc *foo
    123123123123 
    123.456.3899
    800-123-1232
    900-123-1675
    801-345-3455
    cat
    mat
    bat
    pat
    Rat


    Mr.Rea
    Ms.Gadsf
    Mr faldsfj
    Mr... lkdsfjla
    
    CoreyMsSchafer@gmail.com
    corey.ms@university.edu
    corey-scafer234@my-work.net

    http://www.google.com
    https://www.nasa.gov
    http://youtube.com
    https://facebook.com
    www.instagram.com
    '''
text2="asdfadsfasdfa adsfasdfasdfasdf"

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text)
for match in matches:
    print(match)
# using quantiiers now
print("Using Quantifiers now")
pattern = re.compile(r'\d{3}.\d+.\d+')
matches = pattern.finditer(text)
for match in matches:
    print(match)

print("\nnew--------------------------------------------------------------------\n")
# helps matching the phone numbers that have  in between and not all the chars..
pattern = re.compile(r'\d\d\d[.]\d\d\d[.]\d\d\d\d')
matches = pattern.finditer(text)
for match in matches:
    print(match)
print("\nnew--------------------------------------------------------------------\n")
# now we need to match only numbers starting with 80 or 90 
pattern = re.compile(r'[89]0[0-9][-]\d\d\d[-]\d\d\d\d')
matches = pattern.finditer(text)
for match in matches:
    print(match)
print("\nnew--------------------------------------------------------------------\n")
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text)
for match in matches:
    print(match)
print("\nnew--------------------------------------------------------------------\n")
# matching everything except bat (only 3 letter words wnding with at))
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text)
for match in matches:
    print(match)

print("\nnew--------------------------------------------------------------------\n")
# we want to match Mr Mr. 
pattern = re.compile(r'Mr\.{0,3}w*') #or Mr\.? 
matches = pattern.finditer(text)
for match in matches:
    print(match)
print("\nnew--------------------------------------------------------------------\n")
# matching everything except bat (only 3 letter words wnding with at))
pattern = re.compile(r'\w+') # matches all the word character till word ends ..
matches = pattern.finditer(text2)
for match in matches:
    print(match)

print("\nnew--------------------------------------------------------------------\n")
#  wrinting the regex for email finding in the text file
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') # matches all the word character till word ends ..
matches = pattern.finditer(text)
for match in matches:
    print(match)

# writing the emails and getting f = open('university_towns.txt','r')
# string_list = f.readlines()
# f.close()
# for line in range(0,len(string_list),1):
#     string_list[line] = re.sub(r"(\w+)(\s?\w+)\s?(,?\s?)((\([^\n]*\)?|\[(\w+)*\]))+",r'\1\2\3',string_list[line])

# a = open('university_towns.txt','w')
# a.writelines(string_list)
# a.close()
,text)
print(subbed_urls) # prints some extra contents also...
 
print("\nnew--------------------------------------------------------------------\n")

pattern = re.compile(r'Mr\.{0,3}w*')
match = pattern.findall(text)
# findall returns the tuple of groups 
for match in matches:
    print(match) 
text ='''Alabama[edit]
Auburn (Auburn University)[1]
Florence (University of North Alabama)
Jacksonville (Jacksonville State University)[2]
Livingston (University of West Alabama)[2]
Montevallo (University of Montevallo)[2]
Troy (Troy University)[2]
Tuscaloosa (University of Alabama, Stillman College, Shelton State)[3][4]
Tuskegee (Tuskegee University)[5]
Alaska[edit]
'''