# -*- coding: utf-8 -*-

import pathlib


# -- DATASET GLOBAL INFO -- #

# Camera-PrIMuS
# Calvo-Zaragoza, J.; Rizo, D. Camera-PrIMuS: Neural end-to-end Optical Music Recognition on realistic monophonic scores.
# In Proceedings of the 19th International Society for Music Information Retrieval Conference, Paris. 2018, pp. 248-255


label_extn = ".krn"

base_path = "Corpus/End2End/Primus"
base_dir = pathlib.Path(base_path)
labels_dir = base_dir 

folds_dir = base_dir / "data"
output_dir = base_dir / "Outputs"


def set_data_globals():
    global image_extn
    global images_dir
    global image_flag
    # AMT
    image_extn = ".png"
    images_dir = base_dir / "converted_imgs"
    # cv2.IMREAD_UNCHANGED
    image_flag = -1


# --------------------

# AMT architecture based on:
# Miguel A. Román, Antonio Pertusa, Jorge Calvo-Zaragoza
# Data representations for audio-to-score monophonic music transcription

# filters = [8, 8]
# kernel_size = [[10, 2], [8, 5]]
# pool_size = strides = [[2, 2], [2, 1]]
# leakyrelu_alpha = 0.2
# lstm_units = [256, 256]
# lstm_dropout = 0.5

img_max_width = None

# This is true ONLY WHEN pool_size and strides have the same shape
width_reduction = 2

def set_arch_globals(batch=16):
    global img_max_height 
    global height_reduction
    global batch_size
    batch_size = batch
    # AMT
    img_max_height = 256
    height_reduction = 4
