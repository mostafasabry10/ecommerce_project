
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide', page_title='Ecommerce EDA')

st.markdown("<h1 style='text-align: center; color: white;'>Ecommerce KPIs</h1>", unsafe_allow_html= True)

st.image('https://marketplace.canva.com/EAGkJu6RBag/1/0/1600w/canva-pink-and-white-minimalist-e-commerce-presentation-pUrMakjsI6U.jpg')

df = pd.read_csv('Cleaned_df.csv',index_col=0)

st.dataframe(df)

total_revenue = df['total_price'].sum()

total_orders = df['sales_id'].nunique()

total_coustomers = df['customer_name'].nunique()

avg_order_value = df['total_price'].mean()

col1,col2,col3,col4 = st.columns(4)

with col1 :
    st.metric('Total Revenue',total_revenue)

with col2 :
    st.metric('Total Orders',total_orders)

with col3 :
    st.metric('Total Coustomers',total_coustomers)

with col4 :
    st.metric('Average Order Value',avg_order_value)

    
df_sort = df.sort_values(by = 'order_date')
plot_df = df_sort.groupby('order_date')['total_price'].sum().reset_index()
st.plotly_chart(px.line(plot_df,x = 'order_date',y = 'total_price'))


st.plotly_chart(px.histogram(df,x = 'product_type',color = 'colour',barmode = 'group'))

plot_df = df['city'].value_counts().head(10).reset_index()
st.plotly_chart(px.bar(plot_df,x = 'city',y = 'count',text_auto=True))
