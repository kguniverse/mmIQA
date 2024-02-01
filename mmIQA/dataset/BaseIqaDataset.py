from mmengine.dataset import BaseDataset


class BaseIqaDataset(BaseDataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_distortion_types(self, idx):
        cls_idx = self.data_list[idx]['distortion_type']
        return self.metainfo['classes'][cls_idx]
    
    