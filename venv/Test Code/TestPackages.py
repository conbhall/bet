import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a DataFrame with some sample data
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Using NumPy to add a noise column
np.random.seed(0)
df['Noise'] = np.random.normal(0, 1000, size=len(df))

# Show updated DataFrame
print("\nUpdated DataFrame with noise:")
print(df)

# Prepare data for linear regression
X = df[['Age', 'Noise']]  # Features
y = df['Salary']          # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Predict the values
predictions = model.predict(X_test)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, predictions)

print(f"\nPredictions: {predictions}")
print(f"Mean Squared Error: {mse}")
