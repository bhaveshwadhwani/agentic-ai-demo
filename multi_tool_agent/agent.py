import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from typing import Optional

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


def google_search(query: str, num_results: Optional[int] = 5) -> dict:
    """Performs a Google Search and returns the results.

    Args:
        query (str): The search query.
        num_results (Optional[int]): The number of search results to return. Defaults to 5.

    Returns:
        dict: status and result or error msg.
    """
    try:
        from googlesearch import search
        results = list(search(query, num_results=num_results))
        return {"status": "success", "results": results}
    except ImportError:
        return {
            "status": "error",
            "error_message": (
                "The 'googlesearch-python' package is not installed. Please install it to use this tool."
            ),
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


root_agent = Agent(
    name="demo_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time, weather in a city, and perform google searches."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    )
)

root_agent.tools = [get_weather, get_current_time, google_search]
