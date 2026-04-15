import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Page setup
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📊 Real-Time Stock Market Dashboard")
st.write("Enter a stock symbol like AAPL, TSLA, RELIANCE.NS")

# Input box
stock = st.text_input("Stock Symbol")

# Time period selector
period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

if stock:
    # Download stock data
    data = yf.download(stock, period=period, interval="1d")

    if data.empty:
        st.error("No data found. Check stock symbol.")
    else:
        st.subheader(f"Showing data for: {stock}")

        # Show table
        st.dataframe(data.tail())

        # Line chart (Close price)
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Close"],
                mode="lines",
                name="Close Price"
            )
        )

        fig.update_layout(
            title="Stock Price Trend",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Candlestick chart
        fig2 = go.Figure(
            data=[
                go.Candlestick(
                    x=data.index,
                    open=data["Open"],
                    high=data["High"],
                    low=data["Low"],
                    close=data["Close"],
                    name="Candlestick"
                )
            ]
        )

        fig2.update_layout(
            title="Candlestick Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_dark"
        )

        st.plotly_chart(fig2, use_container_width=True)