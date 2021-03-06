<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ADMP/blob/master/example/pulseai_logo.png'>
</div>

<h1 align="center">
   ConvolutionBox
</h1>

---
<p align="center">
    <em>ConvolutionBox is a convenient tool for convolution visualization, whicn can help you design the architecture of the CNN.</em>
    <br>
    <a>
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"> 
    </a>
    <a>
        <img src="https://img.shields.io/badge/Browser-Chrome-red.svg">
    </a>
    <a>
        <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Passing">
    </a>
    <a href="https://github.com/pyecharts/pyecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://pypi.org/project/pyecharts/">
        <img src="https://img.shields.io/badge/python-3.x-blue.svg" >
    </a>
</p>
<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ConvolutionBox/blob/master/example/index.gif'>
</div>

---
# Introduction

Different tasks, different data, of course, different models.In orader to establish the best CNN architecture, 
we can use the **NAS** to find it, but it takes much time and the result is instable.Most of the time, we just need 
to try different moudle like '**Inception**', '**Continuous convolution**' and so on.**Tensorboard** is best visualization API that I've 
ever used, but it always need a complete network and generate log, which is convenient for training but not for designing,
because sometimes we just need to know the capability of the module.So I build the **ConvolutionBox**, which can figuratively
described as a 'Convolution calculator', and it will help you rapidly get the behavior of moudle.Hope you will enjoy that!   

<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ConvolutionBox/blob/master/example/conv.png'>
</div>

# Language & Frame & Browser

**Language**:

Python3 + HTML + JavaScript

**Frame**:

Flask 1.0.2 + Echarts 4.x

**Browser**

Gooogle Chrome is recommended

# Usage

## Convolution

The "**Convlution**" moudle will accept an image, then perform four consecutive convolution operations and display the feature maps obtained from each operation.At last, it will generate the gray histograms of the first three convolution features.Before you click the "Go", just make sure all the parameters are filled in or you'll get '**Internel server error**'.

**Arg**：

* Filter Size: An reasonable positive integer.

* Filter Strides: An reasonable positive integer.

* Padding: Just make a descion, and 'SAME' is recommended.

**Attention**:

All the feature maps you generated will be saved in the '**static/images/conv**'

In future versions, we will add more types of convolution operations like '**Pointwise convolution**', '**Deepwise separable convolution**' and so on.

## Pooling

<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ConvolutionBox/blob/master/example/pooling.png'>
</div>

The "**Pooling**" moudle will accept a feature image, then perform two kinds of operations——"MaxPooling" and "AveragePooling",and display the feature maps obtained from each operation.At last, it will generate the gray histograms of the features.Before you click the "Go", just make sure all the parameters are filled in or you'll get '**Internel server error**'.

**Arg**：

* Pool Size: An reasonable positive integer.

* Filter Strides: An reasonable positive integer.

* Padding: Just make a descion, and 'SAME' is recommended.

**Attention**:

All the feature maps you generated will be saved in the '**static/images/pooling**'

## Extractor

<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ConvolutionBox/blob/master/example/extractor.png'>
</div>

The "**Extractor**" moudle contains lots of convolution networks such as 'LeNet5', 'AlexNet', 'ResNet'.The moudle will accept an image, then use the predefined CNN to extract the feature maps.And it will generate the gray histograms of the features.Before you click the "Go", just make sure all the parameters are filled in or you'll get '**Internel server error**'.

**Args**:
* Extractor: The type of extractor.And the supported extractor for current version is as below:

|||Type||||
|--|--|--|--|--|--|
|LeNet5|AlexNet|VGGNet16|VGGNet19|RestNet34|ResNet50|

**Attention**:

All the feature maps you generated will be saved in the '**static/images/extractor**'

## Augmentation

<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ConvolutionBox/blob/master/example/augmentation.png'>
</div>

The "**Augmetation**" moudle provides the function of images data augmetation, with this moudle, you can efficiently accomplish the data augmentation task.In the current version, 9 processing methods are supported:

||**Method**||
|:--:|:-:|:-:|
|rotate|zoom in|zoom out|
|shear|noise|mirroring|
|saturation adjustment|contrast ratio adjustment|brightness adjustment|

Before you click the "Go", just make sure all the parameters are filled in or you'll get '**Internel server error**'.


**Args**:
* Methods: The method to augment your data.
* Input Path: The folder of the images to be processed.

* Output Path: The foleder to save the processed images.

* Amplification factor: An reasonable integer which indicts the amplification factor.


**Attention**:

You can do more elaborate operations by changing the source code.


# Get it now
Clone it：
```
$ git clone https://github.com/Mingqi-Yuan/ConvolutionBox.git
```
or  you can get the zip file，then make a  **Flask project** with **PyCharm**.
```
$  wget https://codeload.github.com/Mingqi-Yuan/ConvolutionBox/zip/master
```


# Packages required
The moudle below is required for the ConvolutionBox:


* TensorFlow
* Matplotlib
* Flask
* json
* NumPy
* OpenCV

The python environment of **Anaconda3** is recommended.

---

# License
[MIT License](LICENSE)

