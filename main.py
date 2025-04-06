from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from database import Base, engine

# Create DB Tables
Base.metadata.create_all(engine)

# Initialize Agents
customer_agent = CustomerAgent()
product_agent = ProductAgent()
recommendation_agent = RecommendationAgent()

print("Setup Done! Agents are Ready to be used.")
