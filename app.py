import streamlit as st
import pandas as pd
from agents.recommendation_agent import RecommendationAgent

st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")

st.title("🛍️ Smart Shopping Recommendation System")

# Upload CSV files
uploaded_customer_file = st.file_uploader("Upload Customer Data CSV", type=["csv"])
uploaded_product_file = st.file_uploader("Upload Product Data CSV", type=["csv"])

if uploaded_customer_file and uploaded_product_file:
    customer_df = pd.read_csv(uploaded_customer_file, on_bad_lines='skip')
    product_df = pd.read_csv(uploaded_product_file, on_bad_lines='skip')

    customer_df.columns = customer_df.columns.str.strip()
    product_df.columns = product_df.columns.str.strip()

    st.write("### Customer Data Sample")
    st.write(customer_df.head())

    st.write("### Product Data Sample")
    st.write(product_df.head())

    customer_id = st.text_input("Enter Customer ID (Example: C1001)")

    if st.button("Recommend Products"):
        if customer_id:
            recommendation_agent = RecommendationAgent()

            categories, recommendations = recommendation_agent.recommend_products(customer_id, customer_df, product_df)

            if not categories:
                st.error("Customer ID not found!")
            else:
                st.success(f"Browsing History Categories of {customer_id}")
                st.write(list(set(categories)))  # Unique categories

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
    st.info("Upload both Customer & Product CSV files to proceed.")
