# Grok Chat Client

## Overview
A cross-platform chat client for interacting with the Grok API (from xAI). Built with React Native, it supports real-time conversations, tool usage (function calling for external tools like searches or code execution), and local message history. Designed for extensibility, allowing easy addition of new tools and features.

## Features
- **Chat Interface**: Send and receive messages with Grok models (e.g., Grok-4.20).
- **Tool Usage Support**: Integrate and execute external tools (e.g., code execution, searches) during conversations.
- **Cross-Platform**: Runs on iOS, Android, web (via React Native Web), and desktop (Windows/macOS).
- **Local Persistence**: Store chat history and settings securely.
- **Extensibility**: Modular tool registry for adding custom plugins.
- **Security**: Encrypted API key storage.

## Technology Stack
- **Frontend**: React Native (TypeScript) with Expo.
- **State Management**: Redux Toolkit.
- **API Integration**: Axios for Grok API calls.
- **Persistence**: AsyncStorage/SQLite.
- **UI**: react-native-gifted-chat.
- **Other**: Jest for testing, react-native-keychain for security.

## Installation
1. Prerequisites: Node.js, Expo CLI (`npm install -g @expo/cli`).
2. Clone the repo: `git clone <repo-url>`.
3. Install dependencies: `npm install`.
4. Start the app: `expo start`.

## Usage
1. Obtain an API key from [xAI Console](https://console.x.ai).
2. Launch the app and enter your API key in settings.
3. Start chatting! Tools will be invoked automatically when Grok requests them.

## Development
- **Project Setup**: See `plan.md` for the high-level development plan.
- **Adding Tools**: Edit the tool registry in `src/tools/` and update API service logic.
- **Testing**: Run `npm test`.
- **Build**: Use Expo for platform-specific builds.

## Contributing
Contributions welcome! Please open an issue or PR for features/bugs. Keep the README updated as we develop.

## License
TBD (e.g., MIT).