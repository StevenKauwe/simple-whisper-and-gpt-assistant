# Voice-Activated Assistant

## Overview

The voice-activated assistant is a Python application that listens for specific audio cues and performs actions based on those cues.
It uses a combination of audio recording, transcription, and action handling to provide a voice-activated interface for various tasks.

## Features

- Wake phrase detection to start listening for commands.
- Transcription of audio to text for command recognition.
- Customizable actions that can be triggered by voice commands.
- Integration with external services for advanced functionalities (e.g., GPT, transcription services).

## Requirements

- Python 3.12+
- Rye for python package management

```bash
curl -sSf https://rye-up.com/get | bash
```

## Setup

1. [Install Rye](https://rye-up.com/guide/installation/)
2. Initialize and install dependencies via `rye sync --no-lock`.
If you want to update the lock files, and therefor the dependencies, run `rye sync` instead.
3. Ensure you have the necessary credentials and settings for any external services used by the actions (e.g., GPT, transcription services).
For now the app assumes you have a valid OpenAI API key set as an environment variable.

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

## Usage

To start the voice-activated assistant, run the following command in your terminal:

```bash
rye sync --no-lock
rye run voice-assistant

# I also included a shorter version of the same command (see .toml to customize)
ryo run va
```

Once running, the application will listen for the wake phrase and then await further voice commands to trigger registered actions.
You may need to adjust settings to allow the application to access your microphone.
On a macOS system, you can do this by going to `System Preferences` -> `Security & Privacy` -> `Privacy` -> `Microphone` and enabling access for the terminal application you are using.

## Actions

The application supports registering custom actions.
Each action is associated with a specific phrase that, when detected in the transcription, will trigger the action's `perform` method.

The following actions are included by default:

- `TranscribeAndPasteTextAction`: Transcribes spoken text and pastes it into a text field.
- `TalkToGPTAction`: Sends the transcribed text to GPT for processing and handles the response.
- `UpdateSettingsAction`: Updates settings based on voice commands.

You can register additional actions by extending the `Action` class and adding them to the `ActionController`.

## Customization

To customize actions or add new ones, modify the `VoiceControlledRecorder.register_actions` method.
Create instances of your action classes and register them with the `ActionController`.

## Logging

The application uses `loguru` for logging.
You can adjust the logging level by modifying the `logger_init` function call in the script.

## Graceful Shutdown

The application handles `SIGTERM` and `SIGINT` signals to ensure a graceful shutdown when the process is terminated.

## License

Please ensure you comply with the licenses of all components and dependencies used within this application.
