# --- Logging ------
import logging
import os

logging.basicConfig(level=logging.WARNING)

# ---  Project Root ------
# Is is helpful to have a reference to the root directory of the project
PROJECT_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
