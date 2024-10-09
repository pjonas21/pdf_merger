import os
import flet as ft
from PyPDF2 import PdfMerger

def merge_pdf(folder_path: str, file_name: str, page: ft.Page):
    if not os.path.isdir(folder_path):
        page.controls[-1].value = "O caminho não é uma pasta válida."
        page.controls[-1].size = 16
        page.controls[-1].color = ft.colors.RED_700
        page.controls[-1].weight=ft.FontWeight.BOLD
        page.controls[-1].italic=True
        page.update()
        return
    
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
    if not pdf_files:
        page.controls[-1].value = "Nenhum arquivo encontrado."
        page.controls[-1].size = 16
        page.controls[-1].color = ft.colors.ORANGE_700
        page.controls[-1].weight=ft.FontWeight.BOLD
        page.controls[-1].italic=True
        page.update()
        return
    
    merger = PdfMerger()
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)

    if not file_name:
        file_name = 'pdf-combinado'

    output_path = os.path.join(folder_path, f'{file_name}.pdf')
    merger.write(output_path)
    merger.close()

    page.controls[-1].value = f"Sucesso. \nCaminho {output_path}"
    page.controls[-1].size = 16
    page.controls[-1].color = ft.colors.GREEN_700
    page.controls[-1].weight=ft.FontWeight.BOLD
    page.controls[-1].italic=True
    page.update()
    return
    
