import os
import shutil
import urllib2
import numpy as np

NUM_CHARS = len("00001")
NUM_IMAGES = 14779# hardcoded, sorry guys...
ROOT_FOLDER = os.path.join(os.path.dirname(__file__), "spin_pics")
TEST_FOLDER = os.path.join(ROOT_FOLDER, "test")
ALL_FOLDER = os.path.join(ROOT_FOLDER, "all")
MODE = "TEST"

if os.path.exists(ROOT_FOLDER):
  shutil.rmtree(ROOT_FOLDER)
os.mkdir(ROOT_FOLDER)
os.mkdir(TEST_FOLDER)
os.mkdir(ALL_FOLDER)

if MODE == "TEST":
  for i in range(1, 24 + 1):
    s = ('%0'+str(NUM_CHARS)+'d.jpg')%i
    response = urllib2.urlopen('https://www.fotomada.gr/files/orkomosies/180719_HLEKTROLOGOI_MHX/original/' + s)
    with open(os.path.join(TEST_FOLDER, s),'wb') as output:
      output.write(response.read())
elif MODE == "ALL":
  for i in range(1, 24 + 1):
    s = ('%0'+str(NUM_CHARS)+'d.jpg')%i
    response = urllib2.urlopen('https://www.fotomada.gr/files/orkomosies/180719_HLEKTROLOGOI_MHX/original/' + s)
    with open(os.path.join(TEST_FOLDER, s),'wb') as output:
      output.write(response.read())

# response = urllib2.urlopen('http://www.example.com/')
# html = response.read()