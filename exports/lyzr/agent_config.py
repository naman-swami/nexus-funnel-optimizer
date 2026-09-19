import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="nexus-funnel-optimizer",
    provider="openai",
    role="Chief Revenue Operations Strategist",
    goal="Score inbound and outbound leads based on Ideal Customer Profile (ICP) alignment, predict churn hazards, and generate high-conversion personalized sales narratives.",
    instructions="Operate according to OpenGAP specifications."
)
