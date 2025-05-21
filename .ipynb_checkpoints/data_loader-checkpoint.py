import requests 
import pandas as pd 
import os 

def get_dataset(url: str , file_name : str ) -> pd.DataFrame:
    file_path = f"Data/{file_name}.csv"
    if os.path.exists(file_path): 
        print("File already exists")
    else: 
        print("File doesn't exists. Downloading ...............")
        response = requests.get(url)
        with open(f"Data/{file_name}.csv" , "wb") as f: 
            f.write(response.content)
    return pd.read_csv(f"Data/{file_name}.csv")


        