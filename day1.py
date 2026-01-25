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

def diseases_stats(file_name): 
     data = pd.read_csv(file_name)
     data_filter = data[data['Disease'] != 'Healthy']
     return { 
          'total_diseases' : len(data_filter),
          'diseases_by_crop' : data_filter.groupby('Crop_name').size().to_dict(),
          'avg_confidence' : data_filter['Confidence_score'].mean(),
          'low_confidence' : data_filter[data_filter['Confidence_score'] < 0.9]['Disease'].tolist()
    }

diseases_summary = diseases_stats('crop_diseases.csv')
print(diseases_summary)

def student_summary(names,scores):
     summary = {}
     for name, score in zip (names,scores):
          if name not in summary and score > 70:
               summary[name] = score
     return summary
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
scores = [85, 67, 90, 45, 78, 88]
student_results = student_summary(students, scores)
print(student_results)