from weasyprint import HTML  # pip install weasyprint
import os


def convert(file: str, html_string: str) -> str:
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
    HTML(string=html_string).write_pdf(file)
    return os.path.abspath(file)

