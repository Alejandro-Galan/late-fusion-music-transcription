# -*- coding: utf-8 -*-

import os, shutil

import tensorflow as tf

import config
from experimentation import k_fold_experiment, k_fold_test_experiment

from word_graphs.smith_waterman import k_fold_multimodal_experiment as sw_k_fold_multimodal_experiment
from confusion_networks.cn_combination import k_fold_multimodal_experiment as cn_k_fold_multimodal_experiment
from word_graphs.wg_decoded_evaluation import k_fold_multimodal_experiment as cwg_k_fold_multimodal_experiment, k_fold_light_multimodal_experiment as light_cwg_k_fold_multimodal_experiment

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"
tf.config.list_physical_devices("GPU")

if __name__ == "__main__":
    epochs = 150

    config.set_data_globals()
    config.set_arch_globals(batch=4)

    print("Starting experiment of", epochs, "epochs")
    # Train the model:
    k_fold_experiment(epochs)

    # STAND-ALONE EVALUATION
    # Evaluate the model
    k_fold_test_experiment()



