!pip install kaggle

import os
os.environ['KAGGLE_USERNAME'] = 'aaronfletcher1'
os.environ['KAGGLE_KEY'] = '4beca6d26c2dc02017dddcffd5e0d64e

!kaggle datasets download -d dataset_name
