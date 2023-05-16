import qrcode
#import cv2
import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#st.set_option('deprecation.showfileUploaderEncoding', False)





def predict_note_authentication(Link):
  image=qrcode.make(Link)
  image.save("sunrise.jpg")
  image = Image.open('sunrise.jpg')
  
  

  
  return image

def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">LINK TO QR-CODE CONVERTER </p></center> 

   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.header("Enter The URL")
    UserID = st.text_input("Link","")

    resul=""
    if st.button("Get QR Code"):
      result=predict_note_authentication(UserID)
      st.image(result)
    if st.button("About"):
      st.subheader("Developed by Jayant kumar")
      st.subheader(" Department of Computer Engineering")

if __name__=='__main__':
  main()
   
