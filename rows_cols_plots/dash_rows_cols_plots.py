from dash import Dash, dcc, html, Input, Output

# to make some nice interactive plots with plotly
import plotly.express as px

# to use rows and cols and theme
import dash_bootstrap_components as dbc

# Get some data and clean data for user inputs
df = px.data.gapminder()
countries = df["country"].sort_values().unique()
years = df["year"].sort_values().unique()

app = Dash(
    __name__,
    # Use a pre-made theme
    external_stylesheets=[dbc.themes.CERULEAN],
)

app.layout = html.Div(
    [
        # Add a title
        html.H1("Gapminder data"),
        # 2 rows with 2 columns each
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="scatter")),
                dbc.Col(dcc.Graph(id="bar")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6("Select a country"),
                        dcc.Dropdown(
                            options=countries,
                            value=countries[0],
                            id="country-dropdown",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6("Select a year"),
                        dcc.Slider(
                            min=min(years),
                            max=max(years),
                            step=5,
                            # this is crazy, gives a lot of control but unwieldy
                            marks={y: str(y) for y in range(min(years), max(years), 5)},
                            value=years[0],
                            id="year-slider",
                        ),
                    ]
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("scatter", "figure"),
    Input("country-dropdown", "value"),
)
def update_scatter(country):
    # filter to selected country and render scatter chart
    # of country's gdp x lifeExp
    plot_df = df[df["country"] == country]
    fig = px.scatter(plot_df, x="gdpPercap", y="lifeExp", log_x=True)

    return fig


@app.callback(
    Output("bar", "figure"),
    Input("year-slider", "value"),
)
def update_scatter(year):
    # filter to selected year and render bar chart
    # of top lifeExp countries
    plot_df = df[df["year"] == year]
    plot_df = plot_df.sort_values("lifeExp", ascending=False).head(10)
    fig = px.bar(plot_df, x="country", y="lifeExp")

    return fig


if __name__ == "__main__":
    app.run(debug=True)
