#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from custom_tool.crew import QnATool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'subject': 'Story',
        'grade': '2',
        'lesson_url': 'https://api.bookbotkids.workers.dev/books/f60ac1f9-e513-433f-a640-6cbdf028cd98/Magnet%20Magic!.pdf',
    }
    
    try:
        QnATool().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


