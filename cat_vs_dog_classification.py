import streamlit as st
from fastai.vision.all import *

st.title("Cat vs Dog Classifier")
st.text("Created by Preslie Tong")

def cat_or_dog(file_name):
    if file_name[0].isupper(): #same as == True
        return "CAT"
    else:
        return "DOG"

cat_vs_dog_model = load_learner("cat_vs_dog_fastai_2_7_19.pkl")

uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "png", "jpeg"])
if uploaded_file:
    real_img = PILImage.create(uploaded_file)
    resized_img = real_img.resize((224, 224), Image.NEAREST)
    prediction = cat_vs_dog_model.predict(resized_img)
