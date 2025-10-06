import joblib
import pandas as pd

model = joblib.load("../soil_model.pkl")

test_data = [35,25,20,24,75,6.0,110]

sample_input = {
    "N": test_data[0],
    "P": test_data[1],
    "K": test_data[2],
    "temperature": test_data[3],
    "humidity": test_data[4],
    "ph": test_data[5],
    "rainfall": test_data[6]
}



input_df = pd.DataFrame([sample_input])

probabilities = model.predict_proba(input_df)[0]  #prob array
crop_labels = model.classes_  #crop name

results = pd.DataFrame({
    "Crop": crop_labels,
    "Probability": probabilities
}).sort_values(by="Probability", ascending=False)

print(results.to_string(index=False))