"""
MIT License

Copyright (c) 2019 Mingqi Yuan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/31
Usage: Network---ResNet50
"""

from utils.generate_unique_id import generate_unique_id
import tensorflow as tf
import numpy as np
import cv2

tf.enable_eager_execution()


def Conv2d_BN(x, nb_filter, kernel_size, strides=(1, 1), padding='same', name=None):
    if name is not None:
        bn_name = name + '_bn'
        conv_name = name + '_conv'
    else:
        bn_name = None
        conv_name = None

    x = tf.layers.Conv2D(nb_filter, kernel_size, padding=padding, strides=strides, activation='relu', name=conv_name)(x)
    x = tf.layers.BatchNormalization(axis=3, name=bn_name)(x)
    return x

def Conv_Block(inpt, nb_filter, kernel_size, strides=(1, 1), with_conv_shortcut=False):
    x = Conv2d_BN(inpt, nb_filter=nb_filter, kernel_size=kernel_size, strides=strides, padding='same')
    x = Conv2d_BN(x, nb_filter=nb_filter, kernel_size=kernel_size, padding='same')
    if with_conv_shortcut:
        shortcut = Conv2d_BN(inpt, nb_filter=nb_filter, strides=strides, kernel_size=kernel_size)
        x = tf.add(x, shortcut)
        return x
    else:
        x = tf.add(x, inpt)
        return x

def ResNet34(path_to_image):
    img_dir = path_to_image
    img_data = np.array(cv2.imread(img_dir, 1)).astype('float32')
    img_data = cv2.resize(img_data, (224, 224))
    img_data = tf.reshape(img_data, [1, img_data.shape[0], img_data.shape[1], 3])

    x = Conv2d_BN(img_data, nb_filter=64, kernel_size=(7, 7), strides=(2, 2), padding='valid')
    x = tf.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)
    # (56,56,64)
    x = Conv_Block(x, nb_filter=64, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=64, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=64, kernel_size=(3, 3))
    # (28,28,128)
    x = Conv_Block(x, nb_filter=128, kernel_size=(3, 3), strides=(2, 2), with_conv_shortcut=True)
    x = Conv_Block(x, nb_filter=128, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=128, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=128, kernel_size=(3, 3))
    # (14,14,256)
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3), strides=(2, 2), with_conv_shortcut=True)
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=256, kernel_size=(3, 3))
    # (7,7,512)
    x = Conv_Block(x, nb_filter=512, kernel_size=(3, 3), strides=(2, 2), with_conv_shortcut=True)
    x = Conv_Block(x, nb_filter=512, kernel_size=(3, 3))
    x = Conv_Block(x, nb_filter=512, kernel_size=(3, 3))
    x = tf.layers.AveragePooling2D(pool_size=(7, 7), strides=2)(x)

    feature = x.numpy()
    feature = feature.astype('uint8')
    feature = np.reshape(feature, [32, 16])

    result_dir = 'static/images/extractor/' + 'ResNet34_' + generate_unique_id()
    cv2.imwrite(result_dir, feature)

    return result_dir


