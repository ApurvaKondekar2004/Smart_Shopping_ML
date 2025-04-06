import pandas as pd

class RecommendationAgent:
    def __init__(self):
        pass

    def recommend_products(self, customer_id, customer_df, product_df):
        customer_row = customer_df[customer_df['Customer_ID'] == customer_id]

        if customer_row.empty:
            return [], []

        browsing_history = customer_row['Browsing_History'].values[0]
        browsing_categories = [cat.strip().replace("'", "") for cat in browsing_history.strip("[]").split(',')]

        print(f"Browsing History Categories of Customer {customer_id}: {browsing_categories}")

        recommendations = []

        for category in browsing_categories:
            # All customers browsing that category
            all_browsing = customer_df['Browsing_History'].tolist()

            subcategory_counter = {}

            for history in all_browsing:
                cats = [cat.strip().replace("'", "") for cat in history.strip("[]").split(',')]
                if category in cats:
                    # Get all subcategories in this category from product_df
                    subcategories = product_df[product_df['Category'] == category]['Subcategory'].tolist()
                    for sub in subcategories:
                        subcategory_counter[sub] = subcategory_counter.get(sub, 0) + 1

            if subcategory_counter:
                # Most common subcategory
                popular_subcategory = max(subcategory_counter, key=subcategory_counter.get)

                product = product_df[
                    (product_df['Category'] == category) &
                    (product_df['Subcategory'] == popular_subcategory)
                ].head(1)

                if not product.empty:
                    recommendations.append({
                        'Product_ID': product.iloc[0]['Product_ID'],
                        'Category': category,
                        'Subcategory': popular_subcategory
                    })

        return browsing_categories, recommendations[:5]  # Only Top 5

