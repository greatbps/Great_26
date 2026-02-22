import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json
from datetime import datetime, timedelta

# 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = '28b91fdccad3809ca3d1cf7348e118dc'
BASE_PATH = r'C:\공유\Great_26\00_INBOX'
LAST_SYNC_FILE = r'C:\공유\Great_26\last_sync.txt'

HEADERS = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

def get_prop_text(prop):
    if not prop: return ""
    p_type = prop.get('type')
    if p_type == 'title':
        return prop['title'][0].get('plain_text', '') if prop['title'] else ""
    elif p_type == 'rich_text':
        return "".join([t.get('plain_text', '') for t in prop['rich_text']])
    elif p_type == 'select':
        return prop['select'].get('name', '') if prop['select'] else ""
    elif p_type == 'multi_select':
        return ", ".join([m.get('name', '') for m in prop['multi_select']])
    elif p_type == 'url':
        return prop.get('url', '') or ""
    elif p_type == 'date':
        return prop['date'].get('start', '') if prop['date'] else ""
    return ""

def get_page_content(page_id):
    url = f'https://api.notion.com/v1/blocks/{page_id}/children'
    response = requests.get(url, headers=HEADERS)
    blocks = response.json().get('results', [])
    content = ''
    for block in blocks:
        b_type = block.get('type')
        if b_type in ['paragraph', 'heading_1', 'heading_2', 'heading_3', 'bulleted_list_item', 'numbered_list_item']:
            data = block.get(b_type)
            if data and 'rich_text' in data:
                content += ''.join([p.get('plain_text', '') for p in data['rich_text']]) + '\n'
    return content

def judge_category(title, content):
    text = (title + content).lower()
    if any(k in text for k in ['코딩', '개발', 'python', 'git', 'ai']): return 'Development'
    if any(k in text for k in ['경제', '주식', '투자', '돈']): return 'Finance'
    return 'General'

def main():
    if not os.path.exists(BASE_PATH): os.makedirs(BASE_PATH)
    # 전체 다시 가져오기 위해 필터 시간 조정
    last_sync = "2020-01-01T00:00:00.000Z" 
    
    url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'
    response = requests.post(url, headers=HEADERS, json={'filter': {'timestamp': 'last_edited_time', 'last_edited_time': {'after': last_sync}}})
    pages = response.json().get('results', [])
    
    print(f"Syncing {len(pages)} pages...")

    for page in pages:
        props = page.get('properties', {})
        
        # 1. 제목 가져오기
        title = get_prop_text(props.get('Name') or props.get('Title') or props.get('제목')) or "Untitled"
        
        # 2. 기존 카테고리 확인 (없으면 AI 판단)
        category = get_prop_text(props.get('Category') or props.get('카테고리'))
        if not category:
            content_sample = get_page_content(page['id'])[:500]
            category = judge_category(title, content_sample)
        
        # 3. 기존 요약 확인 (없으면 자동 생성)
        summary = get_prop_text(props.get('Summary') or props.get('요약'))
        content = get_page_content(page['id'])
        if not summary:
            summary = content[:200].replace('\n', ' ')
        
        # 4. 파일 저장 경로 설정
        cat_path = os.path.join(BASE_PATH, category)
        if not os.path.exists(cat_path): os.makedirs(cat_path)
        
        safe_title = "".join([c for c in title if c not in r'\/:*?"<>|']).strip()[:50]
        file_path = os.path.join(cat_path, f"{safe_title}.md")
        
        # 5. DB 구조를 반영한 파일 작성
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write("## 📋 Metadata\n")
            for key, val in props.items():
                text_val = get_prop_text(val)
                if text_val and key not in [title, 'Summary', '요약', 'Category', '카테고리']:
                    f.write(f"- **{key}:** {text_val}\n")
            f.write(f"- **Notion URL:** {page.get('url')}\n\n")
            
            f.write(f"## 📝 Summary\n{summary}\n\n")
            f.write(f"## 📄 Content\n{content}")
            
        print(f"Processed: {title} -> {category}")

if __name__ == "__main__":
    main()

