#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple page generator using string concatenation
"""
import json
import os

# Load data
with open('website_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ru_chapters = data['ru']['chapters']
en_chapters = data['en']['chapters']

os.makedirs('docs/ru', exist_ok=True)
os.makedirs('docs/en', exist_ok=True)

# Build pages for Russian
print("Creating Russian pages...")
for i, chapter in enumerate(ru_chapters):
    # Find prev/next
    prev_num = ru_chapters[i-1]['number'] if i > 0 else None
    next_num = ru_chapters[i+1]['number'] if i < len(ru_chapters)-1 else None
    
    html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>""" + chapter['title'] + """ - Дубай RERA Broker 2025</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; line-height: 1.6; }
        header { background: #2c3e50; color: white; padding: 20px; margin-bottom: 30px; }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        .nav { margin: 20px 0; }
        .nav a { background: #3498db; color: white; padding: 10px 20px; text-decoration: none; margin: 5px; border-radius: 5px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 12px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <header>
        <h1>Дубай RERA Broker 2025: от нуля до сделок</h1>
        <div>
            <a href="index.html">Оглавление</a>
            <a href="../en/chapter-""" + chapter['number'] + """.html">English</a>
        </div>
    </header>
    
    <div class="nav">"""
    
    if prev_num:
        html += '<a href="chapter-' + prev_num + '.html">← Предыдущая</a>'
    html += '<a href="index.html">Главная</a>'
    if next_num:
        html += '<a href="chapter-' + next_num + '.html">Следующая →</a>'
    
    html += """    </div>
    
    <article>"""
    
    # Add chapter sections
    for section in chapter.get('sections', []):
        html += '<div id="' + section['id'] + '">'
        html += '<h2>' + section['title'] + '</h2>'
        html += section['content']
        html += '</div>'
    
    html += """    </article>
    
    <div class="nav">"""
    
    if prev_num:
        html += '<a href="chapter-' + prev_num + '.html">← Предыдущая</a>'
    html += '<a href="index.html">Главная</a>'
    if next_num:
        html += '<a href="chapter-' + next_num + '.html">Следующая →</a>'
    
    html += """    </div>
</body>
</html>"""
    
    with open(f"docs/ru/chapter-{chapter['number']}.html", 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Created chapter {chapter['number']}")

# Build TOC for Russian
toc_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Оглавление - Дубай RERA Broker 2025</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: #2c3e50; color: white; padding: 30px; margin-bottom: 40px; }
        h1 { margin: 0; }
        .toc { list-style: none; padding: 0; }
        .toc li { margin: 10px 0; }
        .toc a { display: block; padding: 15px; background: #f8f9fa; color: #2c3e50; text-decoration: none; border-left: 4px solid #3498db; }
        .toc a:hover { background: #e3f2fd; }
    </style>
</head>
<body>
    <header>
        <h1>Оглавление</h1>
        <p>Дубай RERA Broker 2025: от нуля до сделок</p>
        <a href="../en/index.html" style="color: white;">English</a>
    </header>
    <ul class="toc">"""

for chapter in ru_chapters:
    toc_html += '<li><a href="chapter-' + chapter['number'] + '.html">Глава ' + chapter['number'] + ': ' + chapter['title'] + '</a></li>'

toc_html += """    </ul>
</body>
</html>"""

with open('docs/ru/index.html', 'w', encoding='utf-8') as f:
    f.write(toc_html)

print("Created Russian TOC")

# Similar for English
print("\nCreating English pages...")
for i, chapter in enumerate(en_chapters):
    prev_num = en_chapters[i-1]['number'] if i > 0 else None
    next_num = en_chapters[i+1]['number'] if i < len(en_chapters)-1 else None
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>""" + chapter['title'] + """ - Dubai RERA Broker 2025</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; line-height: 1.6; }
        header { background: #2c3e50; color: white; padding: 20px; margin-bottom: 30px; }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        .nav { margin: 20px 0; }
        .nav a { background: #3498db; color: white; padding: 10px 20px; text-decoration: none; margin: 5px; border-radius: 5px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 12px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <header>
        <h1>Dubai RERA Broker 2025: from zero to deal</h1>
        <div>
            <a href="index.html">Table of Contents</a>
            <a href="../ru/chapter-""" + chapter['number'] + """.html">Русский</a>
        </div>
    </header>
    
    <div class="nav">"""
    
    if prev_num:
        html += '<a href="chapter-' + prev_num + '.html">← Previous</a>'
    html += '<a href="index.html">Home</a>'
    if next_num:
        html += '<a href="chapter-' + next_num + '.html">Next →</a>'
    
    html += """    </div>
    
    <article>"""
    
    for section in chapter.get('sections', []):
        html += '<div id="' + section['id'] + '">'
        html += '<h2>' + section['title'] + '</h2>'
        html += section['content']
        html += '</div>'
    
    html += """    </article>
    
    <div class="nav">"""
    
    if prev_num:
        html += '<a href="chapter-' + prev_num + '.html">← Previous</a>'
    html += '<a href="index.html">Home</a>'
    if next_num:
        html += '<a href="chapter-' + next_num + '.html">Next →</a>'
    
    html += """    </div>
</body>
</html>"""
    
    with open(f"docs/en/chapter-{chapter['number']}.html", 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Created chapter {chapter['number']}")

# Build TOC for English
toc_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Table of Contents - Dubai RERA Broker 2025</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: #2c3e50; color: white; padding: 30px; margin-bottom: 40px; }
        h1 { margin: 0; }
        .toc { list-style: none; padding: 0; }
        .toc li { margin: 10px 0; }
        .toc a { display: block; padding: 15px; background: #f8f9fa; color: #2c3e50; text-decoration: none; border-left: 4px solid #3498db; }
        .toc a:hover { background: #e3f2fd; }
    </style>
</head>
<body>
    <header>
        <h1>Table of Contents</h1>
        <p>Dubai RERA Broker 2025: from zero to deal</p>
        <a href="../ru/index.html" style="color: white;">Русский</a>
    </header>
    <ul class="toc">"""

for chapter in en_chapters:
    toc_html += '<li><a href="chapter-' + chapter['number'] + '.html">Chapter ' + chapter['number'] + ': ' + chapter['title'] + '</a></li>'

toc_html += """    </ul>
</body>
</html>"""

with open('docs/en/index.html', 'w', encoding='utf-8') as f:
    f.write(toc_html)

print("Created English TOC")
print("\n=== Website generated successfully! ===")
print("Open docs/ru/index.html or docs/en/index.html")

