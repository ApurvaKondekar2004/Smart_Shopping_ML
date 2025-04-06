import pandas as pd
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from database import Base, engine

Base.metadata.create_all(engine)

url1='https://drive.google.com/uc?id=1Xkgs_Tvn56O7Q7FakAEvNGW4jbN3F3gO'
url='https://drive.google.com/uc?id=1YTCLpb3z1lvkgS-ZZcM17pYJIG4uM_So'
customer_df = pd.read_csv(url1)
product_df = pd.read_csv(url)

customer_agent = CustomerAgent()
product_agent = ProductAgent()

recommendation_agent = RecommendationAgent()

customer_id = 'C1001'  # Example Customer ID

browsing_categories, recommendations = recommendation_agent.recommend_products(customer_id, customer_df, product_df)

print(f"\nBrowsing Categories of Customer {customer_id}: {browsing_categories}")

print("\nRecommended Products based on Popular Subcategory:")
for idx, rec in enumerate(recommendations, 1):
    print(f"{idx}. Product ID: {rec['Product_ID']} | Category: {rec['Category']} | Popular Subcategory: {rec['Subcategory']}")
