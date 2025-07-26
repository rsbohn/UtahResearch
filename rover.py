## download and summarize links
import os

SESSION_ID=os.environ.get("SESSION_ID")
destination_folder = "./reports"

def load_links(filename) -> list:
  pass

def download_record(url) -> str:
  pass

def build_summary(source, text):
  """Summarise the text, save in a markdown file."""
  pass

def main():
  links = load_links("alex-moyes.links")
  for link in links:
    print("Fetching {link}...")
    record = download_record(link)
    build_summary(link, record)
