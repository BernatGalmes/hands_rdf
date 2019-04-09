import os
import numpy as np
import json
import math


class Config:
    """
        Dades de configuració del sistema d'aprenentatge
    """

    __INSTANCE = None

    class __Data:

        def __init__(self):

            # Software version
            self.VERSION = 1

            self.DATASET = "RDF_Train"
            self.m = 300000

            self.OFFSETS_USE_ALL = True
            self.OFFSETS_DISTRIBUTION = "UNIFORM"
            self.N_FEATURES = 1000
            self.N_OFFSETS = 2

            self.ROUND_VALUES = -2

            self.OFFSETS_SEED = 10

            self.DATA_IMS_IN_FILE = 2000
            self.DATA_PIXELS_CLASS = 500

            # Threshold of depth images, maximum depth to consider in images.
            self.TH_DEPTH = 4000

            # Value to fill the background
            self.BG_DEPTH_VALUE = int(np.iinfo(np.uint16).max / 2)

            # Random forest parameters
            self.rf_inc_trees_fit = 15
            self.rf_max_depth = 30
            self.rf_min_samples_leaf = 1

            self.scale_data = False

            self.FOLDER_DATA = os.path.realpath(os.path.dirname(__file__) + '/../../../data')

            self.CLASS_TAG = "isHand"

        @property
        def DATA_COLUMNS(self):
            """
            Llista de les columnes de les dades a utilitzar de cada regió
            :return:
            """
            return ["feat_" + str(i) for i in range(0, self.N_FEATURES)]

        @property
        def PATH_DATASET(self):
            return "/home/bernat/datasets/" + self.DATASET + "/"

        @property
        def FOLDER_RAW_DATA(self):

            return self.FOLDER_DATA + "/rawData/v" + str(self.VERSION) + "_" + self.OFFSETS_DISTRIBUTION + "_" + str(
                self.N_FEATURES) + "_" + str(self.OFFSET_MAX) + "/" + self.DATASET + "/"

        @property
        def FOLDER_RAW(self):
            return self.FOLDER_DATA + "/rawData/v" + str(
                self.VERSION) + "_" + self.OFFSETS_DISTRIBUTION + "_" + str(
                self.N_FEATURES) + "_" + str(self.OFFSET_MAX) + "/"

        @property
        def FOLDER_TRAIN(self):
            return self.FOLDER_RAW_DATA + "train/"

        @property
        def FOLDER_TEST(self):
            return self.FOLDER_RAW_DATA + "test/"

        @property
        def FOLDER_RESULTS(self):
            return self.FOLDER_DATA + "/results/v" + str(self.VERSION) + "/"

        @property
        def FOLDER_FRAMES(self):
            return self.FOLDER_DATA + "/frames/v" + str(self.VERSION) + "/"

        @property
        def FOLDER_CLFS(self):
            return self.FOLDER_DATA + "/Classifiers/v" + str(self.VERSION) + "/" \
                   + self.OFFSETS_DISTRIBUTION + "_" + str(self.N_FEATURES) + "/"

        @property
        def FOLDER_OFFSETS(self):
            return self.FOLDER_DATA + "/offsets/"

        @property
        def FOLDER_OFFSETS(self):
            return self.FOLDER_DATA + "/offsets/"

        @property
        def FILE_DATA(self):
            return self.FOLDER_TRAIN + "/data_*"

        @property
        def PATH_CLF_FILE(self):
            return self.FOLDER_RAW_DATA + '/clf' + str(self.VERSION) + '_' + str(self.OFFSET_MAX) + '.sav'

        @property
        def FILE_TEST_DATA(self):
            return self.FOLDER_TEST + "/data_*"

        @property
        def FILE_OFFSETS(self):
            return self.FOLDER_OFFSETS + "offsets_v" + str(self.VERSION) + ".xlsx"

        @property
        def OFFSET_MAX(self):
            return int(0.4 * self.m)

        @property
        def MIN_DEPTH(self):
            return 0   # lower depth than this value are marked with max depth

        def save_json(self, file):
            with open(file, 'w') as fp:
                json.dump(self.__dict__, fp, sort_keys=True, indent=4)

        def save_txt(self, path):
            file = path + "config.info"
            with open(file, 'w') as fp:
                fp.write(self.__str__())

        def __str__(self):
            txt = "----------" \
                  "\nPROGRAM CONFIGURATION:" \
                  "\n----------"
            for key in self.__dict__:
                txt += key + ": " + str(self.__dict__[key]) + "\n"

            return txt

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls.__Data()
        return cls.__INSTANCE


config = Config()
