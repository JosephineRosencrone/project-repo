from master_thesis_python_repo.live.screen_capture import Screen_Capture


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m master_thesis_python_repo` and `$ master_thesis_python_repo `.

    This is the program's entry point.
    """

    Screen_Capture(name="test", screen_width=800, screen_height=800).run()
