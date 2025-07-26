## download and summarize links
import os
import requests
from pathlib import Path

SESSION_ID = os.environ.get("SESSION_ID")
destination_folder = Path("./reports")

def load_links(filename: str) -> list:
    """Load newline separated URLs from a file.

    Lines starting with '#' or empty lines are ignored.
    """
    links = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            links.append(line)
    return links

def download_record(url: str) -> str:
    """Download a single URL and return its text content."""
    session = requests.Session()
    if SESSION_ID:
        # attempt to use session cookie if provided
        session.cookies.set("sessionid", SESSION_ID)
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def build_summary(source: str, text: str) -> None:
    """Summarize the text and write it to a Markdown file."""
    destination_folder.mkdir(exist_ok=True)
    # naive summary: first 100 words
    words = text.split()
    summary = " ".join(words[:100])
    safe_name = source.replace("/", "_").replace(":", "_")
    out_file = destination_folder / f"{safe_name}.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Summary for {source}\n\n")
        f.write(summary)

def main():
    links = load_links("alexander-moyes.links")
    for link in links:
        print(f"Fetching {link}...")
        record = download_record(link)
        build_summary(link, record)

if __name__ == "__main__":
    main()
