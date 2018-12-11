import os
import hcs_utils.refactoring

config_vars = {}

# ************ 01 ************ #
# ****** PREPROCESSING ******* #
# **************************** #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 01.01 INPUT DIRECTORIES AND FILES

config_vars["root_directory"] = 'f:/Projects/ACC_training'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 01.02 INPUT NAME REGEXP

config_vars["input_regexp"] = 'r{:02d}c{:02d}f{:02d}p*-ch{:d}*'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 01.03 OUTPUT NAME REGEXP

config_vars["output_regexp"] = '{:s}_w{:c}{:02d}_s{:02d}'

# ************ 02 ************ #
# ** FLAT FIELD CORRECTION *** #
# **************************** #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 02.01 F

config_vars["ffc_method"] = "CIDRE"

# ************ 03 ************ #
# ***** FOCUS DETECTION ****** #
# **************************** #

config_vars["focus_detection_method"] = "best_plane"

# ************ 04 ************ #
# ***** QUALITY CONTROL ****** #
# **************************** #

config_vars["qc_fov_focus"] = False
config_vars["qc_fov_saturation"] = False
config_vars["qc_segmentation"] = False

# ************ 05 ************ #
# ******* SEGMENTATION ******* #
# **************************** #

config_vars = hcs_utils.refactoring.setup_working_directories(config_vars)