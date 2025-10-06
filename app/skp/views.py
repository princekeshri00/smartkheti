import os
import pandas as pd
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'model', 'soil_model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = joblib.load(f)

CROP_CLASSES = model.classes_

@csrf_exempt
def predict_crop(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            input_df = pd.DataFrame([data])

            probabilities = model.predict_proba(input_df)[0]
            crop_probs = list(zip(CROP_CLASSES, probabilities))
            
            top_crops = sorted(crop_probs, key=lambda x: x[1], reverse=True)[:7]
            total_prob = sum([prob for crop,prob in top_crops])

            response_data = {crop: round(prob/total_prob*100, 1) for crop, prob in top_crops}
            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
