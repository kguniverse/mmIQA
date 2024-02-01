from mmengine.dataset import BaseDataset, force_full_init

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
        'classes': ['refimgs', 'jp2k', 'jpeg', 'wn', 'gblur', 'fastfading'],
        'info': {
            'fastfading': {
                "description": "Fast Fading Rayleigh",
                "nums": 174
            },
            'gblur': {
                "description": "Gaussian blur",
                "nums": 174
            },
            'jp2k': {
                "description": "JPEG2000",
                "nums": 227
            },
            'jpeg': {
                "description": "JPEG",
                "nums": 233
            },
            'wn': {
                "description": "White noise in the RGB components",
                "nums": 174
            },
        }
    }
    def __init__(self, *args, **kwargs):
        super(LIVEDataset, self).__init__(*args, **kwargs)
        self.check_labels()
    
    @force_full_init
    def check_labels(self):
        for img_path, tp, level in self.data_list:
            if self._metainfo['classes'][tp] == 'refimgs':
                assert level == 0, f"Reference images should have level 0, got {level}"

    
