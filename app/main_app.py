# Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import time


# Loading the Model

@st.cache_resource
def load_my_model():
    """Load model once into cache to improve performance
    """
    return load_model('models/dog_breed.h5')

try:
    model = load_my_model()
except FileNotFoundError:
    st.error("Error: 'dog_breed.h5' model file not found. Please ensure the file is in the same directory as the app or provide the correct path.")
    st.stop()

# Name of Classes
CLASS_NAMES = ['pekinese', 'walker_hound', 'boxer', 'otterhound',
               'english_setter', 'dhole', 'toy_poodle', 'border_terrier',
               'norwegian_elkhound', 'shih-tzu', 'kuvasz', 'german_shepherd',
               'greater_swiss_mountain_dog', 'australian_terrier',
               'rhodesian_ridgeback', 'appenzeller', 'samoyed', 'border_collie',
               'entlebucher', 'collie', 'malamute', 'chihuahua', 'saluki',
               'komondor', 'bull_mastiff', 'bernese_mountain_dog', 'lhasa',
               'scotch_terrier', 'miniature_pinscher', 'brabancon_griffon',
               'toy_terrier', 'flat-coated_retriever',
               'soft-coated_wheaten_terrier', 'siberian_husky', 'briard',
               'chesapeake_bay_retriever', 'beagle', 'vizsla',
               'west_highland_white_terrier', 'kerry_blue_terrier', 'whippet',
               'japanese_spaniel', 'curly-coated_retriever', 'pembroke',
               'silky_terrier', 'sussex_spaniel', 'german_short-haired_pointer',
               'french_bulldog', 'english_springer', 'rottweiler']

# Setting Title of App
st.title("Dog Breed Prediction")
st.markdown("Upload an image of your dog to predict its breed!")

# Sidebar for Dog Breed List and Search
with st.sidebar:
    st.subheader("Supported Dog Breeds")
    
    # Create a search bar for search feature
    search_query = st.text_input("Search breed:", key="search_bar")
    
    # Display search results only when search bar has content
    if search_query:
        st.subheader("Search Results:")
        filtered_breeds = [breed for breed in CLASS_NAMES if search_query.lower() in breed.lower()]
        
        if filtered_breeds:
            for breed in filtered_breeds:
                st.write(f"• {breed}")
        else:
            st.info("No matching breeds found.")
    
    # Separate section for all breeds (not affected by search)
    st.markdown("---")
    st.subheader("All Supported Breeds")
    
    # Create a container with scrollable content for all breeds
    breed_container = st.container()
    with breed_container:
        # Show first 10 breeds by default
        show_all = st.checkbox("Show all breeds", False)
        
        if show_all:
            # Display all breeds
            for breed in CLASS_NAMES:
                st.write(f"• {breed}")
        else:
            # Display only first 10 breeds
            for breed in CLASS_NAMES[:10]:
                st.write(f"• {breed}")
            if len(CLASS_NAMES) > 10:
                st.write(f"_...and {len(CLASS_NAMES) - 10} more breeds_")
                st.write("_Check 'Show all breeds' to view the complete list_")

# Main area for image upload and prediction
dog_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
predict_button = st.button('Predict Breed')

if predict_button:
    if dog_image is not None:
        try:
            # Convert the file to an OpenCV image
            file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)

            # Displaying the image
            st.image(opencv_image, channels="BGR", caption="Uploaded Image")

            # Resizing the image
            img_resized = cv2.resize(opencv_image, (224, 224))
            # Convert image to 4 Dimension
            img_expanded = np.expand_dims(img_resized, axis=0)
            # Normalize the image (assuming your model expects normalized input)
            img_normalized = img_expanded / 255.0

            # Make Prediction
            Y_pred = model.predict(img_normalized)
            predicted_class_index = np.argmax(Y_pred)
            predicted_breed = CLASS_NAMES[predicted_class_index]
            confidence = Y_pred[0][predicted_class_index] * 100

            # Displaying the prediction result
            st.subheader("Prediction Result:")
            st.write(f"The predicted dog breed is: **{predicted_breed.replace('_', ' ').title()}**")
            st.write(f"Confidence: **{confidence:.2f}%**")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please upload a dog image to make a prediction.")