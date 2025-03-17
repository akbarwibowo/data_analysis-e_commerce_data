import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')

st.title('E-Commerce Dataset Analysis Dashboard')

# first question visualization
first_df = pd.read_csv('main_data/first_quest.csv')

st.header('1. Numbers of Orders per Hour of Day')
st.write('This visualization shows the number orders per hour in a day.')

first_figure = plt.figure(figsize=(20, 8))
sns.barplot(x=first_df['order_purchase_hour'], y=first_df['purchase_amount'], palette='viridis')

# Highlight the max bar
max_value_idx = first_df['purchase_amount'].argmax()
plt.bar(max_value_idx, first_df.loc[max_value_idx], color='red', alpha=0.5)

plt.title('Number of Orders per Hour of Day')
plt.xlabel('Hour of Day (24-hour format)')
plt.ylabel('Number of Orders')
plt.grid(True, alpha=0.5)

st.pyplot(first_figure, use_container_width=False)

st.markdown(f'The red bar represents the hour with the highest number of orders. Which its peak order at 16:00 with {first_df.loc[max_value_idx, "purchase_amount"]} orders.')


# second question visualization
st.markdown('---')
second_df = pd.read_csv('main_data/second_quest.csv')

st.header("2. State's Customer Percentage Change in Last 6 Months")
st.write('This visualization shows the percentage change of customers in each state in the last 6 months.')

initial_orders = second_df.groupby('customer_state')['order_id'].head(4).groupby(second_df['customer_state']).sum()
final_orders = second_df.groupby('customer_state')['order_id'].tail(4).groupby(second_df['customer_state']).sum()

# Calculate percentage change
percent_change = ((final_orders - initial_orders) / initial_orders * 100).sort_values(ascending=False)

# Create a bar plot
second_figure = plt.figure(figsize=(15, 8))
colors = ['blue' if x > 0 else 'red' for x in percent_change]
plt.bar(percent_change.index, percent_change.values, color=colors)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.title('Percentage Change in Customer Orders by State (Last 6 Months)')
plt.xlabel('State')
plt.ylabel('Percentage Change (%)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Add value labels on top of each bar
for i, v in enumerate(percent_change):
    plt.text(i, v + (5 if v > 0 else -5), 
            f'{v:.1f}%', 
            ha='center', 
            va='bottom' if v > 0 else 'top')

plt.tight_layout()

st.pyplot(second_figure)
st.markdown('The blue bars represent the states with positive percentage change in customer orders, while the red bars represent the states with negative percentage change in customer orders.')


# third question visualization
st.markdown('---')
third_df = pd.read_csv('main_data/third_quest.csv')

st.header('3. Product Sales Amount in Last Quartal')
st.write('This visualization shows the top 10 sales amount of each product category in the last quartal.')

st.bar_chart(
    data=third_df,
    x='product_category_name_english',
    y='purchase_amount',
    horizontal=True,
    x_label='Sales Amount',
    y_label='Product Category'
)

st.markdown('The bar chart above shows the top 10 sales amount of each product category in the last quartal. The product category with the highest sales amount is **Health & Beauty**.')

# fourth question visualization
st.markdown('---')
fourth_df = pd.read_csv('main_data/fourth_quest.csv')
st.header('4. Total Transaction per Payment Menthod ')
st.write('This visualization shows the total transaction per payment method.')

st.bar_chart(
    data=fourth_df,
    x='payment_type',
    y='payment_value',
    horizontal=True,
    x_label='Total Transaction',
    y_label='Payment Method'
)

st.markdown('The bar chart above shows the total transaction per payment method. The payment method with the highest total transaction is **credit_card**.')

# fifth question visualization
st.markdown('---')
fifth_df = pd.read_csv('main_data/fifth_quest.csv')

st.header('5. Sales Percentage Since Last Year')
st.write('This visualization shows the sales percentage change since last year.')

# Create a bar plot
fifth_figure = plt.figure(figsize=(20, 10))
plt.bar(fifth_df['product_category_name_english'], fifth_df['percentage_change'])
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.title('Percentage Change in Product Category Sales (Year to Year)')
plt.xlabel('Product Category')
plt.ylabel('Percentage Change (%)')
plt.xticks(rotation=75)
plt.grid(True, alpha=0.3)

# Add value labels
for i, v in enumerate(fifth_df['percentage_change']):
    plt.text(i, v + (1 if v > 0 else -1), 
            f'{v:,.1f}%', 
            ha='center', 
            va='bottom' if v > 0 else 'top',)

plt.tight_layout()

st.pyplot(fifth_figure)

st.markdown('The bar chart above shows the percentage change in sales for each product category since last year. The product category with the highest percentage increase is **Diapers & Hygene** with `2,400%` increase')


# sixth question visualization
st.markdown('---')
sixth_df = pd.read_csv('main_data/sixth_quest.csv')
st.header('6. Average Transaction Value per Month')
st.write('This visualization shows the average transaction value per month.')

st.line_chart(
    data=sixth_df,
    x='period_str',
    y= 'price',
    x_label='Year-Month',
    y_label='Average Transaction Value'
)

st.markdown('The line chart above shows the average transaction value per month. The average transaction value in overall month are above `120`')


# seventh question visualization
st.markdown('---')
seventh_df = pd.read_csv('main_data/seventh_quest.csv')

st.header('7. Photos Quantity and Sales Amount Correlation')
st.write('This visualization shows the correlation between photos quantity and sales amount.')

seventh_figure = plt.figure(figsize=(5, 4))
sns.heatmap(seventh_df.corr(), annot=True, cmap='viridis')
plt.title('Number of Photos vs Frequency')

st.pyplot(seventh_figure, use_container_width=False, clear_figure=True)

st.markdown('The heatmap above shows the correlation between photos quantity and sales amount. The correlation coefficient is `-0.62`, which indicates a strong negative correlation between the two variables. Hence, the lower the pictures quantity, the higher the sales amount.')
