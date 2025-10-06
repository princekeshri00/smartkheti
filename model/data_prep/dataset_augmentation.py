import pandas as pd
import numpy as np

df = pd.read_csv("../processed_data/features.csv")
labels = pd.read_csv("../processed_data/labels.csv")

noise_fraction = 0.05  # +-5%
augment_factor = 10 

augmented_data = []
augmented_labels = []

for _ in range(augment_factor):
    noisy_features = df.copy()
    
    for col in df.columns:
        #+- 5% gaussian noise
        noise = np.random.normal(0, noise_fraction * (df[col].max() - df[col].min()), size=len(df))
        noisy_features[col] += noise
    
    augmented_data.append(noisy_features)
    augmented_labels.append(labels)

df_augmented = pd.concat([df] + augmented_data, ignore_index=True)
labels_augmented = pd.concat([labels] + augmented_labels, ignore_index=True)

df_augmented = df_augmented.sample(frac=1).reset_index(drop=True)
labels_augmented = labels_augmented.sample(frac=1).reset_index(drop=True)

df_augmented.to_csv("../processed_data/features_n.csv", index=False)
labels_augmented.to_csv("../processed_data/labels_n.csv", index=False)

print("done -> ", df_augmented.shape)