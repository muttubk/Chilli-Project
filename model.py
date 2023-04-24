# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
import pickle



with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


#Code from ChillFolderML
import numpy as np

# load the saved model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
        


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import cv2

fixed_size = tuple((256, 256))

from functions_pack import rgb_bgr
from functions_pack import bgr_hsv
from functions_pack import img_segmentation
from functions_pack import fd_hu_moments
from functions_pack import fd_haralick
from functions_pack import fd_histogram
import tempfile

def predict_result(img_obj):
    print(img_obj)
    img = Image.open(img_obj)
    img = img.save("img.jpg")
    image = cv2.imread("img.jpg")
#     st.image(image, caption="Original image")
    image = cv2.resize(image, fixed_size)
# Running Function Bit By Bit
    RGB_BGR       = rgb_bgr(image)
    BGR_HSV       = bgr_hsv(RGB_BGR)
    IMG_SEGMENT   = img_segmentation(RGB_BGR,BGR_HSV)

    # Call for Global Fetaure Descriptors
    fv_hu_moments = fd_hu_moments(IMG_SEGMENT)
    fv_haralick   = fd_haralick(IMG_SEGMENT)
    fv_histogram  = fd_histogram(IMG_SEGMENT)

    # Concatenate 
    global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments])

    new_feature = global_feature.reshape(1, -1)
    pred=model.predict(new_feature)
    
    return pred[0]

# # Preparing and pre-processing the image
# def preprocess_img(img_path):
#     op_img = Image.open(img_path)
#     img_resize = op_img.resize((224, 224))
#     img2arr = img_to_array(img_resize) / 255.0
#     img_reshape = img2arr.reshape(1, 224, 224, 3)
#     return img_reshape


# # Predicting function
# def predict_result(predict):
#     pred = model.predict(predict)
#     return np.argmax(pred[0], axis=-1)

