from bs4 import BeautifulSoup

# Try reading with different encodings
content = ""
encodings = ["utf-16", "utf-8", "latin-1", "cp1252"]

for enc in encodings:
    try:
        with open("temp_course.html", "r", encoding=enc) as f:
            content = f.read()
        print(f"Successfully read with encoding: {enc}")
        break
    except Exception as e:
        print(f"Failed with {enc}: {e}")

if not content:
    print("Could not read file.")
    exit()

soup = BeautifulSoup(content, "html.parser")

print(f"Page Title: {soup.title.string if soup.title else 'No title'}")

# Find articles
articles = soup.find_all("article")
print(f"Found {len(articles)} articles.")

for article in articles:
    title_tag = article.find("h2", class_="entry-title")
    if title_tag:
        link = title_tag.find("a")
        if link:
            print(f"Title: {link.text.strip()}")
            print(f"Link: {link['href']}")
            print("-" * 20)
