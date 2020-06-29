import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
r = requests.get(url)
htmlcode = r.content
soup = BeautifulSoup(htmlcode, 'html.parser')

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup, 'html.parser')
# print(type(soup2.string))
# exit()

# get the html code of page
value = soup.prettify()
# find all of this tag
paras = soup.find_all('p')

# find first of this tag
# print(soup.find('p'))


# find with specific notation
# print(soup.find('p', class_='lead'))

# get the content of given line
# print(soup.find('p').get_text())

links = soup.find_all('a')
all_links = set()
for link in links:
    # print(link.get('href'))
    if(link.get('href') != '#'):
        linktext = "https://codewithharry.com" + link.get('href')
        all_links.add(linktext)
        # print(linktext)

# .content dont need itration or you can use itration also
navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent.contents)

# .children need an itartor to print its childrens but is is fast because i not use extra memory
# for itm in navbarSupportedContent.children:
#     # print(itm)

# for printing the contnt within that tag or you can use stripped_strings for removiung the extrra space b/w output
# for itms in navbarSupportedContent.strings:
#     print(itms)


# for getting the parent or parents of the div

# print(navbarSupportedContent.parent)

# for item in navbarSupportedContent.parents:
    # print(item.name)


# for previous and next sibilings

# print(navbarSupportedContent.next_sibling.next_sibling)
# for item in navbarSupportedContent.previous_siblings:
#     print(item)

# using id ans clas # and .
# elem = soup.select('#loginModal')
# print(elem)
elem = soup.select('.modal-footer')
print(elem)