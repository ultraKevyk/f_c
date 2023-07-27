from bs4 import BeautifulSoup
import requests
import re
import csv
import pickle

# Downloads all data for fish_calc

webs = ["https://www.crsplzen.cz/rubrika/mimopstruhove-reviry-zpc-us/",
"https://www.crsplzen.cz/rubrika/mimopstruhove-reviry-zpc-us/?p=2"]
size_dict = {}
name_dict = {}
data_dir = ""


def get_links(url):     # gathering all links on page
    pattern = "/inpage/"
    links = ""
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    for link in soup.find_all('a'):
        data = link.get('href')
        if data:
            if pattern in data and "https://www.crsplzen.cz" not in data :
                links += "https://www.crsplzen.cz" + data + "#"

    return  links


def get_table(url):     # getting table of fishes/catches/weights
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    fish = []
    pieces = []
    weight = []
    rows = soup.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        if (len(data) == 11):
            fish.append(data[0].get_text())
            pieces.append(data[4].get_text())
            weight.append(data[5].get_text())
    if fish and pieces and weight:
        for i in range(2):
            fish.pop(0)
            pieces.pop(0)
            weight.pop(0)
        return fish, pieces, weight


def get_size(url):      # getting size of fishning area
    pattern = ".....ha"
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    matches = soup.find_all(['h1', 'p'])
    for match in matches:
        if "ha" in match.text:
            line = str(match)
            size = re.search(pattern, line).group()
            break
    clean_size = ""
    for i in size:
        if i.isdigit():
            clean_size += i
        elif i == ",":
            clean_size += "."
    if clean_size:
        float_size = float(clean_size)
        return float_size


def get_title(url, part):       # getting name/code of area  ## part: for 1st part - 0, for 2nd part - 1
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    title = str(soup.title(string=True))
    title = re.sub(r'\\x..', '', title)

    clean_title = ""
    if part == 0:
        for i in title:
            if i.isnumeric():
                clean_title += i
            elif i.isalpha() and len(clean_title) >= 6:
                break
    elif part == 1:
        light = False
        for i in title:
            if i.isalpha() and i.isupper():
                light = True
                clean_title += i
            elif  i.isnumeric() and light == True:
                clean_title += i
            elif i.isalpha() and light == True:
                clean_title += i
            elif  i == " " and light == True:
                clean_title += i
    return clean_title


def save_csv_table(name, table):        # saving table to *.csv
    path = data_dir + name + ".csv"
    with open(path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in range(len(table[0])):
            fish = []
            for j in range(len(table)):
                fish.append(table[j][i])
            writer.writerow(fish)
    print(name + " saved in " + name + ".csv")
    return


def save_dictionary(dictionary, name_of_dict):      # saving dictionry to file with Pickle library
    path = data_dir + name_of_dict + ".pkl"
    with open (path, 'wb') as d:
        pickle.dump(dictionary, d)
        print("Dictionary " + name_of_dict + " saved.")


def get_all_data(source):       # Getting all data (:-P)
    print("Downloading data...")
    for url in source:
        for link in (get_links(url).split('#')):
            if link:
                if get_table(link):
                    district_table = (list(get_table(link)))
                    for i in range(len(district_table[0])):
                        for j in range(len(district_table)):
                            if "," in district_table[j][i]:
                                district_table[j][i] = district_table[j][i].replace(",", ".")
                    save_csv_table(get_title(link, 0), district_table)
                    size_dict[get_title(link, 0)] = get_size(link)
                    name_dict[get_title(link, 0)] = get_title(link, 1)
                    list_of_fish = list(get_table(link)[0])
    save_dictionary(list_of_fish, "FISH")
    save_dictionary(size_dict, "SIZES")
    save_dictionary(name_dict, "NAMES")