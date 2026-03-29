from sklearn.ensemble import IsolationForest
import numpy as np
# Let's say we track "Number of Requests per Minute"
# Most users do 5-10 requests. A hacker might do 500.
data = np.array([8,10])

# Train the AI
model = IsolationForest(contamination=0.2) # We expect 20% to be "weird"
model.fit(data)

# Predict
predictions = model.predict(data) 

for i, pred in enumerate(predictions):
    status = "Normal" if pred == 1 else "ANOMALY DETECTED"
    print(f"Request Count: {data[i]} -> Result: {status}")
