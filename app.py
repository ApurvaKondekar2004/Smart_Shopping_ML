import streamlit as st
import pandas as pd
from agents.recommendation_agent import RecommendationAgent

# Load Data
customer_df = pd.read_csv('data/customer_data_collection.csv')
product_df = pd.read_csv('data/product_recommendation_data.csv')

recommendation_agent = RecommendationAgent()

st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")

st.title("🛍️ Smart Shopping Recommendation System")

customer_id = st.text_input("Enter Customer ID (Example: C1001)")

if st.button("Recommend Products"):
    if customer_id:
        categories, recommendations = recommendation_agent.recommend_products(customer_id, customer_df, product_df)

        if not categories:
            st.error("Customer ID not found!")
        else:
            st.success(f"Browsing History Categories of {customer_id}")
            st.write(list(set(categories)))  # Unique categories only

            st.subheader("Top 5 Recommended Products:")
            if recommendations:
                for idx, rec in enumerate(recommendations[:5], 1):
                    st.markdown(f"""
                    **{idx}. Product ID:** {rec['Product_ID']}  
                    **Category:** {rec['Category']}  
                    **Subcategory:** {rec['Subcategory']}  
                    """)

            else:
                st.warning("No Recommendations found for this customer.")

else:
    st.info("Enter a Customer ID and click Recommend Products")

