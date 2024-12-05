#!/usr/bin/env python
import sys
import warnings

from my_mas.crew import MyMas

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with expanded input variables.
    """
    inputs = {
        'product_category': 'Smartphones',  # Example default value
        'target_brands': 'Apple, Samsung, Google',  # Example default brands
        'needs_features': 'High camera quality, 5G support, Battery life over 4000 mAh'  # Example default features
    }
    MyMas().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'product_category': 'Smartphones',  # Example default value
        'target_brands': 'Apple, Samsung, Google',  # Example default brands
        'needs_features': 'High camera quality, 5G support, Battery life over 4000 mAh'  # Example default features
    }
    try:
        MyMas().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMas().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'product_category': 'Smartphones',  # Example default value
        'target_brands': 'Apple, Samsung, Google',  # Example default brands
        'needs_features': 'High camera quality, 5G support, Battery life over 4000 mAh'  # Example default features
    }
    try:
        MyMas().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
