# Simplification of: Late multimodal fusion for image and audio music transcription


![Tensorflow](https://img.shields.io/badge/Tensorflow-%FFFFFF.svg?style=flat&logo=Tensorflow&logoColor=orange&color=white) [![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)]() 


## About

Branch from [`Late multimodal fusion for image and audio music transcription`]([10.5281/zenodo.6797870](https://github.com/mariaalfaroc/late-fusion-music-transcription)). Simplification to use only AMT features.


## How To Use

### Dataset

We use the [**Camera-PrIMuS**](https://grfia.dlsi.ua.es/primus/) dataset.

The Camera-PrIMuS dataset contains 87&nbsp;678[^2] real-music incipits[^3], each represented by six files: (i) the Plaine and Easie code source, (ii) an image with the rendered score, (iii) a distorted image, (iv) the musical symbolic representation of the incipit both in Music Encoding Initiative format (MEI) and (v) in an on-purpose simplified encoding (semantic encoding), and (vi) a sequence containing the graphical symbols shown in the score with their position in the staff without any musical meaning (agnostic encoding).

[^2]: In this work, we consider 22&nbsp;285 samples out of the total 87&nbsp;678 that constitute the complete Camera-PrIMuS dataset. This selection resulted from a data curation process, primarily involving the removal of samples containing long multi-rests. These music events contribute minimally to the length of the score image but may span a large number of frames in the audio signal.

[^3]: An incipit is a sequence of notes, typically the first ones, used for identifying a melody or musical work.

## Experiments

To replicate our experiments, you will first need to meet certain requirements specified in the [`Dockerfile`](Dockerfile). Alternatively, you can set up a virtual environment if preferred. Once you have prepared your environment (either a Docker container or a virtual environment) and followed the steps in the [dataset](#dataset) section, you are ready to begin. Follow this recipe to replicate our experiments:

```bash
$ cd dataset
$ python main.py
```


**Citation**

```bibtex
@article{alfaro2023late,
  author       = {Alfaro-Contreras, Mar{\'i}a and Valero-Mas, Jose J. and I{\~n}esta, Jose M. and Calvo-Zaragoza, Jorge},
  title        = {{Late multimodal fusion for image and audio music transcription}},
  journal      = {Expert Systems with Applications},
  volume       = {216},
  pages        = {119491},
  year         = {2023},
  issn         = {0957-4174}
}
```

----

**Requirements**

tensorflow-gpu==2.3.1<br />
pandas==1.3.0<br />
numpy==1.18.5<br />
opencv-python==4.5.3.56<br />
swalign==0.3.6
