import pdfplumber
from gtts import gTTS


def get_pdf_text(pdf_file_path):
    pages_text = ''
    with pdfplumber.open(pdf_file_path) as pdf:
        pages_text = ''.join([page.extract_text() for page in pdf.pages])
        pages_text_cleaned = pages_text.replace("\n", "")
    return pages_text_cleaned


def create_pdf_audio(pdf_text, language='ru', output_file='output.mp3'):
    audio = gTTS(text=pdf_text, lang=language)
    audio.save(output_file)


def main():
    pdf_file_path = 'text.pdf'
    pdf_text = get_pdf_text(pdf_file_path)
    create_pdf_audio(pdf_text)


if __name__ == '__main__':
    main()
