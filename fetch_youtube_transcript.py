import sys
import os

# Add the browser-cdp skill scripts to path
skill_dir = os.path.expanduser('~/Library/Application Support/QClaw/openclaw/config/skills/browser-cdp/scripts')
sys.path.insert(0, skill_dir)

from browser_launcher import BrowserLauncher, BrowserNeedsCDPError
from cdp_client import CDPClient
from page_snapshot import PageSnapshot
from browser_actions import BrowserActions
import time

# Step 1: Launch browser and get CDP connection
launcher = BrowserLauncher()
try:
    cdp_url = launcher.launch(browser='chrome', reuse_profile=True, wait_for_user=True)
except BrowserNeedsCDPError as e:
    print(f"⚠️ {e}")
    print("请按照上面的指引操作后，重新运行脚本")
    sys.exit(1)

# Step 2: Connect to CDP
client = CDPClient(cdp_url)
client.connect()

# Step 3: Check existing tabs for YouTube video
target_url = 'https://www.youtube.com/watch?v=bTA8sjgvA4c'
tabs = client.list_tabs()
tab = None
for t in tabs:
    if target_url in t['url']:
        tab = t
        break

if tab:
    print(f"🔍 找到已有标签页，复用: {tab['title']}")
    client.attach(tab['id'])
else:
    print(f"🌐 新开标签页访问: {target_url}")
    tab = client.create_tab(target_url)
    client.attach(tab['id'])

# Step 4: Wait for page to load
actions = BrowserActions(client, PageSnapshot(client))
actions.wait_for_load()
time.sleep(5)  # Extra wait for YouTube to load fully

# Step 5: Extract transcript by clicking "Show transcript"
print("📝 尝试提取视频字幕...")
snapshot = PageSnapshot(client)
tree = snapshot.accessibility_tree()

# Look for "..." more actions button
for line in tree.split('\n'):
    if '[e' in line and ('更多操作' in line or 'More actions' in line or '...' in line):
        ref = line.split('[')[1].split(']')[0]
        print(f"点击更多操作按钮: {ref}")
        actions.click_by_ref(ref)
        time.sleep(2)
        break

# Look for "Show transcript" option
tree = snapshot.accessibility_tree()
for line in tree.split('\n'):
    if '[e' in line and ('显示字幕' in line or 'Show transcript' in line):
        ref = line.split('[')[1].split(']')[0]
        print(f"点击显示字幕: {ref}")
        actions.click_by_ref(ref)
        time.sleep(3)
        break

# Extract transcript text
text = actions.evaluate("document.querySelector('#segments-container').innerText")
with open('youtube_transcript.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"✅ 字幕已保存到 youtube_transcript.txt，共 {len(text)} 字符")
