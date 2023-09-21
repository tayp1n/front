import typing as t

import dash  # type: ignore
from dash import dcc, html, Input, Output, State, dash_table  # type: ignore
import pandas as pd
import plotly.express as px  # type: ignore
from skimage import io  # type: ignore
from collections import OrderedDict

app = dash.Dash(__name__, suppress_callback_exceptions=True)
data = pd.read_csv("app/assets/EmployeeSampleData.csv", encoding="latin1")

data_frame: OrderedDict[str, list] = OrderedDict([("Words", [])])
df = pd.DataFrame(data_frame)

app.layout = html.Div(
    [
        html.Link(
            rel="stylesheet",
            href="app/assets/styles/styles.css",
        ),
        html.H5("graph with employee data"),
        dcc.Graph(id="incidence-matrix"),
        html.H5("input field with save button"),
        dcc.Input(id="text-input", type="text", placeholder="Enter text..."),
        html.Button("Save", id="save-button"),
        dash_table.DataTable(
            id="word-table",
            data=df.to_dict("records"),
            columns=[{"id": c, "name": c} for c in df.columns],
            style_data={"whiteSpace": "normal", "height": "auto", "textAlign": "left"},
            style_header={"textAlign": "left", "display": None},
        ),
        html.H5("selectbox & imageclick"),
        dcc.Dropdown(
            id="image-selector",
            options=[
                {"label": "Image 1", "value": "app/assets/imgs/image1.jpeg"},
                {"label": "Image 2", "value": "app/assets/imgs/image2.jpeg"},
                {"label": "Image 3", "value": "app/assets/imgs/image3.jpeg"},
            ],
        ),
        html.Div(id="image-container"),
    ]
)


@app.callback(
    Output("incidence-matrix", "figure"), Input("incidence-matrix", "selectedData")
)
def update_employee_graph(selectedData):
    if selectedData is None:
        filtered_data = data
    else:
        points = selectedData["points"]
        selected_cities = [point["text"] for point in points]
        filtered_data = data[data["City"].isin(selected_cities)]

    fig = px.scatter(
        filtered_data,
        x="Bonus %",
        y="Annual Salary",
        color="City",
        labels={"Bonus %": "Bonus Amount", "Annual Salary": "Salary"},
    )

    return fig


@app.callback(Output("selected-image", "src"), Input("image-selector", "value"))
def update_selected_image(image_path):
    return image_path


@app.callback(
    Output("image-container", "children"),
    [Input("image-selector", "value"), Input("image-container", "n_clicks")],
)
def update_image_and_display_clicked_content(selected_image, n_clicks):
    if not n_clicks:
        return html.Img(src=selected_image, style={"max-width": "100%"}), None

    click_info = {
        "event_type": "click",
        "clicked_element": selected_image,
    }

    image = io.imread(selected_image)

    fig = px.imshow(image)
    fig.update_layout(dragmode="drawrect")
    config = {
        "modeBarButtonsToAdd": [
            "drawline",
            "drawopenpath",
            "drawclosedpath",
            "drawcircle",
            "drawrect",
            "eraseshape",
        ]
    }

    print(click_info)

    return (
        html.Div(
            [
                html.H3("Drag and draw annotations"),
                dcc.Graph(figure=fig, config=config),
            ]
        ),
        None,
    )


@app.callback(
    Output("word-table", "data"),
    Input("save-button", "n_clicks"),
    State("text-input", "value"),
    State("word-table", "data"),
)
def add_word_to_table(
    n_clicks: int, new_word: str, current_data: t.List[t.Dict[str, t.Any]]
) -> t.List[t.Dict[str, t.Any]]:
    if n_clicks is None:
        return current_data
    if not new_word:
        return current_data

    updated_data = current_data + [{"Words": new_word}]

    return updated_data


def get_app():
    return app
