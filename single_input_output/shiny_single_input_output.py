# ui is what the user sees
# server is what does stuff for the user
# (one main task of the server is "rendering" plots/text/etc)
from shiny import App, ui, render

# State which pieces should appear on the screen
app_ui = ui.page_fluid(
    # `input_` funcitons are how the user will give inputs
    # user inputs have a unique id that the server can
    # use to access the inputted value
    # (eg `input.selected_letter()` will get this dropdown's value)
    ui.input_select(
        id="selected_letter",
        label="Select label",
        selected="A",
        choices=["A", "B", "C"],
    ),
    # `output_` functions are how the server will talk back to the user
    # the output id matches the name of the function in the server that
    # makes the output
    # (eg `def example_output():` will render the text to display here)
    ui.output_text(id="example_output"),
)


# To make updates based on inputs
# Shiny has a `server` function
# Dash has `callbacks`
def server(input, output, session):
    @output
    @render.text
    def example_output():
        # `input.selected_letter()` comes from the `input_`
        # in the `ui` with `id="selected_letter"`
        return f"You chose: {input.selected_letter()}"


# Run it up
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
