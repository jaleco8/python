# Make an example of prediction in Python (In the Administration area)
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the sales data
sales_data = pd.read_csv('sales_data.csv')

# Create a model
model = LinearRegression()

# Create a dictionary that maps each month to a numerical value
month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

# Apply the dictionary to the 'Month' column
sales_data['Month'] = sales_data['Month'].map(month_to_num)

# Train the model
model.fit(sales_data[['Month']], sales_data['Revenue'])

# Make a prediction for December
prediction = model.predict([[12]]) # type: ignore

# Print the prediction
print('The predicted revenue for December is $ {:.2f}'.format(prediction[0]))