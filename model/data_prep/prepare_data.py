import pandas as pd
import os

base_dir = "/Users/princekeshri/Desktop/SIH_2025/model"
data_path = os.path.join(base_dir, "data", "soil.csv")
processed_dir = os.path.join(base_dir, "processed_data")
os.makedirs(processed_dir, exist_ok=True)

df = pd.read_csv(data_path)
print("dataset loaded - ", df.shape)

X = df.drop('label', axis=1)
y = df['label']

X.to_csv(os.path.join(processed_dir, "features.csv"), index=False)
y.to_csv(os.path.join(processed_dir, "labels.csv"), index=False)

print("features saved - ", os.path.join(processed_dir, "features.csv"))
print("labels saved - ", os.path.join(processed_dir, "labels.csv"))