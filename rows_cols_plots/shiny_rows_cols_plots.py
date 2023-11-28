from shiny import App, ui

# to give us an easy theme to apply
import shinyswatch

# to make some nice interactive plots with plotly
import plotly.express as px

# `ui` doesn't come with "render_plotly" instead
# our plotly plots will be "widgets"
from shinywidgets import output_widget, render_widget

# Get some data and clean data for user inputs
df = px.data.gapminder()
countries = list(df["country"].sort_values().unique())
years = list(df["year"].sort_values().unique())

app_ui = ui.page_fluid(
    # Use a pre-made theme
    shinyswatch.theme.cerulean(),
    # Add a title
    ui.h1("Gapminder data"),
    # 2 rows with 2 columns each
    ui.row(
        # according to bootstrap the screen is 12 units wide
        # here are two columns 6 wide each (takes whole screen)
        # unfortunately, avoid saying `width=6`
        ui.column(6, output_widget("scatter")),
        ui.column(6, output_widget("bar")),
    ),
    ui.row(
        ui.column(
            6,
            ui.input_select(
                id="selected_country",
                label="Select a country",
                choices=countries,
                selected=countries[0],
            ),
            align="center",
        ),
        ui.column(
            6,
            ui.input_slider(
                id="selected_year",
                label="Select a year",
                min=min(years),
                max=max(years),
                value=years[0],
                step=5,
                # remove the comma (1,952 becomes 1952)
                sep="",
            ),
            align="center",
        ),
    ),
)


def server(input, output, session):
    @output
    @render_widget
    def scatter():
        # filter to selected country and render scatter chart
        # of country's gdp x lifeExp
        plot_df = df[df["country"] == input.selected_country()]
        fig = px.scatter(plot_df, x="gdpPercap", y="lifeExp", log_x=True)

        return fig

    @output
    @render_widget
    def bar():
        # filter to selected year and render bar chart
        # of top lifeExp countries
        plot_df = df[df["year"] == input.selected_year()]
        plot_df = plot_df.sort_values("lifeExp", ascending=False).head(10)
        fig = px.bar(plot_df, x="country", y="lifeExp")

        return fig


app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
