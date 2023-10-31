import wikipediaapi
import re

wiki_wiki = wikipediaapi.Wikipedia(
    language='pl',
    user_agent='Your-User-Agent-Name'
)

# Replace 'Układ Słoneczny' with the title of the page you want to fetch
page_title = 'Układ Słoneczny'

page = wiki_wiki.page(page_title)
if page.exists():
    # Get the content
    page_content = page.text

    # Replace hyphens, double commas, brackets, and all non-alphanumeric characters
    page_content = re.sub(r'[-(),;.\[\]{}"]', '', page_content)

    # Replace all whitespace characters with commas
    page_content = ','.join(page_content.split())

    # Specify the filename where you want to save the content
    filename = 'uklad_sloneczny.txt'

    # Write the content to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(page_content)

    print(f"Content saved to {filename}")
else:
    print("Page does not exist.")
