import pandas as pd

data = {
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool'],
    'Forecast': ['Same', 'Same', 'Change', 'Same'],
    'EnjoySport': ['Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

concepts = df.iloc[:, :-1].values
target = df.iloc[:, -1].values

hypothesis = ['0'] * len(concepts[0])

for i in range(len(target)):
    if target[i] == "Yes":
        for j in range(len(hypothesis)):
            if hypothesis[j] == '0':
                hypothesis[j] = concepts[i][j]
            elif hypothesis[j] != concepts[i][j]:
                hypothesis[j] = '?'

print("Final Hypothesis:")
print(hypothesis)
