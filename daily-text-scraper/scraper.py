import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_data():
    # Get today's date in the required format
    today = datetime.today()
    date_str = today.strftime('%Y-%m-%dT00:00:00.000Z')
    
    # Construct the URL with today's date
    url = f"https://wol.jw.org/en/wol/h/r1/lp-e/{today.strftime('%Y/%m/%d')}"
    print(f"Fetching URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the specific section for today's daily text
    today_section = None
    sections = soup.find_all('div', {'class': 'tabContent'})
    
    for section in sections:
        data_date = section.get('data-date', '')
        if data_date.startswith(date_str):
            today_section = section
            break
    
    if not today_section:
        print("Today's text section not found.")
        return None

    # Extract the header (title)
    header = today_section.find('header')
    title = header.find('h2').text.strip() if header and header.find('h2') else "No title found"
    
    # Extract the scripture
    scripture = today_section.find('p', {'class': 'themeScrp'})
    scripture_text = scripture.text.strip() if scripture else "No scripture found"
    
    # Extract the body text
    body_text_div = today_section.find('div', {'class': 'bodyTxt'})
    body_texts = [p.text.strip() for p in body_text_div.find_all('p')] if body_text_div else ["No body text found"]
    
    return {
        "title": title,
        "scripture": scripture_text,
        "body_texts": body_texts
    }

def main():
    data = fetch_data()
    if data:
        print("Date:")
        print(data['title'])
        print("\nScripture:")
        print(data['scripture'])
        print("\nDaily Text:")
        for item in data['body_texts']:
            print(item)
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
