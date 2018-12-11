import os
import glob
import random

def setup_working_directories(config_vars):

    ## Expected raw data directories:
    config_vars["raw_data_dir"] = os.path.join(config_vars["root_directory"], '0_raw_data/')
    config_vars["corrected_data_dir"] = os.path.join(config_vars["root_directory"], '1_corrected/')

    config_vars["focused_data_dir"] = os.path.join(config_vars["root_directory"], '3_focused/')
    config_vars["segmented_data_dir"] = os.path.join(config_vars["root_directory"], '4_segmented/')
    config_vars["qc_filtered"] = os.path.join(config_vars["root_directory"], '5_qc_filtered/')

    config_vars["annotations_dir"] = os.path.join(config_vars["root_directory"], '6_annotations/')
    config_vars["reports_dir"] = os.path.join(config_vars["root_directory"], '7_reports/')

    return config_vars
