import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

print("Loading genomic feature matrix...")
data = pd.read_csv("amr_clinical_data.csv")

# 1. Feature Selection & Preprocessing
features = ["k_mer_frequency", "mutation_score", "plasmid_count", "efflux_pump_active"]
target = "resistance_status"

X = data[features]
y = data[target]

# Neural networks require scaled data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 2. Train the Deep Learning Model (Multi-Layer Perceptron)
print("Training Deep Neural Network (MLPClassifier)...")
# Structure: 2 hidden layers with 64 and 32 neurons
dl_model = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=500, random_state=42)
dl_model.fit(X_train, y_train)

# 3. Evaluate the Model
predictions = dl_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report (Susceptible = 0, Resistant = 1):")
print(classification_report(y_test, predictions))