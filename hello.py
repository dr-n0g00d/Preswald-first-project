# By: Prasannadatta Kawadkar
# On: 8 May 2025

from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# Connect and load data
connect()
df = get_df("housing")

# Get top 15 by median_income
sql = """
SELECT total_rooms, total_bedrooms, median_income
FROM housing
ORDER BY median_income DESC
LIMIT 15
"""
filtered_df = query(sql, "housing")

# heading
text("# California Housing Visualization")
text("A comparison of median income, room counts, and bedroom availability in top-earning housing areas.")

# Table preview
table(filtered_df, title="Top 15 by Median Income")

# Bar chart: Income vs Total Rooms
fig_bar = px.bar(
    filtered_df,
    x="median_income",
    y="total_rooms",
    color_discrete_sequence=["#ff4d4d"],
    labels={"median_income": "Median Income", "total_rooms": "Total Rooms"},
    title="Total Rooms vs Median Income"
)
fig_bar.update_layout(
    plot_bgcolor="#fff8f8",
    paper_bgcolor="#ffffff",
    font=dict(size=14),
    title_x=0.5
)
plotly(fig_bar)

# Line chart: Total Bedrooms vs Total Rooms
fig_line = px.line(
    filtered_df,
    x="total_rooms",
    y="total_bedrooms",
    markers=True,
    line_shape="linear",
    color_discrete_sequence=["#cc0066"],
    labels={"total_rooms": "Total Rooms", "total_bedrooms": "Total Bedrooms"},
    title="Total Bedrooms vs Total Rooms"
)
fig_line.update_layout(
    plot_bgcolor="#fff8f8",
    paper_bgcolor="#ffffff",
    font=dict(size=14),
    title_x=0.5
)
plotly(fig_line)
