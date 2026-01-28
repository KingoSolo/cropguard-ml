import numpy as np 
# import pandas as pd 

# sample_data = {
#      'Crop_name': ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean'],
#      'Disease' : ['Rust', 'Blast', 'Smut', 'Powdery Mildew', 'Root Rot'],
#      'Confidence_score': [0.95, 0.89, 0.92, 0.85, 0.90],
#      'Region' : ['Lagos', 'Nairobi', 'Cairo', 'Johannesburg', 'Accra']
# }

# df = pd.DataFrame(sample_data)
# df.to_csv('crop_diseases.csv', index=False)
# print(df)

# def explore_dataset(file_name):
#      data = pd.read_csv(file_name)
#      return { 
#           'shape' : data.shape,
#           'columns' : data.columns.tolist(),
#           'dtypes': data.dtypes.to_dict(),
#           'missing_values': data.isna().sum().to_dict()
#      }

# summary = explore_dataset('crop_diseases.csv')
# print(summary)

# def diseases_stats(file_name): 
#      data = pd.read_csv(file_name)
#      data_filter = data[data['Disease'] != 'Healthy']
#      return { 
#           'total_diseases' : len(data_filter),
#           'diseases_by_crop' : data_filter.groupby('Crop_name').size().to_dict(),
#           'avg_confidence' : data_filter['Confidence_score'].mean(),
#           'low_confidence' : data_filter[data_filter['Confidence_score'] < 0.9]['Disease'].tolist()
#     }

# diseases_summary = diseases_stats('crop_diseases.csv')
# print(diseases_summary)

# def student_summary(names,scores):
#      summary = {}
#      for name, score in zip (names,scores):
#           if name not in summary and score > 70:
#                summary[name] = score
#      return summary
# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
# scores = [85, 67, 90, 45, 78, 88]
# student_results = student_summary(students, scores)
# print(student_results)



# Exercise 1: Create blank image array
def create_image_array(height, width):
    np_array = np.zeros((height,width))
    return np_array


# Exercise 2: Normalize data 
def normalize_array(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.zeros(arr)
    
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized


# Exercise 3: Threshold/binarize image
def threshold_image(image, threshold=128):
    return np.where(image >= threshold, 255, 0)


# Test cases (run these to verify your code):
if __name__ == "__main__":
    # Test 1: Create blank image
    blank = create_image_array(100, 100)
    print("Test 1 - Blank image shape:", blank.shape)
    print("Should be: (100, 100)")
    
    # Test 2: Normalize array
    test_arr = np.array([10, 50, 100, 200, 255])
    normalized = normalize_array(test_arr)
    print("\nTest 2 - Normalized values:", normalized)
    print("Should be close to: [0. 0.163 0.367 0.776 1.]")
    
    # Test 3: Edge case - all same values
    same_vals = np.array([5, 5, 5, 5])
    normalized_same = normalize_array(same_vals)
    print("\nTest 3 - Normalized same values:", normalized_same)
    print("Should be: [0. 0. 0. 0.]")
    
    # Test 4: Threshold image
    test_image = np.array([[50, 100, 150], 
                           [200, 250, 75]])
    binary = threshold_image(test_image, threshold=128)
    print("\nTest 4 - Binary image:")
    print(binary)
    print("Should be:\n[[  0   0 255]\n [255 255   0]]")

