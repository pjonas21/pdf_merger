import flet as ft
import json
from merger import merge_pdf


def main(page: ft.Page):

    def on_pick_folder(e):
        if e.data:
            folder_data = json.loads(e.data)
            folder_path.value = f"{folder_data['path']}"
            page.update()
    

    page.title = "PDF Merger"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.icon = "assets\\icons\\pdf.ico"
    page.padding = ft.padding.all(10)
    page.window.height = 400
    page.window.width = 650

    folder_path = ft.TextField(label="Caminho da pasta", width=400)
    file_name = ft.TextField(label="Nome do arquivo de saída", width=400)
    status_label = ft.Text("", width=400)

    dialog = ft.FilePicker(on_result = on_pick_folder)

    select_folder_btn = ft.ElevatedButton(
        text="Selecionar pasta",
        on_click=lambda _: dialog.get_directory_path()
    )

    combine_btn = ft.ElevatedButton(
        text="Combinar PDFs",
        on_click = lambda _: merge_pdf(folder_path.value, file_name.value, page)
    )

    folder_row = ft.Row(
        controls=[
            folder_path,
            select_folder_btn
        ]
    )

    page.overlay.append(dialog)
    page.add(folder_row, file_name, combine_btn, status_label)

ft.app(target=main)