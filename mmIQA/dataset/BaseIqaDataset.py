from mmengine.dataset import BaseDataset


class BaseIqaDataset(BaseDataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    