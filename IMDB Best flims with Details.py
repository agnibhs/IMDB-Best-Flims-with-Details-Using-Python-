#Scrap List of best flim ever with link and year
from bs4 import BeautifulSoup
from selenium import webdriver
class Flim():
    def _init_(self,rank,title,year,link):
        self.rank = ''
        self.title = ''
        self.year = ''
        self.link = ''

def get_flim_list():

    driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    driver.get(url)
    #print (driver.page_source) #To Print Whole Page Source file

    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find('table', class_='chart')

    flim_list = []
    for td in table.find_all('td', class_='titleColumn'):
        #print(td.text.strip().replace('\n','').replace('      ','')) # To print list of 250 movies
        full_title = td.text.strip().replace('\n', '').replace('      ', '')
        #print(full_title)

        rank = full_title.split(".")[0]
        #print(rank)

        title = full_title.split('.')[1].split('(')[0]
        #print(title)

        year = full_title.split('(')[1][:-1]
        #print(year)

        a = td.find('a')
        #print("https://www.imdb.com/" + a['href'])

        print('\n')

        new_flim = Flim()
        new_flim.rank = rank
        new_flim.title = title
        new_flim.year = year
        new_flim.link = "https://www.imdb.com/" + a['href']

        flim_list.append(new_flim)

    driver.quit()
    return (flim_list)

flim_list = get_flim_list()

for f in flim_list:
    print(f.title)
    print(f.rank)
    print(f.year)
    print(f.link)

a = input("\n Progress Complete \n Press Enter to exit")