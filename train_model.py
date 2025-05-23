from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save the trained model
model_path = os.path.join("model", "iris_model.pkl")
joblib.dump(model, model_path)

print(f"Model trained and saved to {model_path}")