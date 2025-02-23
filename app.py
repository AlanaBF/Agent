from smolagents import CodeAgent, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool
from tools.visit_webpage import VisitWebpageTool
from tools.web_search import DuckDuckGoSearchTool
import os
from dotenv import load_dotenv
from Gradio_UI import GradioUI

HF_TOKEN = os.environ["HF_TOKEN"]
weather_api_key = os.environ["WEATHER_API_KEY"]
translator_api_key = os.environ["TRANSLATOR_API_KEY"]

@tool
def get_weather(city: str)-> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that retrieves the weather for a given city.

    Args:
        city: The name of the city for which to retrieve the weather.

    Returns:
        A dictionary containing the weather data.
    """
    try: 
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        return response.json()
     
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_translation(text: str, to_language: str, from_language: str) -> str:
    """
    Translate text from one language to another using the Google Translate API.

    Args:
        text: 
            The text to be translated.
        to_language: 
            The language to translate the text into.
        from_language: 
            The language of the original text.

    Returns:
        str: The translated text in JSON format.
    """
    try:
        url = f"https://free-google-translator.p.rapidapi.com/external-api/free-google-translator?from={from_language}&to={to_language}&query={text}"
        response = requests.post(url, headers={"x-rapidapi-key": translator_api_key})
        return response.json()
    except Exception as e:
        return f"Error: {str(e)}"  
        
        
        
@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
agent = CodeAgent(
    model=model,
    tools=[final_answer, DuckDuckGoSearchTool(), VisitWebpageTool(), image_generation_tool, get_weather, get_translation, get_current_time_in_timezone], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()