from bs4 import BeautifulSoup
import requests
import webbrowser
from termcolor import colored
from pyfiglet import Figlet
import colorama


colorama.init()

print(colored("*"*75, 'green'))

f = Figlet(font="isometric2")
print(colored(f.renderText("MangaCli"),'red', attrs=['bold','underline']))

print(colored("*"*75, 'green'))


ms = input(colored("\nSearch for Manga: \n", 'red', attrs=['bold','underline']))
msl = ms.split()
source = requests.get("https://m.manganelo.com/search/story/"+ '_'.join(msl)).text

soup = BeautifulSoup(source, 'lxml')

manga_dict = {}
chap_dict = {}

print(colored("\n\nSearch Results:\n ", 'green', attrs=['underline']))

# fetches the manga titles and saves them in a dictionary
c = 1
for a in soup.find_all('a', class_ = 'item-img'):

    m_name = a['title']
    titletext = str(c)+ ") " + m_name
    print(colored(titletext, 'red'))
    # print()

    manga_dict[c] = m_name
    c+= 1


# searches for the manga in the dictionary : corresponding to the number selected

ask = int(input('\nSelect the number corresponding to the manga you want to read:\n'))

for k in range(1,len(manga_dict)+1):
    if k == ask:
        manga_select = manga_dict[k]
    
print(colored("\nSelected Manga: " + manga_select, 'green', 'on_red', attrs=['bold']))

print(colored("-"*75, 'green'))

# sends request to manga page and fetches the list of chapters

for a in soup.find_all('a', class_ = 'item-img'):
    if a['title'] == manga_select:
        manga_page = a['href']

#print(manga_page)

source2 = requests.get(manga_page).text
soup2 = BeautifulSoup(source2, 'lxml')

print(colored("\nChapter List:\n ", 'green', attrs=['bold', 'underline']))

c = 1
for a in soup2.find_all('a', class_ = 'chapter-name text-nowrap'):
    chap_name = a['title']
    chaptext = (str(c) + ') ' + chap_name)
    print(colored(chaptext, 'blue'))

    chap_dict[c] = chap_name
    c += 1


ask2 = int(input('\nSelect the number coresponding to the chapter you want to read:\n '))

for k in range(1,len(chap_dict)+1):
    if k == ask2:
        chap_select = chap_dict[k]


for a in soup2.find_all('a', class_ = 'chapter-name text-nowrap'):
    if a['title'] == chap_select:
        chap_url = a['href']


print(colored('\nYou selected the chapter: '+ chap_select, 'green', 'on_red', attrs=['bold']))

print("\nNow redirecting to the chapter...")

webbrowser.register('mozilla',
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe")
)


webbrowser.get('mozilla').open(chap_url)











