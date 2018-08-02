import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
# from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import os

ROOT_FOLDER = os.path.join(os.path.dirname(__file__), "spin_pics")
TEST_FOLDER = os.path.join(ROOT_FOLDER, "test")
ALL_FOLDER = os.path.join(ROOT_FOLDER, "all")
INTERMIDIATE_FOLDER = os.path.join(ROOT_FOLDER, "intermidiate")
MODE = "TEST"



inputShape = (299, 299)
preprocess = preprocess_input

model = InceptionV3()
# model.build()

# load images, process them and save to files
# sess = tf.Session()
for img in os.listdir(TEST_FOLDER):
  image = load_img(os.path.join(TEST_FOLDER,img), target_size=inputShape)
  pr_image = preprocess(tf.expand_dims(tf.keras.preprocessing.image.img_to_array(image),axis=0))
  result = model.apply(pr_image)
  result = model.output
  # sess.run(result)
  print(np.shape(result))
  break
# cluster objects inside them using WKNN


# use billinear transform in order to get shapes in initial images