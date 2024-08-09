import os
import google.generativeai as genai

# 配置 API 密钥
api_key = ''  # 替换为您的 Gemini API 密钥
genai.configure(api_key=api_key)


def generate_course_outline(content, processed_content, part_number):
    # 设置 API 生成模型
    model = genai.GenerativeModel("gemini-1.5-pro")

    # 生成文本内容
    response = model.generate_content(
        f"""
1. 初步阅读
   - 通读整个演讲稿
2. 结构化整理
   - 使用Markdown标题语法(#, ##, ###)整理完整的课程讲义
   - 使用嵌套列表组织内容，确保层级清晰
   - 如有多个主题，使用颜色标记语法区分

3. 突出关键信息
   - 使用代码块(```)标注重要概念或引用
   - 对核心观点使用加粗(**文本**)或斜体(*文本*)
   - 使用表格或分隔线(---)突出统计数据

请确保生成的内容是原始讲义的完整整理版本，涵盖所有原始内容，而不是精简版。确保生成内容有明确的逻辑流和适当的标点符号，便于书面阅读。

当前处理的内容部分（第 {part_number} 部分）：
{content}

已经处理过的内容：
{processed_content}
        """,
        generation_config=genai.GenerationConfig(
            max_output_tokens=8192,  # 根据需要调整输出长度
            temperature=0.5,  # 控制输出的创意程度
        )
    )

    return response.text


def process_markdown_file(input_file_path, output_file_path):
    # 读取原始 Markdown 文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 生成的内容部分
    formatted_parts = []
    chunk_size = 8192  # 根据 API 限制设置的分段大小
    processed_content = ""

    for i in range(0, len(content), chunk_size):
        part_content = content[i:i + chunk_size]
        print(f"Processing content from {i} to {i + chunk_size}")
        formatted_content = generate_course_outline(part_content, processed_content, i // chunk_size + 1)
        formatted_parts.append(formatted_content)
        processed_content += part_content  # 更新已处理过的内容

    # 将所有部分合并
    complete_content = "\n\n".join(formatted_parts)

    # 写入到新的 Markdown 文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(complete_content)

    print(f"Processed content saved to {output_file_path}")


def process_all_markdown_files(directory):
    # 遍历目录下的所有 Markdown 文件
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            input_file_path = os.path.join(directory, filename)
            output_file_path = os.path.join(directory, filename.replace(".md", ".ai.md"))
            process_markdown_file(input_file_path, output_file_path)


# 修改为您的 Markdown 文件所在的目录
md_directory = './md'
process_all_markdown_files(md_directory)
