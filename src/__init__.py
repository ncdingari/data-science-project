# src/__init__.py
# This file can be used to handle imports across the src package.
# For example, it can make it easier to import key functions from submodules.

from .data.make_dataset import save_raw_data, save_processed_data
from .features.build_features import add_feature_x
from .models.predict_model import train_model, predict
from .visualization.visualize import plot_salary_by_department

__all__ = [
    "save_raw_data",
    "save_processed_data",
    "add_feature_x",
    "train_model",
    "predict",
    "plot_salary_by_department"
]
