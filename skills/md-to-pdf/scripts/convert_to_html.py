
import markdown
import sys
import os

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    css = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.7;
            color: #2d3748;
            font-size: 15px;
            margin: 0;
            padding: 0;
        }
        .content {
            max-width: 800px;
            margin: 40px auto;
            padding: 40px 20px 60px 20px;
            page-break-before: always;
        }
        h1, h2, h3, h4 { color: #1a202c; margin-top: 1.6em; line-height: 1.35; }
        h1 { font-size: 1.9em; font-weight: 800; border-bottom: 3px solid #e2e8f0; padding-bottom: 0.4em; }
        h2 { font-size: 1.35em; font-weight: 700; border-bottom: 1px solid #edf2f7; padding-bottom: 0.25em; }
        h3 { font-size: 1.1em; font-weight: 700; color: #2b6cb0; }
        h4 { font-size: 1em; font-weight: 600; color: #4a5568; }
        blockquote {
            border-left: 4px solid #4299e1;
            padding: 12px 20px;
            color: #4a5568;
            font-style: italic;
            margin: 1.5em 0;
            background: #ebf8ff;
            border-radius: 0 6px 6px 0;
        }
        code {
            background: #edf2f7; padding: 0.2em 0.4em;
            border-radius: 3px; font-size: 0.88em; color: #c53030;
        }
        hr { border: 0; border-top: 1px solid #e2e8f0; margin: 2em 0; }
        ul, ol { padding-left: 2em; }
        li { margin-bottom: 0.4em; }
        table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.93em; }
        th { background: #2d3748; color: #fff; padding: 10px 14px; text-align: left; font-weight: 600; }
        td { padding: 9px 14px; border-bottom: 1px solid #e2e8f0; }
        tr:nth-child(even) td { background: #f7fafc; }
        img { max-width: 100%; height: auto; display: block; margin: 2em auto; border-radius: 8px;
              box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }

        /* ── Print fix ── */
        * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
        /* ── Cover page ── */
        .cover-page {
            page-break-after: always;
            min-height: 100vh;
            background-color: #0d1b3e;
            background: linear-gradient(150deg, #060d1f 0%, #0d1b3e 40%, #0a2a52 70%, #0e3d6e 100%);
            color: #fff;
            padding: 0;
            box-sizing: border-box;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        /* Decorative circles */
        .cover-page::before {
            content: '';
            position: absolute; top: -140px; right: -100px;
            width: 520px; height: 520px; border-radius: 50%;
            background: radial-gradient(circle, rgba(56,189,248,0.10) 0%, transparent 65%);
        }
        .cover-page::after {
            content: '';
            position: absolute; bottom: -100px; left: -80px;
            width: 400px; height: 400px; border-radius: 50%;
            background: radial-gradient(circle, rgba(99,102,241,0.10) 0%, transparent 65%);
        }

        /* Top ribbon */
        .cover-top-ribbon {
            background: rgba(56,189,248,0.08);
            border-bottom: 1px solid rgba(56,189,248,0.15);
            padding: 14px 56px;
            display: flex;
            align-items: center;
            gap: 12px;
            position: relative;
            z-index: 2;
        }
        .cover-ribbon-dot {
            width: 8px; height: 8px; border-radius: 50%;
            background: #38bdf8;
            box-shadow: 0 0 10px rgba(56,189,248,0.7);
        }
        .cover-ribbon-text {
            font-size: 0.72em; font-weight: 700;
            letter-spacing: 0.18em; text-transform: uppercase;
            color: #7dd3fc;
        }

        /* Main content area */
        .cover-body {
            flex: 1;
            padding: 52px 56px 44px;
            position: relative; z-index: 2;
            display: flex; flex-direction: column;
        }
        .cover-eyebrow {
            font-size: 0.75em; font-weight: 600;
            letter-spacing: 0.12em; text-transform: uppercase;
            color: rgba(56,189,248,0.7);
            margin-bottom: 20px;
        }
        .cover-title {
            font-size: 2.1em; font-weight: 800; line-height: 1.25;
            color: #fff; margin: 0 0 32px 0; max-width: 680px;
            letter-spacing: -0.01em;
        }
        .cover-meta-row {
            display: flex; align-items: center; gap: 20px;
            margin-bottom: 40px; flex-wrap: wrap;
        }
        .cover-tag {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.12);
            color: rgba(255,255,255,0.6);
            font-size: 0.73em; font-weight: 500;
            padding: 4px 12px; border-radius: 20px;
            letter-spacing: 0.04em;
        }
        .cover-url-chip {
            display: flex; align-items: center; gap: 8px;
            background: rgba(56,189,248,0.08);
            border: 1px solid rgba(56,189,248,0.2);
            border-radius: 6px;
            padding: 8px 14px;
            margin-bottom: 36px;
            max-width: fit-content;
        }
        .cover-url-icon { font-size: 0.85em; }
        .cover-url-text {
            font-size: 0.78em; color: #7dd3fc;
            font-family: monospace; word-break: break-all;
        }

        /* Divider line */
        .cover-rule {
            width: 100%; height: 1px;
            background: linear-gradient(90deg, rgba(56,189,248,0.3), transparent);
            margin: auto 0 32px;
        }

        /* GitHub project card at bottom */
        .cover-gh-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 12px;
            padding: 20px 24px;
            display: flex;
            align-items: center;
            gap: 20px;
            position: relative; z-index: 2;
            margin: 0 56px 44px;
        }
        .cover-gh-icon-wrap {
            background: rgba(56,189,248,0.12);
            border: 1px solid rgba(56,189,248,0.25);
            border-radius: 10px;
            width: 44px; height: 44px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.3em; flex-shrink: 0;
        }
        .cover-gh-info { flex: 1; }
        .cover-gh-label {
            font-size: 0.65em; text-transform: uppercase;
            letter-spacing: 0.12em; color: rgba(255,255,255,0.35);
            margin-bottom: 4px;
        }
        .cover-gh-name {
            font-size: 0.95em; font-weight: 700; color: #e2e8f0;
            margin-bottom: 3px;
        }
        .cover-gh-url {
            font-size: 0.78em; color: #38bdf8; font-family: monospace;
        }
        .cover-gh-badge {
            background: rgba(56,189,248,0.12);
            border: 1px solid rgba(56,189,248,0.3);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.68em; font-weight: 700;
            color: #7dd3fc; letter-spacing: 0.08em;
            text-transform: uppercase; white-space: nowrap;
        }

        /* Author card at bottom */
        .cover-author-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 12px;
            padding: 20px 24px;
            display: flex;
            align-items: center;
            gap: 20px;
            position: relative; z-index: 2;
            margin: 0 56px 44px;
        }
        .cover-author-icon {
            background: rgba(56,189,248,0.12);
            border: 1px solid rgba(56,189,248,0.25);
            border-radius: 10px;
            width: 44px; height: 44px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.3em; flex-shrink: 0;
        }
        .cover-author-info { flex: 1; }
        .cover-author-label {
            font-size: 0.65em; text-transform: uppercase;
            letter-spacing: 0.12em; color: rgba(255,255,255,0.35);
            margin-bottom: 4px;
        }
        .cover-author-name {
            font-size: 0.95em; font-weight: 700; color: #e2e8f0;
            margin-bottom: 3px;
        }
        .cover-author-contact {
            font-size: 0.78em; color: #38bdf8; font-family: monospace;
        }
        .cover-author-divider {
            width: 1px; height: 50px;
            background: rgba(255,255,255,0.15);
            margin: 0 10px;
        }
        .cover-gh-info { flex: 1; }
        .cover-gh-label {
            font-size: 0.65em; text-transform: uppercase;
            letter-spacing: 0.12em; color: rgba(255,255,255,0.35);
            margin-bottom: 4px;
        }
        .cover-gh-name {
            font-size: 0.9em; font-weight: 700; color: #e2e8f0;
            margin-bottom: 3px;
        }
        .cover-gh-url {
            font-size: 0.72em; color: #38bdf8; font-family: monospace;
        }

        @page { margin: 0; }
        @page :first { margin: 0; }
        @media print {
            .cover-page { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            .content { padding: 40px 40px 60px 40px; }
        }
    </style>
    """

    # Extract title (first H1) and video URL (first line if URL)
    lines = text.strip().split('\n')
    video_url = ''
    doc_title = os.path.splitext(os.path.basename(md_file))[0]

    if lines and lines[0].startswith('http'):
        video_url = lines[0].strip()

    for line in lines:
        if line.startswith('# '):
            doc_title = line[2:].strip()
            break

    url_chip = f"""<div class="cover-url-chip">
        <span class="cover-url-icon">&#x1F4CE;</span>
        <span class="cover-url-text">{video_url}</span>
    </div>""" if video_url else ""

    cover_html = f"""
<div class="cover-page">
    <div class="cover-top-ribbon">
        <div class="cover-ribbon-dot"></div>
        <div class="cover-ribbon-text">AI 访谈深度精译系列 &nbsp;&bull;&nbsp; AI Interview Intelligence Series</div>
    </div>
    <div class="cover-body">
        <div class="cover-eyebrow">Deep-Dive Summary &nbsp;&middot;&nbsp; 全景时间轴版</div>
        <h1 class="cover-title">{doc_title}</h1>
        <div class="cover-meta-row">
            <span class="cover-tag">&#x2728; 证据驱动</span>
            <span class="cover-tag">&#x1F4AC; 原话引用</span>
            <span class="cover-tag">&#x1F1E8;&#x1F1F3; 精准翻译</span>
            <span class="cover-tag">&#x1F4C8; 客观无演绎</span>
        </div>
        {url_chip}
        <div class="cover-rule"></div>
    </div>
    <div class="cover-author-card">
        <div class="cover-author-icon">&#x270D;</div>
        <div class="cover-author-info">
            <div class="cover-author-label">Author &nbsp;&bull;&nbsp; 作者</div>
            <div class="cover-author-name">Max. Zheng</div>
            <div class="cover-author-contact">WeChat: 18910305078</div>
        </div>
        <div class="cover-author-divider"></div>
        <div class="cover-gh-info">
            <div class="cover-gh-label">Open Source Project</div>
            <div class="cover-gh-name">youtube-interview-summarizer</div>
            <div class="cover-gh-url">github.com/max-tutu-dev/youtube-interview-summarizer</div>
        </div>
    </div>
</div>
"""

    html = markdown.markdown(text, extensions=['extra', 'codehilite', 'tables'])
    full_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  {css}
</head>
<body>
{cover_html}
<div class="content">
{html}
</div>
</body>
</html>"""

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 convert.py input.md output.html")
        sys.exit(1)
    convert_md_to_html(sys.argv[1], sys.argv[2])
