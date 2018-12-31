"""Dataset class template

This module provides a templete for users to implement custom datasets.
"""
from data.base_dataset import BaseDataset, get_transform
# from data.image_folder import make_dataset
# from PIL import Image


class TemplateDataset(BaseDataset):
    """A template dataset class for you to implement custom datasets.

       You can use '--dataset_mode template' to use this dataset.
       The class name should be consistent with both the filename and its dataset_mode option.
       The filename should be <dataset_mode>_dataset.py
       The class name should be <DATASET_MODE>Dataset.py
    """
    @staticmethod
    def modify_commandline_options(parser, is_train):
        """Add new dataset-specific options, and rewrite default values for existing options.

        Parameters:
            parser -- the option parser
            is_train -- if it is training phase or test phase. You can use this flag to add training-specific or test-specific options.

        Returns:
            the modified parser.
        """
        parser.add_argument('--new_dataset_option', type=float, default=1.0, help='new dataset option')
        parser.set_defaults(max_dataset_size=10, new_dataset_option=2.0)  # specify dataset-specific default values
        return parser

    def initialize(self, opt):
        """Initialize this dataset class

        Parameters:
            opt -- training/test options
        A few things can be done here.
        - save the options.
        - get image paths and meta information of the dataset.
        - define the image transformation.
        """
        # save the option and dataset root
        self.opt = opt
        self.root = opt.dataroot
        # get the image paths of your dataset;
        self.image_paths = []  # You can call <sorted(make_dataset(self.root))> to get all the image paths under the directory self.root
        # define the default transform function. You can use <base_dataset.get_transform>; You can also define your custom transform function
        self.transform = get_transform(opt)

    def __getitem__(self, index):
        """Return a data point and its metadata information.

        Parameters:
            index -- a random integer for data indexing

        Returns:
            a dicrtionary of data with their names. It ususally contains the data itself and its metadata information.

        Step 1: get a random image path: e.g., path = self.image_paths[index]
        Step 2: load your data from the disk: e.g., image = Image.open(path).convert('RGB').
        Step 2: convert your data to a PyTorch tensor. You can use function such as self.transform. e.g., data = self.transform(image)
        Step 3: return a data point as a dictionary.
        """
        path = 'temp'    # needs to be a string
        data_A = None    # needs to be a tensor
        data_B = None    # needs to be a tensor
        return {'data_A': data_A, 'data_B': data_B, 'path': path}

    def __len__(self):
        """Return the number of images"""
        return len(self.image_paths)

    def name(self):
        """Return the name of this dataset"""
        return 'TemplateDataset'