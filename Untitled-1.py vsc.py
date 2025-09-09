import plotly.express as px
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)
import plotly.express as px


fig = px.bar(data, x='Game_title', y='Hours', color="Game_title",  color_discrete_map={
        'Dota 2': '#a6611a',
        'Counter-Strike Global Offensive': '#dfc27d',
    'Team Fortress 2': '#f5f5f5',
    'Counter-Strike': '#80cdc1', "Sid Meier's Civilization V": '#018571'
    })
fig.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black",
    legend_title_font_color="black",
   title={
        'text': "<b>Game Titles and Hours Played<b>",
        'y':0.93,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="<b>Game Titles<b>",
    yaxis_title="<b>Hours Played<b>",
    legend_title="<b>Game Titles<b>"
    )


fig.update_xaxes(title_font_family="Times New Roman")
fig.show()