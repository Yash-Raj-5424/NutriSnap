import tensorflow as tf
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import json
import os
import urllib.request


def download_if_missing(filename, url):
    """Download a file from GitHub if it doesn't already exist locally."""
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded: {filename}")


def analyze_food_image(image_path, top_n=3):
    """Complete food analysis from image to nutrition visualization with automatic GitHub downloads."""

    # === 1. GitHub download URLs (REPLACE with your actual raw URLs) ===
    MODEL_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_recognition_model.h5'
    CLASS_INDICES_URL = 'https://github.com/your-username/your-repo/raw/main/models/class_indices.json'
    NUTRI_MODEL_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_nutrition_predictor.pkl'
    ENCODER_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_label_encoder.pkl'

    # === 2. Download files if missing ===
    download_if_missing('food_recognition_model.h5', MODEL_URL)
    download_if_missing('class_indices.json', CLASS_INDICES_URL)
    download_if_missing('food_nutrition_predictor.pkl', NUTRI_MODEL_URL)
    download_if_missing('food_label_encoder.pkl', ENCODER_URL)

    try:
        # === 3. Load models and encoders ===
        model = tf.keras.models.load_model('food_recognition_model.h5')
        with open('class_indices.json') as f:
            class_indices = json.load(f)
        nutri_model = joblib.load('food_nutrition_predictor.pkl')
        encoder = joblib.load('food_label_encoder.pkl')

        # === 4. Load and preprocess image ===
        img = image.load_img(image_path, target_size=(150, 150))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # === 5. Predict food classes ===
        preds = model.predict(img_array)[0]
        top_indices = np.argsort(preds)[-top_n:][::-1]

        # === 6. Predict nutrition ===
        results = []
        for i in top_indices:
            food = class_indices[str(i)]
            try:
                encoded = encoder.transform([food])
                nutri = nutri_model.predict(pd.DataFrame({'food_encoded': encoded}))[0]
                results.append({
                    'Food': food,
                    'Confidence': f"{preds[i]:.1%}",
                    'Calories': round(nutri[0], 1),
                    'Fat (g)': round(nutri[1], 1),
                    'Carbs (g)': round(nutri[2], 1),
                    'Protein (g)': round(nutri[3], 1)
                })
            except ValueError:
                print(f"Could not predict nutrition for: {food}")
                continue

        # === 7. Visualization ===
        if results:
            df = pd.DataFrame(results)
            nutrients = ['Calories', 'Fat (g)', 'Carbs (g)', 'Protein (g)']
            plt.figure(figsize=(15, 12))
            for i, nutrient in enumerate(nutrients, 1):
                plt.subplot(2, 2, i)
                sizes = df[nutrient]
                plt.pie(sizes, labels=df['Food'], autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'white'})
                plt.title(nutrient)
            plt.tight_layout()
            plt.show()
            return df

        return pd.DataFrame()

    except Exception as e:
        print("Something went wrong during analysis:", e)
        return pd.DataFrame()
import tensorflow as tf
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import json
import os
import urllib.request


def download_if_missing(filename, url):
    """Download a file from GitHub if it doesn't already exist locally."""
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded: {filename}")


def analyze_food_image(image_path, top_n=3):
    """Complete food analysis from image to nutrition visualization with automatic GitHub downloads."""

    # === 1. GitHub download URLs (REPLACE with your actual raw URLs) ===
    MODEL_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_recognition_model.h5'
    CLASS_INDICES_URL = 'https://github.com/your-username/your-repo/raw/main/models/class_indices.json'
    NUTRI_MODEL_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_nutrition_predictor.pkl'
    ENCODER_URL = 'https://github.com/your-username/your-repo/raw/main/models/food_label_encoder.pkl'

    # === 2. Download files if missing ===
    download_if_missing('food_recognition_model.h5', MODEL_URL)
    download_if_missing('class_indices.json', CLASS_INDICES_URL)
    download_if_missing('food_nutrition_predictor.pkl', NUTRI_MODEL_URL)
    download_if_missing('food_label_encoder.pkl', ENCODER_URL)

    try:
        # === 3. Load models and encoders ===
        model = tf.keras.models.load_model('food_recognition_model.h5')
        with open('class_indices.json') as f:
            class_indices = json.load(f)
        nutri_model = joblib.load('food_nutrition_predictor.pkl')
        encoder = joblib.load('food_label_encoder.pkl')

        # === 4. Load and preprocess image ===
        img = image.load_img(image_path, target_size=(150, 150))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # === 5. Predict food classes ===
        preds = model.predict(img_array)[0]
        top_indices = np.argsort(preds)[-top_n:][::-1]

        # === 6. Predict nutrition ===
        results = []
        for i in top_indices:
            food = class_indices[str(i)]
            try:
                encoded = encoder.transform([food])
                nutri = nutri_model.predict(pd.DataFrame({'food_encoded': encoded}))[0]
                results.append({
                    'Food': food,
                    'Confidence': f"{preds[i]:.1%}",
                    'Calories': round(nutri[0], 1),
                    'Fat (g)': round(nutri[1], 1),
                    'Carbs (g)': round(nutri[2], 1),
                    'Protein (g)': round(nutri[3], 1)
                })
            except ValueError:
                print(f"Could not predict nutrition for: {food}")
                continue

        # === 7. Visualization ===
        if results:
            df = pd.DataFrame(results)
            nutrients = ['Calories', 'Fat (g)', 'Carbs (g)', 'Protein (g)']
            plt.figure(figsize=(15, 12))
            for i, nutrient in enumerate(nutrients, 1):
                plt.subplot(2, 2, i)
                sizes = df[nutrient]
                plt.pie(sizes, labels=df['Food'], autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'white'})
                plt.title(nutrient)
            plt.tight_layout()
            plt.show()
            return df

        return pd.DataFrame()

    except Exception as e:
        print("Something went wrong during analysis:", e)
        return pd.DataFrame()
