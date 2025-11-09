#!/usr/bin/python3
import sys

# Import the batch processing module
processing = __import__('1-batch_processing')

if __name__ == "__main__":
    # Process users in batches of 50 and print them
    try:
        processing.batch_processing(50)
    except BrokenPipeError:
        # Handle cases when output is piped and closed early
        sys.stderr.close()
