#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from linkedincontentagent.crew import Linkedincontentagent

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
        "thought": "i'm bad and lazy at posting in linkedin so i build this ai agent to make that easier for me using crew ai and openai api.",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Linkedincontentagent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "thought": "Sharing insights from my latest project in AI.",
        "current_year": str(datetime.now().year)
    }
    try:
        Linkedincontentagent().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Linkedincontentagent().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "thought": "Excited to announce a new feature I just released!",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Linkedincontentagent().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
