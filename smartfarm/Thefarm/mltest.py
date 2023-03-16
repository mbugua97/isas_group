import pickle

# Load the saved model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

new_data = [[72, 65]] # Example new data with temperature 20 and humidity 80
prediction = model.predict(new_data)


print(prediction)