from typing import List, Union
from mmengine.dataset import BaseDataset, force_full_init

import os

import scipy
import numpy as np

class LIVEDataset(BaseDataset):

    r"""
    structure:
    {
        "data_list": [
            {
                "img_path": "path/to/image",
                "distortion_type": 1,
                "distortion_level": 1.0
            },
            ...
        ]
    }
    """
    MATAINFO = {
        'name': 'LIVE',
        'classes': ['fastfading', 'gblur', 'jp2k', 'jpeg', 'wn', 'refimgs'],
        'descriptions': {
            'fastfading': 'Fast Fading Rayleigh',
            'gblur': 'Gaussian blur',
            'jp2k': 'JPEG2000',
            'jpeg': 'JPEG',
            'wn': 'White noise in the RGB components',
            'refimgs': 'Reference images'
        },
    }
    def __init__(self, *args, **kwargs):
        super(LIVEDataset, self).__init__(*args, **kwargs)
        self.check_labels()
    
    @force_full_init
    def check_labels(self):
        for img_path, tp, level in self.data_list:
            if self._metainfo['classes'][tp] == 'refimgs':
                assert level == 0, f"Reference images should have level 0, got {level}"

    
