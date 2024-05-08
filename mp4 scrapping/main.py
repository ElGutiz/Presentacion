import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# Function to extract mp4 URLs from an specific webpage
def extract_mp4_links(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all articles
        articles = soup.find_all('article')
        
        # Extract titles and hrefs from each article
        article_links = []
        for article in articles:
            href = article.find('a', href=True)['href']  # Hyperlink is within an <a> tag
            article_links.append((href))
        
        # Extract mp4 URLs from linked pages
        mp4_links = []

        for href in article_links:
            # Follow the link to the article page
            article_url = urljoin(url, href)  # Built URL
            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')
        
            # Find mp4 URLs on the article page
            links = article_soup.find_all('a', href=True)
            for link in links:
                mp4_href = link['href']
                if mp4_href.endswith('.mp4'):
                    mp4_links.append(mp4_href)
            
        # Return list of mp4 URL
        return mp4_links
    
    except Exception as e:
        print("An error occurred:", e)
        return []

# Function to download and save mp4 files
def save_mp4_files(mp4_links, directory='mp4_files'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for mp4_link in mp4_links:
        try:
            # Get the filename from the URL
            filename = mp4_link.split('/')[-1]
            
            # Fetch the mp4 content
            response = requests.get(mp4_link)
            
            # Save the mp4 content to a file
            with open(os.path.join(directory, filename), 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {filename}")
        
        except Exception as e:
            print(f"Failed to download {mp4_link}: {e}")

# Example usage
url = ''
mp4_links = extract_mp4_links(url)
save_mp4_files(mp4_links)

