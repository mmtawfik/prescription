import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import datetime

def create_prescription(image_data, patient_name, date, day, birthday, prescription):
    image = Image.open(BytesIO(image_data))
    image = image.convert("RGB")  # Convert image to RGB mode
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 28)

    draw.text((50, 50), "Patient Name:", (0, 0, 0), font=font)
    draw.text((50, 80), "Date:", (0, 0, 0), font=font)
    draw.text((50, 110), "Day:", (0, 0, 0), font=font)
    draw.text((50, 140), "Birthday:", (0, 0, 0), font=font)
    draw.text((50, 170), "Prescription:", (0, 0, 0), font=font)

    draw.text((220, 395), patient_name, (0, 0, 0), font=font)
    draw.text((745, 395), date, (0, 0, 0), font=font)
    draw.text((200, 110), day, (0, 0, 0), font=font)
    draw.text((300, 455), birthday, (0, 0, 0), font=font)
    draw.text((200, 500), prescription, (0, 0, 0), font=font)

    image.save('prescription.jpg', format='JPEG')  # Save as JPEG format
    st.image(image, caption='Prescription', use_column_width=True)

def display_image(image_data):
    image = Image.open(BytesIO(image_data))
    st.image(image, caption='Input Image', use_column_width=True)

def create_app():
    st.title('Create Prescription App')
    st.markdown("This app helps you create a prescription by filling in the details.")

    patient_name = st.text_input("Patient Name", "")
    prescription_date = datetime.date.today().strftime("%d-%m-%Y")
    day = datetime.datetime.today().strftime("%A")
    birthday = st.date_input("Patient's Birthday")
    prescription = st.text_area("Prescription")

    image_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
    submit = st.button("Create Prescription")

    if submit:
        if image_file is not None:
            image_data = image_file.read()
            create_prescription(image_data, patient_name, prescription_date, day, str(birthday), prescription)
        else:
            create_prescription(None, patient_name, prescription_date, day, str(birthday), prescription)

if __name__ == '__main__':
    create_app()