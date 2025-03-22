import logging
import os
from datetime import datetime

# Define log directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)  # Ensure directory exists

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)





'''
This script:

1. Sets up a logs directory if it doesn’t exist.

2. Creates a unique log file based on the current timestamp.

3. Configures logging settings to store logs with timestamps, line numbers, severity levels, etc.

4. Writes a test log message to confirm logging works.'''