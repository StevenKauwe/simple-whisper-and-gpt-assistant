from textwrap import dedent


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.ACTIVATION_KEYS = "ctrl+alt+space"
        self.EXIT_KEYS = "ctrl+alt+s"
        # self.MODEL_ID = "gpt-4-1106-preview"
        self.MODEL_ID = "gpt-3.5-turbo-1106"
        self.AUDIO_FILE_DIR = "outputs"
        self.HOLD_TO_TALK = False
        self.TIMEOUT = 60 * 60  # 1 hour

        self.USE_STT = True
        self.USE_TTS = False
        self.LOCAL = True
        self.LANGUAGE = "en"

        self.TRANSCRIPTION_PREPROMPT = dedent(
            """\
            # Trascript Converter

            This is the output of an imperfect speech-to-text engine.
            Please convert this text into a more readable format.

            ## python code

            You should convert the text into production level, enterprise grade, python code.
            This means converting the rough idea from the text into a more polished, production ready, python code.

            As a part of this, include function definitions, class definitions, and other python code.
            You should also have docstrings if usage is complex (otherwise we prefer simple) and, if necessary to explain WHY something is done, comments.
            We use numpy doc style docstrings. Black and flake8 are used for formatting and linting.

            ## general

            You should fix any spelling mistakes, grammar mistakes, and other mistakes in the text.
            You should also seek to fix any mistakes from the speech-to-text engine itself.
            This includes fixing any mistakes in the punctuation, capitalization, and other aspects of the text.
            You might need to replace words based on context, or add words to make the text more readable.
            You should also add whitespace to make the text more readable (e.g. add newlines, spaces, etc.) since the speech-to-text engine does not add any whitespace.
            """
        )
        self.PRINT_TO_TERMINAL = True

    def update(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise ValueError(f"Invalid config key: {key}")


config = Config()
