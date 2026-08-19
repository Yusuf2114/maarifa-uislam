import os
import json

BOOKS = [
    "bukhari", "muslim", "nasai", "dawud", "tirmidhi", "majha",
    "nawawi", "malik", "ahmad", "darimi", "mishkat",
    "riyadussalihin", "aladab", "bulugh", "shamail", "qudsi", "hisn"
]

def find_hadith_dir(book):
    """Inatafuta folda ya hadithi iwe imeitwa 'hadith' au 'hadiths'."""
    for possible_name in ["hadith", "hadiths"]:
        path = os.path.join(book, possible_name)
        if os.path.isdir(path):
            return path
    return None

def build_manifest():
    manifest = {}

    for book in BOOKS:
        if not os.path.isdir(book):
            print(f"[SKIP] Folda ya '{book}' haipo, inarukwa.")
            continue

        book_entry = {"books": {"version": 1}, "files": {}}

        hadith_dir = find_hadith_dir(book)
        if hadith_dir:
            for filename in os.listdir(hadith_dir):
                if filename.endswith(".json"):
                    file_id = filename.replace(".json", "")
                    book_entry["files"][file_id] = {"version": 1}
        else:
            print(f"[WARN] '{book}': folda ya hadith/hadiths haikupatikana.")

        manifest[book] = book_entry
        print(f"[OK] {book}: fileId {len(book_entry['files'])} zimeongezwa.")

    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("\n✅ manifest.json imetengenezwa kikamilifu!")

if __name__ == "__main__":
    build_manifest()