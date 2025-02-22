import pandas as pd

index = 0
countries = ["USA", "Russia", "UK", "South Korea"]

def extract_movie_data(file_name):
    return pd.read_csv(file_name)

def add_new_column(data):
    data["box_office"] = pd.to_numeric(data["box_office"], errors="coerce")
    data["budget"] = pd.to_numeric(data["budget"], errors="coerce")
    data["balance"] = (data["box_office"] - data["budget"])
    return data

def filter_countries(data):
    mask = (data["country"] == countries[index])
    return data[mask]

def sort_data(data):
    return data.sort_values(by="balance", ascending = False)

def drop_data(data):
    data.drop(index = data.index[10:], axis=0, inplace=True)
    data.drop(["language", "country", "duration", "budget", "box_office"], axis=1, inplace=True)
    return data

def load_data(data):
    data.to_excel(f"{countries[index]}.xlsx", index=False)

for _ in range(len(countries)): 
    df = extract_movie_data("movies.csv").pipe(filter_countries).pipe(add_new_column).pipe(sort_data).pipe(drop_data).pipe(load_data)
    index += 1
    

    

    
