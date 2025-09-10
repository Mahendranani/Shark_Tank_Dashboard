


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # -------------------- PAGE CONFIG --------------------
# st.set_page_config(
#     page_title="Shark Tank India Dashboard",
#     page_icon="🦈",
#     layout="wide"
# )

# # -------------------- LOAD DATA --------------------
# df = pd.read_csv("data/shark_tank_clean.csv")

# # Clean deal amount
# df["total_deal_amount"] = pd.to_numeric(df["total_deal_amount"], errors="coerce").fillna(0)

# # -------------------- THEME STYLING --------------------
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#         background-color: #F7F9FB;
#         color: #171A1C;
#     }

#     .metric-card {
#         background: #E6F1FF;
#         border-radius: 16px;
#         padding: 20px;
#         text-align: center;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.05);
#         transition: transform 0.2s ease-in-out;
#     }
#     .metric-card:hover {
#         transform: translateY(-4px);
#     }
#     .metric-card h3 {
#         font-size: 18px;
#         font-weight: 400;
#         margin-bottom: 8px;
#         color: #171A1C;
#     }
#     .metric-card h2 {
#         font-size: 28px;
#         font-weight: 700;
#         color: #006EFE;
#     }

#     .top-bar {
#         background: linear-gradient(90deg, #006EFE, #4BA3FF);
#         padding: 15px;
#         border-radius: 12px;
#         color: white;
#         margin-bottom: 20px;
#         text-align: center;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # -------------------- SIDEBAR --------------------
# st.sidebar.image("assets/logo.png", use_container_width=True)
# st.sidebar.title("Navigation")

# page = st.sidebar.radio("Go to", ["Overview", "Industry Insights", "Shark Profiles", "Deal Analysis"])

# # -------------------- MAIN DASHBOARD --------------------
# st.markdown("<div class='top-bar'><h1>🦈 Shark Tank India Dashboard</h1></div>", unsafe_allow_html=True)

# # -------------------- KPIs --------------------
# total_pitches = df.shape[0]
# startups_funded = df[df["total_deal_amount"] > 0].shape[0]
# funding_success_rate = round((startups_funded / total_pitches * 100), 1) if total_pitches > 0 else 0

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown(f"<div class='metric-card'><h3>📊 Total Pitches</h3><h2>{total_pitches}</h2></div>", unsafe_allow_html=True)

# with col2:
#     st.markdown(f"<div class='metric-card'><h3>🚀 Startups Funded</h3><h2>{startups_funded}</h2></div>", unsafe_allow_html=True)

# with col3:
#     st.markdown(f"<div class='metric-card'><h3>📈 Funding Success Rate</h3><h2>{funding_success_rate}%</h2></div>", unsafe_allow_html=True)

# # -------------------- PAGE ROUTES --------------------
# if page == "Overview":
#     st.subheader("Pitch Overview")
#     st.dataframe(df.head(10))

# elif page == "Industry Insights":
#     st.subheader("Top 10 Industries by Pitches")
#     industry_count = df["industry"].value_counts().head(10).reset_index()
#     industry_count.columns = ["Industry", "Count"]

#     fig = px.bar(
#         industry_count,
#         x="Industry",
#         y="Count",
#         text="Count",
#         color="Industry",
#         color_discrete_sequence=px.colors.sequential.Blues
#     )
#     fig.update_layout(
#         plot_bgcolor="#FFFFFF",
#         paper_bgcolor="#FFFFFF",
#         showlegend=False,
#         font=dict(family="Inter")
#     )
#     st.plotly_chart(fig, use_container_width=True)

# # ---------------------- Shark Profiles ----------------------
# # ---------------------- Shark Profiles ----------------------
# elif page == "Shark Profiles":
#     st.header("🦈 Shark Profiles")

#     # Shark list with images
#     sharks = {
#         "Aman Gupta": "images/aman.png",
#         "Namita Thapar": "images/namita.png",
#         "Peyush Bansal": "images/peyush.png",
#         "Anupam Mittal": "images/anupam.png",
#         "Vineeta Singh": "images/vineeta.png",
#         "Amit Jain": "images/amit.png",
#         "Ritesh Agarwal": "images/ritesh.png",
#     }

#     # Selectbox
#     selected_shark = st.selectbox("Select a Shark", list(sharks.keys()))

#     # Show shark image
#     st.image(sharks[selected_shark], caption=selected_shark, width=200)

#     # Find the investment and equity columns for this shark
#     shark_cols = [col for col in df.columns if selected_shark.split()[0].lower() in col.lower() and "investment_amount" in col]

#     if shark_cols:
#         amt_col = shark_cols[0]
#         equity_col = amt_col.replace("investment_amount", "investment_equity")

#         # Metrics
#         total_deals = df[df[amt_col] > 0].shape[0]
#         total_amount = df[amt_col].sum()
#         avg_equity = df[equity_col].mean()

#         # Overview
#         st.markdown(f"#### {selected_shark} Overview")
#         c1, c2, c3 = st.columns(3)
#         c1.metric("Deals Invested", total_deals)
#         c2.metric("Total Invested in Lakhs ", f"₹ {total_amount:,.0f}")
#         c3.metric("Avg Equity (%)", f"{avg_equity:.2f}%")

#         # Industry distribution
#         st.markdown("##### Investment by Industry")
#         invest_ind = (
#             df.groupby("industry")[amt_col]
#               .sum()
#               .reset_index()
#               .sort_values(by=amt_col, ascending=False)
#         )

#         fig3 = px.bar(
#             invest_ind,
#             x="industry",
#             y=amt_col,
#             title=f"{selected_shark}'s Investments by Industry",
#             template="plotly_white",
#             color="industry",
#             text_auto=True
#         )
#         fig3.update_layout(showlegend=False)
#         st.plotly_chart(fig3, use_container_width=True)

#     else:
#         st.warning("No investment data available for this shark.")


# # ---------------------- Deal Analysis ----------------------
# elif page == "Deal Analysis":
#     st.header("📊 Deal Analysis")

#     # Investment distribution by Shark
#     shark_cols = [c for c in df.columns if "_investment_amount" in c]
#     shark_investments = df[shark_cols].sum().reset_index()
#     shark_investments.columns = ["Shark", "Investment"]
#     shark_investments["Shark"] = shark_investments["Shark"].str.replace("_investment_amount", "").str.title()

#     fig = px.pie(
#         shark_investments,
#         names="Shark",
#         values="Investment",
#         color_discrete_sequence=px.colors.sequential.Blues
#     )
#     fig.update_traces(textinfo="percent+label")
#     st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Shark Tank India Dashboard",
    page_icon="🦈",
    layout="wide"
)

# -------------------- LOAD DATA --------------------
df = pd.read_csv("data/shark_tank_clean.csv")
df["total_deal_amount"] = pd.to_numeric(df["total_deal_amount"], errors="coerce").fillna(0)

# -------------------- CURRENCY FORMATTING --------------------
def format_crores(amount):
    return f"₹ {amount / 1e2:,.2f} Cr"  # Assuming amount is in lakhs, convert to crores

# -------------------- THEME STYLING --------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F7F9FB;
        color: #171A1C;
    }

    /* Sidebar gradient background */
    .css-1d391kg {
        background: linear-gradient(135deg, #F7F9FB 0%, #E6F1FF 100%) !important;
    }

    .metric-card {
        background: #E6F1FF;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out;
    }
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0,110,254,0.12);
    }
    .metric-card h3 {
        font-size: 1.2rem;
        font-weight: 400;
        margin-bottom: 8px;
        color: #171A1C;
    }
    .metric-card h2 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #006EFE;
    }

    .top-bar {
        background: linear-gradient(90deg, #006EFE 0%, #4BA3FF 100%);
        padding: 15px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        text-align: center;
    }
    .top-bar small {
        font-weight: 400;
        opacity: 0.8;
    }

    /* Responsive font sizes */
    @media (max-width: 768px) {
        .metric-card h2 {
            font-size: 1.5rem !important;
        }
        .metric-card h3 {
            font-size: 1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------
st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Overview", "Industry Insights", "Shark Profiles", "Deal Analysis","Industries"])

# -------------------- MAIN HEADER --------------------
st.markdown("""
    <div class='top-bar'>
        <h1>🦈 Shark Tank India Dashboard</h1>
        <small>Analytics Portfolio by Mahendra</small>
    </div>
""", unsafe_allow_html=True)

# -------------------- KPIs (General) --------------------
total_pitches = df.shape[0]
startups_funded = df[df["total_deal_amount"] > 0].shape[0]
funding_success_rate = round((startups_funded / total_pitches * 100), 1) if total_pitches > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-card'><h3>📊 Total Pitches</h3><h2>{total_pitches}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h3>🚀 Startups Funded</h3><h2>{startups_funded}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><h3>📈 Funding Success Rate</h3><h2>{funding_success_rate}%</h2></div>", unsafe_allow_html=True)

# -------------------- PAGE ROUTES --------------------
if page == "Overview":
    st.subheader("Pitch Overview")
    st.dataframe(df.head(10))

elif page == "Industry Insights":
    st.subheader("Top 10 Industries by Pitches")
    industry_count = df["industry"].value_counts().head(10).reset_index()
    industry_count.columns = ["Industry", "Count"]

    fig = px.bar(
        industry_count,
        x="Industry",
        y="Count",
        text="Count",
        color="Industry",
        color_discrete_sequence=px.colors.sequential.Blues
    )
    fig.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        showlegend=False,
        font=dict(family="Inter")
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Shark Profiles":
    st.header("🦈 Shark Profiles")

    sharks = {
        "Aman Gupta": "images/aman.png",
        "Namita Thapar": "images/namita.png",
        "Peyush Bansal": "images/peyush.png",
        "Anupam Mittal": "images/anupam.png",
        "Vineeta Singh": "images/vineeta.png",
        "Amit Jain": "images/amit.png",
        "Ritesh Agarwal": "images/ritesh.png",
    }

    selected_shark = st.selectbox("Select a Shark", list(sharks.keys()))
    st.image(sharks[selected_shark], caption=selected_shark, width=200)

    shark_cols = [col for col in df.columns if selected_shark.split()[0].lower() in col.lower() and "investment_amount" in col]

    if shark_cols:
        amt_col = shark_cols[0]
        equity_col = amt_col.replace("investment_amount", "investment_equity")
        total_deals = df[df[amt_col] > 0].shape[0]
        total_amount = df[amt_col].sum()
        avg_equity = df[equity_col].mean()

        st.markdown(f"#### {selected_shark} Overview")
        c1, c2, c3 = st.columns(3)
        c1.metric("Deals Invested", total_deals)
        c2.metric("Total Invested (₹ Cr)", format_crores(total_amount))
        c3.metric("Avg Equity (%)", f"{avg_equity:.2f}%")

        st.markdown("##### Investment by Industry")
        invest_ind = (
            df.groupby("industry")[amt_col]
            .sum()
            .reset_index()
            .sort_values(by=amt_col, ascending=False)
        )

        fig3 = px.bar(
            invest_ind,
            x="industry",
            y=amt_col,
            title=f"{selected_shark}'s Investments by Industry",
            template="plotly_white",
            color="industry",
            text_auto=True
        )
        fig3.update_layout(showlegend=False)
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("No investment data available for this shark.")

elif page == "Deal Analysis":
    st.header("📊 Deal Analysis")

    shark_cols = [c for c in df.columns if "_investment_amount" in c]
    shark_investments = df[shark_cols].sum().reset_index()
    shark_investments.columns = ["Shark", "Investment"]
    shark_investments["Shark"] = shark_investments["Shark"].str.replace("_investment_amount", "").str.title()

    fig = px.pie(
        shark_investments,
        names="Shark",
        values="Investment",
        color_discrete_sequence=px.colors.sequential.Blues
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)
    
elif page == "Industries":
    st.header("🏭 Industries Filtered Dashboard")

   
    st.markdown("### Filter Industries")
    industry_filter = st.multiselect(
        "Choose Industries", df["industry"].unique(), default=df["industry"].unique()
    )
    filtered_df = df[df["industry"].isin(industry_filter)]

    # KPIs (Filtered — update as industry selection changes)
    st.markdown("---")
    fc1, fc2, fc3 = st.columns(3)
    fc1.metric("Total  Pitches", filtered_df.shape[0])
    filtered_funded = filtered_df[filtered_df["total_deal_amount"] > 0].shape[0]
    filtered_rate = round((filtered_funded / filtered_df.shape[0] * 100), 1) if filtered_df.shape[0] > 0 else 0
    fc2.metric(" Startups Funded", filtered_funded)
    fc3.metric(" Funding Success Rate (%)", filtered_rate)

    # Optional: Show selected industries
    st.write(f"Selected Industries: {', '.join(industry_filter)}")

    # Industry table/bar chart
    st.subheader("Filtered Pitch Data")
    st.dataframe(filtered_df)

    invest_ind = (
        filtered_df.groupby("industry")["total_deal_amount"]
        .sum()
        .reset_index()
        .sort_values(by="total_deal_amount", ascending=False)
    )

    fig = px.bar(
        invest_ind,
        x="industry",
        y="total_deal_amount",
        title="Total Investment by Industry (Filtered)",
        template="plotly_white",
        color="industry",
        text_auto=True
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

