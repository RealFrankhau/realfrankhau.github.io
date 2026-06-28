from pathlib import Path
import re
p = Path('index_beat.html')
text = p.read_text(encoding='utf-8')
replacements = [
    (r'data-midi="([^"]+?)\.mid"', r'data-midi="\1.mp3"'),
    (r'href="([^"]+?)\.mid"', r'href="\1.mp3"'),
    (r'type="audio/midi"', 'type="audio/mpeg"'),
    (r"player\.canPlayType\('audio/midi'\)", 'player.canPlayType("audio/mpeg")'),
    (r"player\.canPlayType\('audio/x-midi'\)", 'player.canPlayType("audio/mpeg")'),
    (r"player\.canPlayType\('audio/mid'\)", 'player.canPlayType("audio/mpeg")'),
    ('常用節奏形態、撥奏符號和 MIDI 範例', '常用節奏形態、撥奏符號和 MP3 範例'),
    ('請按圖播放對應 MIDI 範例，無需下載檔案。', '請按圖播放對應 MP3 範例，無需下載檔案。'),
    ('附上的 MIDI 檔案來跟著學習。', '附上的 MP3 檔案來跟著學習。'),
    ('目前尚未播放任何 MIDI。', '目前尚未播放任何 MP3。'),
    ('此瀏覽器可能不支援直接播放 MIDI', '此瀏覽器可能不支援直接播放 MP3'),
    ('播放 MIDI 時遇到問題，請確認瀏覽器是否支援 MIDI 或直接下載檔案播放。', '播放 MP3 時遇到問題，請確認瀏覽器是否支援音訊播放或直接下載檔案播放。'),
    ('多聽 MIDI 範例，模仿不同曲風的伴奏型態。', '多聽 MP3 範例，模仿不同曲風的伴奏型態。'),
    (r'下載 ([^<]+?) MIDI', r'下載 \1 MP3'),
]
for pat, rep in replacements:
    text = re.sub(pat, rep, text)
p.write_text(text, encoding='utf-8')
print('updated')
