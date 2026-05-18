import json
import hashlib

def consolidate_rss(entries):
    seen = set()
    unique_entries = []
    for entry in entries:
        # Hash du titre + contenu pour éviter les doublons subtils
        key = hashlib.md5((entry.get('title', '') + entry.get('content', '')).encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            unique_entries.append(entry)
    return unique_entries

if __name__ == '__main__':
    print('RSS Consolidator v4 ready')