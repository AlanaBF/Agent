# Agent README

## Introduction

This is part of my learning from the Hugging Face Agents Course, which I have adapted and added to with new tools.

This agent is a code-based conversational AI that uses the SmolAgents framework to provide a range of tools and functionalities. The agent is designed to assist with various tasks, including weather forecasting, language translation, and time zone conversions.

## Features

- Weather forecasting: The agent can retrieve the current weather for a given city using the OpenWeatherMap API.
- Language translation: The agent can translate text from one language to another using `https://rapidapi.com/joshimuddin8212/api/free-google-translator` from RapidAPI.
- Time zone conversions: The agent can fetch the current local time in a specified time zone.
- Web search: The agent can perform web searches using the DuckDuckGo search engine.
- Webpage visits: The agent can visit webpages and retrieve information.
- Image generation prompts: The agent provides a clearer prompt for generating the image, and then generates it.
- Final answer: The agent can provide a final answer to a question or prompt.

## Requirements

The following dependencies are required to run the agent:

- `markdownify`: Used for formatting text outputs.
- `smolagents`: The core framework for building conversational AI agents.
- `requests`: Used for making API calls to external services.
- `duckduckgo_search`: Used for performing web searches.
- `pandas`: Used for data manipulation and analysis.
- `python-dotenv`: Used for loading environment variables from a `.env` file.
- `smolagents[gradio]`: Used for building the Gradio UI.

## Installation

- Install the required dependencies using pip: `pip install -r requirements.txt`
- Create a `.env` file in the root directory of the project and add your API keys for `Hugging Face`, `OpenWeatherMap`, and `Google Translate`.

The format should be:

- `HF_TOKEN=your_huggingface_token_here`
- `WEATHER_API_KEY=your_api_key_here`
- `TRANSLATOR_API_KEY=your_api_key_here`

## Usage

- Run the agent using `python main.py`.
- Interact with the agent using the Gradio UI. You can input text prompts and receive text outputs. You can also use the UI to select tools and provide input parameters.

### Weather Forecasting

- Get the current weather for a given city:
- Input: "What is the weather like in Birmingham?"
- Output: "The weather in Birmingham is broken clouds with a temperature of -1. 78°C, feels like -1. 78°C, humidity at 88%, and wind speed of 0 m/s."

### Language Translation

- Translate text from one language to another:
- Input: "Translate from English to French: This agent is a code-based conversational AI that uses the SmolAgents framework to provide a range of tools and functionalities. The agent is designed to assist with various tasks, including weather forecasting, language translation, and time zone conversions."
- Output: "Cet agent est un IA conversationnel basé sur le code qui utilise le framework SmolAgents pour fournir une gamme d'outils et de fonctionnalités. L'agent est conçu pour assister à diverses tâches, y compris la prévision météorologique, la traduction de langues et les conversions de fuseaux horaires."

### Web Search

- Perform a web search using the DuckDuckGo search engine:
- Input: "Search for information on Alana Barrett-Frew"
- Output: "Alana Barrett-Frew is a proactive junior Full Stack Developer and AI Engineer at Version 1. She specializes in AI Virtual Assistants using Microsoft Azure, Python, React, and TypeScript. Alana is certified in AZ-900, AI-900, and AI-102. She is passionate about leveraging technology to solve meaningful challenges and has transitioned from a two-decade career as an educator and leader into the tech industry."

### Webpage Visits

- Visit a webpage and retrieve information:
- Input: "Visit the Wikipedia page on machine learning"
- Output: "Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions. [1] Within a subdiscipline in machine learning, advances in the field of deep learning have allowed neural networks, a class of statistical algorithms ..."

## Image Generation Prompts

- Provide prompts for generating images:
- Input: "Generate an image of a 3 dogs, a jack russell, a springer spaniel and a sausage dog"
- Output: "A high-res, photorealistic image of a Jack Russell, a Springer Spaniel, and a Sausage Dog, sitting together in a grassy field, under a clear blue sky."

![Image Ceated](./assets/example.png)

## Tools

The agent uses the following tools:

- `get_weather`: Retrieves the current weather for a given city.
- `get_translation`: Translates text from one language to another.
- `get_current_time_in_timezone`: Fetches the current local time in a specified time zone.
- `DuckDuckGoSearchTool`: Performs web searches using the DuckDuckGo search engine.
- `VisitWebpageTool`: Visits webpages and retrieves information.
- `image_generation_tool`: Provides prompts for generating images and creates the image.
- `FinalAnswerTool`: Provides a final answer to a question or prompt.

## Model

The agent uses the `Qwen/Qwen2.5-Coder-32B-Instruct` model from the Hugging Face Model Hub.

## Prompt Templates

The agent uses prompt templates loaded from the `prompts.yaml` file.
