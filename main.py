# minimal_dash_app.py

from dash import Dash, html

# Create Dash app instance
app = Dash(__name__)
app.title = "Minimal Dash App"

# Define layout
app.layout = html.Div([
    html.H1("Hello, Dash!"),
    html.P("This is a minimal Dash application with some text.")
])

# Run the server
if __name__ == "__main__":
    app.run()
