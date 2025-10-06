import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

x = pd.read_csv("./processed_data/features_n.csv")
y = pd.read_csv("./processed_data/labels_n.csv").squeeze()

rf_model = RandomForestClassifier(n_estimators=1300,max_depth=None,min_samples_split=2,min_samples_leaf=1,bootstrap=True,random_state=42,n_jobs=-1)
# tree no.  |  max tree depth  |  smallest split  |  smallest leaf  |  random subsets  | |  using all cpu cores

rf_model.fit(x, y)

joblib.dump(rf_model, "./soil_model.pkl")
print("done")