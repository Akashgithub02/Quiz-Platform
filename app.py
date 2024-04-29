

from flask import Flask, render_template, request, send_from_directory
import os
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Set up a folder to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = tf.keras.models.load_model('dental.keras')

# Labels used during training
labels = ['dental caries', 'enamel erosion', 'gum disease', 'oral cancer', 'sensitive teeth', 'tooth loss']

# Function to preprocess the input image
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(299, 299))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array

# Function to make predictions
def predict_image(img_array):
    predictions = model.predict(img_array)
    score = tf.nn.sigmoid(predictions[0])
    class_index = np.argmax(score)
    class_name = labels[class_index]
    confidence = int(100 * np.max(score))
    return class_name, confidence

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image from the form
        uploaded_file = request.files['file']
        
        if uploaded_file.filename != '':
            # Save the uploaded file to the upload folder
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.jpg')
            uploaded_file.save(image_path)
            
            # Preprocess the image
            img_array = preprocess_image(image_path)
            
            # Make predictions
            class_name, confidence = predict_image(img_array)
            
            # Render the result on the frontend along with the uploaded image
            return render_template('result.html', class_name=class_name, confidence=confidence, image_path=image_path)

    # Render the main page
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Create the uploads folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    app.run(debug=True)
