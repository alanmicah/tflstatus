import flet as ft
from flet import IconButton, Page, Row, TextField, icons
import line_status

import flet as ft

def main(page: ft.Page):

    page.title = "Flet example"
    page.vertical_alignment = "center"
    txt_number = TextField(value="0", text_align="right", width=100)
    txt_line = ""

    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        txt_line = dd.value

        choose_line(txt_line)

        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("DLR"),
            ft.dropdown.Option("Central"),
            ft.dropdown.Option("Jubilee"),
            ft.dropdown.Option("Victoria"),
        ],
    )
    page.add(dd, b, t)

    def choose_line(e):
        line_status(txt_line.lower())
        page.update()
    
    page.add(
        IconButton(tooltip="Get Line Status", on_click=choose_line)
    )

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
ft.app(target=main)