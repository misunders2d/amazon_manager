import pathlib
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset

from app.tools.google_search import google_search_agent_tool
from app.tools.web import web_fetch
from app.tools.amazon.keepa import keepa_get_product_data, keepa_search, keepa_get_best_sellers

# Load the Amazon Manager skill
base_dir = pathlib.Path(__file__).parent.parent.parent / "skills"
amazon_manager_skill = load_skill_from_dir(base_dir / "amazon-manager-skill")

amazon_manager_agent = Agent(
    name="AmazonManagerAgent",
    model=Gemini(model="gemini-2.0-flash"),
    description="Specialized agent for managing Amazon listings, analyzing product data, and tracking competitors.",
    instruction=(
        "You are the Amazon Manager Agent, an expert in Amazon marketplace dynamics and Keepa data analysis. "
        "Your primary goal is to help the user manage their listings and identify market opportunities.\n\n"
        "1. **Keepa Analysis**: Use the Keepa tools to fetch deep historical data for ASINs. "
        "Analyze pricing trends, sales rank velocity, and identify promotions like Lightning Deals or Prime Exclusive discounts.\n"
        "2. **Market Research**: Use `keepa_search` to find products and `keepa_get_best_sellers` to analyze category trends.\n"
        "3. **Competitor Tracking**: Monitor Buy Box ownership and competitor stock levels.\n"
        "4. **Listing Optimization**: Use Keepa metadata (title, bullets, description) and external research via Google Search and Web Fetch to propose improvements to product listings.\n\n"
        "When performing an analysis, always refer to the instructions in the `amazon-manager-skill` for best practices on interpreting data averages and sales velocity."
    ),
    tools=[
        skill_toolset.SkillToolset(skills=[amazon_manager_skill]),
        keepa_get_product_data,
        keepa_search,
        keepa_get_best_sellers,
        google_search_agent_tool,
        web_fetch,
    ]
)
