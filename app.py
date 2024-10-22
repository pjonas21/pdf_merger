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
    page.window.height = 300
    page.window.width = 600

    folder_path = ft.TextField(label="Caminho da pasta", width=400)
    file_name = ft.TextField(label="Nome do arquivo de saída", width=400)

    dialog = ft.FilePicker(on_result = on_pick_folder)

    select_folder_btn = ft.ElevatedButton(
        text="Selecionar pasta",
        on_click=lambda _: dialog.get_directory_path(),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    combine_btn = ft.ElevatedButton(
        text="Combinar PDFs",
        on_click = lambda _: merge_pdf(folder_path.value, file_name.value, page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    folder_row = ft.Row(
        controls=[
            folder_path,
            select_folder_btn
        ]
    )

    def handle_close(e):
        page.close(dlg_modal_success)

    def handle_close_error(e):
        page.close(dlg_modal_folder_error)

    def handle_close_file_error(e):
        page.close(dlg_modal_file_error)

    dlg_modal_success = ft.AlertDialog(
        modal = True,
        title=ft.Text("Resultado"),
        content=ft.Text("Operação realizada com sucesso.", style=ft.TextStyle(color="green")),
        actions=[
            ft.TextButton("OK", on_click=handle_close)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    dlg_modal_folder_error = ft.AlertDialog(
        modal = True,
        title=ft.Text("Erro"),
        content=ft.Text("O caminho não é uma pasta válida.", style=ft.TextStyle(color="red")),
        actions=[
            ft.TextButton("OK", on_click=handle_close_error)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    dlg_modal_file_error = ft.AlertDialog(
        modal = True,
        title=ft.Text("Erro"),
        content=ft.Text("Nenhum arquivo encontrado.", style=ft.TextStyle(color="red")),
        actions=[
            ft.TextButton("OK", on_click=handle_close_file_error)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.overlay.append(dialog)
    page.add(
        folder_row, 
        file_name, 
        combine_btn, 
        dlg_modal_folder_error,
        dlg_modal_file_error,
        dlg_modal_success
        )

ft.app(target=main)