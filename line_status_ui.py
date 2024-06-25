import flet
from flet import IconButton, Page, Row, TextField, icons
from line_status import get_status
from extensions import app

# import flet as ft

def main(page: flet.Page):

    page.title = "Flet example"
    page.vertical_alignment = "center"
    txt_number = TextField(value="0", text_align="right", width=100)
    txt_line = ""

    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        txt_line = dd.value

        # choose_line(txt_line)
        try:
             with app.app_context(): # Ensure the application context is pushed
                status = get_status(txt_line)
        except Exception as e:
            print(e)
            status = "Failed to get line status"

        t.value += f"\nStatus: {status}"
        page.update()

    t = flet.Text()
    b = flet.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = flet.Dropdown(
        width=200,
        options=[
            flet.dropdown.Option("DLR"),
            flet.dropdown.Option("Central"),
            flet.dropdown.Option("Jubilee"),
            flet.dropdown.Option("Victoria"),
        ],
    )
    page.add(dd, b, t)

    # def choose_line(e):
    #     status = get_line_status(txt_line.lower())
    #     page.update()
    
    # page.add(
    #     IconButton(tooltip="Get Line Status", on_click=choose_line)
    # )

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )
flet.app(target=main)