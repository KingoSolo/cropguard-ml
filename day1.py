import numpy as np 
import pandas as pd 

sample_data = {
     'Crop_name': ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean'],
     'Disease' : ['Rust', 'Blast', 'Smut', 'Powdery Mildew', 'Root Rot'],
     'confidence_score': [0.95, 0.89, 0.92, 0.85, 0.90],
     'region' : ['Lagos', 'Nairobi', 'Cairo', 'Johannesburg', 'Accra']
}

df = pd.DataFrame(sample_data)
df.to_csv('crop_diseases.csv', index=False)
print("DataFrame created and saved to 'crop_diseases.csv'")
print(df)