# `Dash` for initializing app
# `html` for adding html elements (like text, titles, divs)
# `dcc` is a collection of "dash core components" (like dropdown menus)
# `Input`/`Output` needed for your app to do things
from dash import Dash, html, dcc, Input, Output


# Initialize app
app = Dash(__name__)

# State which pieces should appear on the screen
app.layout = html.Div(
    [
        # input components will have an `id` that you
        # need to access the values users inputted
        # we can access this dropdown's value with
        # Input("letter_dropdown", "value")
        dcc.Dropdown(
            options=["A", "B", "C"],
            value="A",
            id="letter_dropdown",
        ),
        # This is currently an empty container with a name tag
        # The contents of the Div are called `children`
        # We'll update the contents of this container with
        # Output("example_output", "children")
        html.Div(id="example_output"),
    ]
)


# To make updates based on inputs
# Shiny has a `server` function
# Dash has `callbacks`
@app.callback(
    # Output("id of layout component to update", "piece of component to update")
    Output("example_output", "children"),
    # Input("id of input component to update", "piece of component to update")
    Input("letter_dropdown", "value"),
)
# This function has one argument coming from my one `Input`
# We have flexibility in naming the argument to the function,
# but it's value is coming from `letter_dropdown`'s `value`
def update_example_output(selected_letter):
    return f"You chose: {selected_letter}"


# Run it up
if __name__ == "__main__":
    app.run(debug=True)
