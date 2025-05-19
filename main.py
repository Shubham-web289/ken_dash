import pandas as pd
from dash import Dash, dash_table, html, Input, Output, State

# Create a sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "Country": ["India", "USA", "Canada"]
})

# Define the global Dash app
app = Dash(__name__)
app.title = "Column Deletion Table"
server = app.server  # Required by Posit Connect

# Define app layout
app.layout = html.Div([
    html.H2("📊 Editable Table with Column Deletion"),
    dash_table.DataTable(
        id='editable-table',
        columns=[{"name": col, "id": col, "deletable": True} for col in df.columns],
        data=df.to_dict("records"),
        editable=True,
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "center"},
    ),
    html.Br(),
    html.Div(id='table-info')
])

# Define callback
@app.callback(
    Output('table-info', 'children'),
    Input('editable-table', 'data'),
    State('editable-table', 'columns')
)
def update_shape(data, columns):
    df_new = pd.DataFrame(data)
    visible_cols = [col["id"] for col in columns]
    return f"✅ Current shape: {df_new.shape[0]} rows × {len(visible_cols)} columns"

# Optional: for local testing
if __name__ == "__main__":
    app.run_server(debug=True)
