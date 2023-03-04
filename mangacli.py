from bs4 import BeautifulSoup
import requests
import webbrowser
from rich.console import console

ms = input("\nSearch for Manga: \n")
msl = ms.split()
source = requests.get("https://m.manganelo.com/search/story/"+ '_'.join(msl)).text

soup = BeautifulSoup(source, 'lxml')

manga_dict = {}
chap_dict = {}

print("\n\nSearch Results:\n ")

# fetches the manga titles and saves them in a dictionary
c = 1
for a in soup.find_all('a', class_ = 'item-img'):

    m_name = a['title']
    print(str(c)+ ") " + m_name)
    print()

    manga_dict[c] = m_name
    c+= 1

# searches for the manga in the dictionary : corresponding to the number selected

ask = int(input('\nSelect the number corresponding to the manga you want to read: \n'))

for k in range(1,len(manga_dict)+1):
    if k == ask:
        manga_select = manga_dict[k]
    
print("\nSelected Manga: ",manga_select)


# sends request to manga page and fetches the list of chapters

for a in soup.find_all('a', class_ = 'item-img'):
    if a['title'] == manga_select:
        manga_page = a['href']

#print(manga_page)

source2 = requests.get(manga_page).text
soup2 = BeautifulSoup(source2, 'lxml')

print("\nChapter List:\n ")

c = 1
for a in soup2.find_all('a', class_ = 'chapter-name text-nowrap'):
    chap_name = a['title']
    print(str(c) + ') ' + chap_name)
    print()

    chap_dict[c] = chap_name
    c += 1


ask2 = int(input('\nSelect the number coresponding to the chapter you want to read:\n '))

for k in range(1,len(chap_dict)+1):
    if k == ask2:
        chap_select = chap_dict[k]


for a in soup2.find_all('a', class_ = 'chapter-name text-nowrap'):
    if a['title'] == chap_select:
        chap_url = a['href']


print('\nYou selected the chapter: ', chap_select)

print("\nNow redirecting to the chapter...")

webbrowser.register('mozilla',
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe")
)


webbrowser.get('mozilla').open(chap_url)











