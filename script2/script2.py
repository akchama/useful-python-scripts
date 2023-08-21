from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def read_from_txt(file_name):
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Form the full path to the file
    full_path = os.path.join(dir_path, file_name)

    with open(full_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words


def write_to_pdf(words, output_file):
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Form the full path to the font file
    font_path = os.path.join(dir_path, "DejaVuSans.ttf")
    font_name = "DejaVuSans"
    pdfmetrics.registerFont(TTFont(font_name, font_path))
    words = [word.capitalize() for word in words]
    words.sort()

    c = canvas.Canvas(output_file, pagesize=landscape(letter))
    width, height = landscape(letter)
    margin = inch
    x = margin
    y = height - margin

    # Set the font for the canvas
    c.setFont(font_name, 12)  # Using size 12 as an example, adjust as needed

    for word in words:
        c.drawString(x, y, word)
        y -= 20  # Yeni satır için yüksekliği azalt.
        if y <= margin:  # Sayfa sonuna gelindiğinde yeni sayfa ekleyin.
            c.showPage()
            y = height - margin

    c.save()


if __name__ == "__main__":
    input_file = "kelimeler.txt"
    output_file = "script2-çıktı.pdf"
    words = read_from_txt(input_file)
    write_to_pdf(words, output_file)
