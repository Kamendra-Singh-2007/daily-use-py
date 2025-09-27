import os, sys, re
from urllib.parse import urlparse

def base_url(u):
    i = u.rfind('/')
    return u[:i+1]

def fix_file(m3u8_path, base):
    with open(m3u8_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out = []
    for line in lines:
        t = line.strip()
        if not t or t.startswith('#') or re.match(r'^https?://', t):
            out.append(line)
        else:
            out.append(base + t + '\n')
    fixed_path = m3u8_path.replace('.m3u8', '_fixed.m3u8')
    with open(fixed_path, 'w', encoding='utf-8') as f:
        f.writelines(out)
    return fixed_path

def main():
    if len(sys.argv) < 2:
        print('usage: python aria_fix.py <m3u8_url>')
        sys.exit(1)
    url = sys.argv[1]
    name = os.path.basename(urlparse(url).path) or 'playlist.m3u8'
    
    # Download with aria2c
    os.system(f'aria2c -q -o "{name}" "{url}"')
    
    # Fix URLs
    base = base_url(url)
    fixed = fix_file(name, base)
    
    # Delete original and rename fixed to original name
    os.system(f'del "{name}"')
    os.system(f'ren "{fixed}" "{name}"')
    
    # Print ffmpeg command
    mp4_name = name.replace('.m3u8', '.mp4')
    print(f"""

ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto,data -allowed_extensions ALL -i "{name}" -c copy "{mp4_name}"

ffplay -protocol_whitelist file,http,https,tcp,tls,crypto,data "{name}"
""")

if __name__ == '__main__':
    main()
