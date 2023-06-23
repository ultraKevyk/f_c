import requests
import csv
import pickle
import os


data_dir = "./website/data/downloaded_data/"

clean_fish = {"kapr": "Kapr obecný", "lín": "Lín obecný", "cejn": "Cejn velký", "tloust":"Jelec tloušť", "okoun": "Okoun říční", "parma":"Parma obecná", "ostroretka": "Ostroretka stěhovavá",
              "podoustev": "Podoustev říční", "štika": "Štika obecná", "candát": "Candát obecný", "sumec": "Sumec velký", "úhoř": "Úhoř říční", "pstruh obecný": "Pstruh obecný",
              "pstruh duhový": "Pstruh duhový", "lipan": "Lipan podhorní", "siven": "Siven americký", "bolen": "Bolen dravý", "maréna peleď" :"Maréna peleď",
              "hlavatka": "Hlavatka obecná", "amur" :"Amur bílý", "tolstolobik": "Tolstolobik bílý", "karas": "Karas", "mník": "Mník jednovousý", "jelec jesen": "Jelec jesen"
}

def average_weight(area, fish):     # calculate average weight of specific fish on specific area
    with open(data_dir + area + ".csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if fish in row:
                try:
                    average_weight = float((row)[2]) / float((row)[1])
                except Exception:
                    break
                return average_weight


def fish_ratio(area, fish, area_size):  # calculate fish/ha ratio on specific area
    with open(data_dir + area + ".csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if fish in row:
                try:
                    ratio = float((row)[1]) / area_size
                except Exception:
                    print()
                    break
                return ratio


def global_average_weight(directory, fish):     # Getting average weight for specific fish on all areas
    total_weight = 0
    num_weights = 0
    weight = 0
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            with open(os.path.join(directory, file), "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if fish in row:
                        try:
                            total_weight += (float(row[2]) / float(row[1]))
                            num_weights += 1
                        except Exception:
                            continue
        try:
            weight = total_weight / num_weights
        except Exception:
            continue
    return  weight


def global_average_ratio(directory, fish, area_sizes):
    total_ratio = 0
    num_ratios = 0
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            with open(os.path.join(directory, file), "r", encoding="utf-8") as file:
                file.name
                name = os.path.basename(file.name).strip(".csv")
                reader = csv.reader(file)
                for row in reader:
                    if fish in row:
                        try:
                            total_ratio += float(row[1]) / area_sizes[name]
                            num_ratios += 1
                        except Exception:
                            continue

    return  total_ratio / num_ratios