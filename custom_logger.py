import inspect
from datetime import datetime as dt

log_level = 0  # Set the minimum log level to display

def log(level, *args):
    """Logs messages with appropriate level, color coding, timestamp, and function name."""
    level_config = {
        5: ('\033[0;101m', '🔳'),   # Red Background
        4: ('\033[1;91m', '🔴'),    # High Intensity Bold Red Text
        3: ('\033[93m', '☢️'),      # Yellow Text
        2: ('\033[92m', '✅'),      # Green Text
        1: ('\033[0m', 'ℹ️')        # White Text
    }
    # Default to 'DEBUG' if the level is out of range
    color, level_name = level_config.get(level, ('\033[0;104m', '🔲'))  # High Intensity Blue Background
    caller_name = inspect.stack()[1].function if inspect.stack()[1].function else 'MAIN'

    # Join the args into a single message string
    message = ' '.join(map(str, args))

    if level >= log_level:
        print(f"{color}{dt.now()} {level_name:<1} <{caller_name}> {message}\033[0m")


def sample_function():
    log(0, "Debug Log.")
    log(1, "Info Log.")
    log(2, "Success Log.")
    log(3, "Warning Log.")
    log(4, "Error Log.")
    log(5, "Critical Log.")

sample_function()  # Example usage within a function