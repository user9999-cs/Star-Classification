from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_read_data(filepath):
    read_data = pd.read_csv(filepath)
    return read_data


data = load_read_data("6 class csv.csv")

# label encoder
label_encoder = LabelEncoder()
data['Star color'] = label_encoder.fit_transform(data['Star color'])
data['Spectral Class'] = label_encoder.fit_transform(data['Spectral Class'])

# Normalize numerical data
scaler = StandardScaler()
data[['Temperature (K)', 'Luminosity(L/Lo)',
      'Radius(R/Ro)', 'Absolute magnitude(Mv)']] = scaler.fit_transform(data[['Temperature (K)',
                                                                              'Luminosity(L/Lo)', 'Radius(R/Ro)',
                                                                              'Absolute magnitude(Mv)']])

# Split the data into features (X) and target (y)
X = data.drop('Star type', axis=1)
y = data['Star type']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
