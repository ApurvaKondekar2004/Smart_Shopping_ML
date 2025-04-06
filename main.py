import pandas as pd
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from database import Base, engine
import gdown

Base.metadata.create_all(engine)



# Google Drive file link converted
url1 = 'https://drive.google.com/file/d/1Xkgs_Tvn56O7Q7FakAEvNGW4jbN3F3gO'
url2 = 'https://drive.google.com/file/d/1YTCLpb3z1lvkgS-ZZcM17pYJIG4uM_So'

# Download customer data
gdown.download(url1, 'customer_data.csv', quiet=False)
gdown.download(url2, 'product_data.csv', quiet=False)

# Load the downloaded data
customer_df = pd.read_csv('customer_data.csv')
product_df = pd.read_csv('product_data.csv')

customer_agent = CustomerAgent()
product_agent = ProductAgent()

recommendation_agent = RecommendationAgent()

customer_id = 'C1001'  # Example Customer ID

browsing_categories, recommendations = recommendation_agent.recommend_products(customer_id, customer_df, product_df)

print(f"\nBrowsing Categories of Customer {customer_id}: {browsing_categories}")

print("\nRecommended Products based on Popular Subcategory:")
for idx, rec in enumerate(recommendations, 1):
    print(f"{idx}. Product ID: {rec['Product_ID']} | Category: {rec['Category']} | Popular Subcategory: {rec['Subcategory']}")
