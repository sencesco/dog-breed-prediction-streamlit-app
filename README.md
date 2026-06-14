# Dog Breed Prediction Streamlit App

A Streamlit web application that predicts a dog's breed from an uploaded image.
The app loads a trained Keras/TensorFlow model from `models/dog_breed.h5`,
preprocesses the uploaded image with OpenCV, and displays the predicted breed
with a confidence score.

## Features

- Upload dog images in `png`, `jpg`, or `jpeg` format.
- Predict one of the supported dog breeds using a trained deep learning model.
- View prediction confidence.
- Search supported breeds from the sidebar.
- Show a complete list of supported breeds.

## Project Structure

```text
.
├── app/
│   └── main_app.py
├── data/
│   └── test-data/
├── models/
│   └── dog_breed.h5
├── notebooks/
│   └── dog-breed-prediction.ipynb
├── requirements.txt
└── REAME.md
```

## Requirements

- Python 3.10 recommended
- TensorFlow 2.15.0
- Streamlit 1.31.1
- OpenCV
- NumPy

Install dependencies from `requirements.txt`.

## Build and Run

```bash
# Install Python 3.10 (recommended)

# Then recreate environment
python3.10 -m venv my_env

# Activate
source my_env/bin/activate    # Linux Bash
source my_env/Scripts/activate   # Git Bash

# Upgrade pip
pip install --upgrade pip

# If above can not work
# python.exe   -m pip install --upgrade pip

# Install again
pip install -r requirements.txt

# Run streamlit
streamlit run app/main_app.py
```

After running the command, Streamlit will print a local URL in the terminal.
Open that URL in your browser to use the app.

## How to Use

1. Start the Streamlit app.
2. Upload a dog image using the file uploader.
3. Click `Predict Breed`.
4. Review the predicted breed and confidence score.
5. Use the sidebar to search or browse supported breeds.

## Model

The application expects the trained model in this project this ,odel trained from `notebooks/dog-breed-prediction.ipynb` and model file at:

```text
models/dog_breed.h5
```

If the model file is missing or moved, the app will stop and show an error.
Keep the model file in the `models` directory unless you also update the path in
`app/main_app.py`.

## Test Images

Sample images are available in:

```text
data/test-data/
```

You can use these images to quickly test the prediction workflow.

## Supported Breeds

The app currently supports 50 dog breed classes, including:

- Siberian Husky
- French Bulldog
- Border Collie
- German Shepherd
- Beagle
- Boxer
- Rottweiler
- Chihuahua
- Samoyed
- Toy Poodle

The full breed list is available in the Streamlit sidebar.

## Notes

- The uploaded image is resized to `224x224` before prediction.
- Image pixel values are normalized by dividing by `255.0`.
- Prediction quality depends on the training data, model accuracy, image quality,
  dog pose, lighting, and whether the breed is supported by the model.

