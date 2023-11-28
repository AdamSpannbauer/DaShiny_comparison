# Dash and Shiny for Python

A series of simple apps to compare the syntax, usability, and ideas for two quick web app frameworks: Dash and Shiny for Python.

Each section has a file for the equivalent app in both Dash and Shiny.  The files are commented to add notes.  The comments assume you go through the sections in order (ie the later sections won't comment on the basics).

We're skipping making a blank page that does nothing.... boring.  Doing things is cool, not doing things is only cool irl, not in web apps.

## Single input and output

A page with a drop down menu and a text output that confirms the user's selection.

**Dash** - [`single_input_output/dash_single_input_output.py`](single_input_output/dash_single_input_output.py)

<p align="center">
  <kbd>
  <img width="50%" src="readme/dash_single_input_output.png">
  </kbd>
</p>

**Shiny** - [`single_input_output/shiny_single_input_output.py`](single_input_output/shiny_single_input_output.py)

<p align="center">
  <kbd>
  <img width="50%" src="readme/shiny_single_input_output.png">
  </kbd>
</p>


## Rows, columns, and plots

A page with two plots and two inputs that filter the plots.  All four components organized using bootstrap rows and columns.

**Dash** - [`rows_cols_plots/dash_rows_cols_plots.py`](rows_cols_plots/dash_rows_cols_plots.py)

<p align="center">
  <kbd>
  <img width="50%" src="readme/dash_rows_cols_plots.png">
  </kbd>
</p>


**Shiny** - [`rows_cols_plots/shiny_rows_cols_plots.py`](rows_cols_plots/shiny_rows_cols_plots.py)

<p align="center">
  <kbd>
  <img width="50%" src="readme/shiny_rows_cols_plots.png">
  </kbd>
</p>

## Wanna contribute?

Add a comparison... pls... ?

**How to**:
* Fork
* Make folder and apps
* Add a section to README.md (copy current sections format)
* Pull Request

Open an Issue if you'd like to discuss before working (ie make an issue named "add navbar example" and the discussion has started).

## More official resources

### Dash

"Dash in 20 minutes<sup>1</sup>": https://dash.plotly.com/tutorial 

<sub>(<sup>1</sup>times might vary)</sub>

### Shiny

If you are familiar with Shiny in R, this resource is really really good: https://shiny.posit.co/py/docs/comp-r-shiny.html

This is a more ground up approach: https://shiny.posit.co/py/docs/overview.htmlhttps://dash.plotly.com/tutorial
