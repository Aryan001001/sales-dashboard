import streamlit as st
import pandas as pd
import sqlite3

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM Sales", conn)

# ---------------- PROCESSING ----------------
df['revenue'] = df['price'] * df['quantity']

# ---------------- TITLE ----------------
st.title("📊 Sales Performance Dashboard")
st.markdown("Analyze revenue, products, and regional performance in real-time")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔍 Filters")

region = st.sidebar.selectbox("Select Region", df['region'].unique())

df = df[df['region'] == region]

# ---------------- KPI CARDS ----------------
st.markdown("## 📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹ {int(df['revenue'].sum())}")
col2.metric("📦 Total Orders", len(df))
col3.metric("📊 Avg Revenue", f"₹ {int(df['revenue'].mean())}")

st.divider()

# ---------------- CHARTS (SIDE BY SIDE) ----------------
col1, col2 = st.columns(2)

# Category chart
with col1:
    st.subheader("📊 Category-wise Revenue")
    category_sales = df.groupby('category')['revenue'].sum()
    st.bar_chart(category_sales)

# Top products chart
with col2:
    st.subheader("🏆 Top Products")
    top_products = df.groupby('product_name')['revenue'].sum().sort_values(ascending=False)
    st.bar_chart(top_products)

st.divider()

# ---------------- TABLE ----------------
st.subheader("📋 Sales Data")
st.dataframe(df, use_container_width=True)