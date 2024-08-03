import PyPDF2
import jaconv

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)  # PdfReaderを使用
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# 特定の平仮名をカタカナに変換する関数
def convert_specific_hiragana_to_katakana(text):
    conversions = {
        "りんご": "リンゴ",
        "らーめん": "ラーメン"
    }
    for hiragana, katakana in conversions.items():
        text = text.replace(hiragana, katakana)
    return text

# メインの処理
if __name__ == "__main__":
    pdf_file = "sample1.pdf"
    extracted_text = extract_text_from_pdf(pdf_file)
    # 特定の単語をカタカナに変換
    converted_text = convert_specific_hiragana_to_katakana(extracted_text)
    print(converted_text)