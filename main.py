import pandas as pd
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from database import Base, engine

Base.metadata.create_all(engine)

customer_df = pd.read_csv('data/customer_data_collection.csv')
product_df = pd.read_csv('data/product_recommendation_data.csv')

customer_agent = CustomerAgent()
product_agent = ProductAgent()

recommendation_agent = RecommendationAgent()

customer_id = 'C1001'  # Example Customer ID

browsing_categories, recommendations = recommendation_agent.recommend_products(customer_id, customer_df, product_df)

print(f"\nBrowsing Categories of Customer {customer_id}: {browsing_categories}")

print("\nRecommended Products based on Popular Subcategory:")
for idx, rec in enumerate(recommendations, 1):
    print(f"{idx}. Product ID: {rec['Product_ID']} | Category: {rec['Category']} | Popular Subcategory: {rec['Subcategory']}")
