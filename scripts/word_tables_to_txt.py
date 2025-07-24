from docx import Document

def word_tables_to_txt(word_path, txt_path):
    """
    从Word文档中提取所有表格内容，并写入TXT文件
    :param word_path: Word文件路径（.docx格式）
    :param txt_path: 输出的TXT文件路径
    """
    # 读取Word文档
    doc = Document(word_path)

    with open(txt_path, 'w', encoding='utf-8') as f:
        # 遍历所有表格
        for table in doc.tables:
            for row in table.rows:
                # 获取每行的单元格内容
                row_text = [cell.text.strip() for cell in row.cells]
                # 用制表符分隔单元格内容并写入文件
                f.write('\t'.join(row_text) + '\n')
            # 表格之间用分隔线区分
            f.write('-' * 50 + '\n')

    print(f"表格内容已成功导出到 {txt_path}")






# 基础使用示例
word_tables_to_txt('1、福建省三医一张网_数据采集标准规范 就诊概要分册.docx', 'output.txt')