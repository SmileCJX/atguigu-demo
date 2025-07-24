from pdf2docx import Converter

def pdf_to_word(pdf_file_path, word_file_path):
    # 创建 Converter 对象
    cv = Converter(pdf_file_path)

    # 将 PDF 文件转换为 Word 文件
    cv.convert(word_file_path, start=0, end=None)

    # 关闭 Converter 对象
    cv.close()

# 示例用法
pdf_file_path = '/Users/caijunxiang/Documents/*.pdf'
word_file_path = '/Users/caijunxiang/Documents/*.docx'

pdf_to_word(pdf_file_path, word_file_path)
