import pandas as pd
from sklearn.linear_model import LinearRegression

# Load historical stock prices into a pandas dataframe
df = pd.read_csv('stock_prices_sample.csv')

# Split the data into training and testing sets
train_data = df[:-100]
test_data = df[-100:]

# Create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(train_data[['OPEN', 'HIGH', 'LOW']], train_data['CLOSE'])

# Use the model to make predictions on the test data
predictions = model.predict(test_data[['OPEN', 'HIGH', 'LOW']])

# Print the predicted stock prices for the test data
print(predictions)