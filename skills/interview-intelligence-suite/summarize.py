#!/usr/bin/env python3
"""
YouTube访谈视频摘要全链路脚本
功能：输入YouTube链接/本地字幕文件 → 提取字幕 → 按V7规则生成摘要 → 输出品牌化PDF
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path

# 配置路径
FETCH_SCRIPT = "/Users/tutuzheng/.qclaw/workspace/fetch_youtube_transcript.py"
VIDEO_SUMMARY_SKILL = "/Users/tutuzheng/.qclaw/workspace/skills/video-summary"
MD_TO_PDF_SKILL = "/Users/tutuzheng/.qclaw/workspace/skills/md-to-pdf"
OUTPUT_DIR = os.path.expanduser("~/Downloads/YouTubeSummaries")
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def run_command(cmd, desc="执行命令"):
    """运行命令并返回结果"""
    print(f"[+] {desc}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[!] 失败：{result.stderr}")
            return None
        return result.stdout.strip()
    except Exception as e:
        print(f"[!] 错误：{str(e)}")
        return None

def fetch_youtube_transcript(url):
    """提取YouTube字幕"""
    print(f"[+] 提取YouTube字幕：{url}")
    output_file = os.path.join(OUTPUT_DIR, f"transcript_{Path(url).name}.txt")
    cmd = f"python3 {FETCH_SCRIPT} {url} --output {output_file}"
    result = run_command(cmd, "提取字幕")
    if result and os.path.exists(output_file):
        print(f"[✓] 字幕已保存到：{output_file}")
        return output_file
    return None

def generate_summary(transcript_file):
    """按V7规则生成摘要"""
    print(f"[+] 生成视频摘要：{transcript_file}")
    base_name = Path(transcript_file).stem.replace("transcript_", "")
    output_md = os.path.join(OUTPUT_DIR, f"{base_name}_summary.md")
    
    # 调用video-summary skill生成摘要
    with open(transcript_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 加载V7规则
    with open(os.path.join(VIDEO_SUMMARY_SKILL, "summary_guidelines.md"), 'r', encoding='utf-8') as f:
        guidelines = f.read()
    
    # 调用大模型生成摘要
    prompt = f"""
    请严格按照以下规则生成视频摘要：
    {guidelines}
    
    视频字幕内容：
    {content[:100000]}  # 限制长度避免超过上下文
    """
    
    # 这里实际调用大模型API，暂时用占位符
    summary_content = f"""# YouTube视频摘要
    （此处为按V7规则生成的摘要内容）
    """
    
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print(f"[✓] 摘要已保存到：{output_md}")
    return output_md

def convert_to_pdf(md_file):
    """转换为品牌化PDF"""
    print(f"[+] 转换为PDF：{md_file}")
    output_pdf = md_file.replace(".md", ".pdf")
    cmd = f"python3 {os.path.join(MD_TO_PDF_SKILL, 'scripts/convert_to_html.py')} {md_file} --output {output_pdf}"
    result = run_command(cmd, "转换PDF")
    if result and os.path.exists(output_pdf):
        print(f"[✓] PDF已生成：{output_pdf}")
        return output_pdf
    return None

def main():
    parser = argparse.ArgumentParser(description="YouTube访谈视频摘要全链路工具")
    parser.add_argument("input", help="YouTube链接或本地字幕文件路径")
    parser.add_argument("--only-md", action="store_true", help="只生成Markdown摘要，不转PDF")
    parser.add_argument("--only-pdf", action="store_true", help="输入为Markdown文件，只转PDF")
    parser.add_argument("--output", "-o", help="指定输出目录")
    
    args = parser.parse_args()
    
    if args.output:
        global OUTPUT_DIR
        OUTPUT_DIR = args.output
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    # 场景1：输入是Markdown文件，只转PDF
    if args.only_pdf and args.input.endswith(".md"):
        pdf_file = convert_to_pdf(args.input)
        if pdf_file:
            print(f"\n🎉 处理完成！PDF文件：{pdf_file}")
        return
    
    # 场景2：输入是YouTube链接
    if args.input.startswith("http"):
        transcript_file = fetch_youtube_transcript(args.input)
        if not transcript_file:
            print("[!] 字幕提取失败")
            sys.exit(1)
    else:
        # 输入是本地字幕文件
        transcript_file = args.input
        if not os.path.exists(transcript_file):
            print(f"[!] 文件不存在：{transcript_file}")
            sys.exit(1)
    
    # 生成摘要
    md_file = generate_summary(transcript_file)
    if not md_file:
        print("[!] 摘要生成失败")
        sys.exit(1)
    
    # 是否转PDF
    if not args.only_md:
        pdf_file = convert_to_pdf(md_file)
        if pdf_file:
            print(f"\n🎉 全部处理完成！最终PDF：{pdf_file}")
    else:
        print(f"\n🎉 处理完成！摘要文件：{md_file}")

if __name__ == "__main__":
    main()
