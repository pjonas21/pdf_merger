import os
import flet as ft
from PyPDF2 import PdfMerger

def merge_pdf(folder_path: str, file_name: str, page: ft.Page):
    if not os.path.isdir(folder_path):
        page.open(page.controls[-3])
        page.update()
        return
    
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
    if not pdf_files:
        page.open(page.controls[-2])
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

    page.open(page.controls[-1])
    page.controls[0].controls[0].value = ""
    page.update()
    return
    
