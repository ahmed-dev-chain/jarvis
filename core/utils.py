import os
import sys
from contextlib import contextmanager

@contextmanager
def silence_stderr():
    """
    Context manager to suppress stderr at the OS level.
    This works for suppressing C/C++ library outputs (like ALSA/JACK).
    """
    new_stderr = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(sys.stderr.fileno())
    
    try:
        os.dup2(new_stderr, sys.stderr.fileno())
        yield
    finally:
        os.dup2(old_stderr, sys.stderr.fileno())
        os.close(new_stderr)
        os.close(old_stderr)
