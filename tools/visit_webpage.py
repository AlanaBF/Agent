from typing import Any, Optional
from smolagents.tools import Tool
import requests
import markdownify
import smolagents
import re

class VisitWebpageTool(Tool):
    name = "visit_webpage"
    description = "Visits a webpage at the given url and reads its content as a markdown string. Use this to browse webpages."
    inputs = {'url': {'type': 'string', 'description': 'The url of the webpage to visit.'}}
    output_type = "string"
    def truncate_input(input_text, max_tokens):
        # Calculate the number of tokens to truncate
        num_tokens_to_truncate = len(input_text.split()) - max_tokens
        
        # Truncate the input text
        truncated_input_text = ' '.join(input_text.split()[:-num_tokens_to_truncate])
        
        return truncated_input_text
    def forward(self, url: str) -> str:
        try:
            from requests.exceptions import RequestException
            from smolagents.utils import truncate_content
        except ImportError as e:
            raise ImportError(
                "You must install packages `markdownify` and `requests` to run this tool: for instance run `pip install markdownify requests`."
            ) from e
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Convert the HTML content to Markdown
            markdown_content = markdownify.markdownify(response.text).strip()
            # Remove multiple line breaks
            markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
            truncated_markdown_content = truncate_content(markdown_content)
            return truncated_markdown_content[:10000]

        except requests.exceptions.Timeout:
            return "The request timed out. Please try again later or check the URL."
        except RequestException as e:
            return f"Error fetching the webpage: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def __init__(self, *args, **kwargs):
        self.is_initialized = False