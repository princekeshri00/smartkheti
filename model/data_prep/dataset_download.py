import kagglehub
import os
import pandas as pd

project_data_dir = "/Users/princekeshri/Desktop/SIH_2025/model/data"
os.makedirs(project_data_dir,exist_ok=True)

download_path = kagglehub.dataset_download("atharvaingle/crop-recommendation-dataset")

csv_path = os.path.join(download_path, "Crop_recommendation.csv")
local_csv_path = os.path.join(project_data_dir,"soil.csv")

df = pd.read_csv(csv_path)
df.to_csv(local_csv_path,index=False)

print("Dataset download + saved - " + local_csv_path)
print("Dataset shape - ",df.shape)
print("Columns - ",df.columns.tolist())
print("Unique crops - ",df['label'].nunique())