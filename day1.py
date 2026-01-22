import numpy as np 
import pandas as pd 

sample_data = {
     'Crop_name': ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean'],
     'Disease' : ['Rust', 'Blast', 'Smut', 'Powdery Mildew', 'Root Rot'],
     'Confidence_score': [0.95, 0.89, 0.92, 0.85, 0.90],
     'Region' : ['Lagos', 'Nairobi', 'Cairo', 'Johannesburg', 'Accra']
}

df = pd.DataFrame(sample_data)
df.to_csv('crop_diseases.csv', index=False)
print(df)

def explore_dataset(file_name):
     data = pd.read_csv(file_name)
     return { 
          'shape' : data.shape,
          'columns' : data.columns.tolist(),
          'dtypes': data.dtypes.to_dict(),
          'missing_values': data.isna().sum().to_dict()
     }

summary = explore_dataset('crop_diseases.csv')
print(summary)