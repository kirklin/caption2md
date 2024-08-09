import pysrt
import os


def srt_to_readable_markdown(srt_file_path, md_file_path):
    # 读取 SRT 文件
    subs = pysrt.open(srt_file_path)

    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        # 写入文件开头的标题
        md_file.write(f"# {os.path.basename(md_file_path).replace('.md', '')}\n\n")

        # 写入字幕文本，去掉时间戳
        for sub in subs:
            # 写入字幕文本
            md_file.write(f"{sub.text}\n\n")


def batch_rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".srt") and "（自动生成）" in filename:
            srt_file_path = os.path.join(directory, filename)
            new_file_name = filename.replace("（自动生成）", "")
            new_srt_file_path = os.path.join(directory, new_file_name)

            # 仅在原路径和新路径不同的情况下才执行重命名
            if srt_file_path != new_srt_file_path:
                os.rename(srt_file_path, new_srt_file_path)
                print(f"Renamed {srt_file_path} to {new_srt_file_path}")

    # 创建标志文件
    flag_file_path = os.path.join(directory, 'processing_done.flag')
    with open(flag_file_path, 'w', encoding='utf-8') as flag_file:
        flag_file.write('SRT files have been processed.')


def convert_srt_files_in_directory(directory):
    # 首先批量重命名文件
    batch_rename_files(directory)

    # 然后转换文件
    for filename in os.listdir(directory):
        if filename.endswith(".srt"):
            srt_file_path = os.path.join(directory, filename)
            md_file_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '.md')
            srt_to_readable_markdown(srt_file_path, md_file_path)
            print(f"Converted {srt_file_path} to Markdown")


# 修改为你的 SRT 文件所在的目录
srt_directory = './srt'
convert_srt_files_in_directory(srt_directory)
