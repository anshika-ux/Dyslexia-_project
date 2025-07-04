import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import gtts
import playsound

# Function to scrape text from a webpage
def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])
    return article_text

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to convert text to speech
def text_to_speech(text):
    tts = gtts.gTTS(text=text, lang="en")
    tts.save("summary.mp3")
    playsound.playsound("summary.mp3")

# Main function to run the web scraping and summarization
def main():
    print("Welcome to the Voice-Based AI Assistant for Summarization!")
    print("You can either paste text for summarization or provide a URL.")
    
    choice = input("Type 'url' to summarize from a webpage or 'text' to paste text: ").strip().lower()

    if choice == 'url':
        url = input("Enter the URL of the webpage to summarize: ")
        print("Scraping the webpage...")
        article_text = scrape_webpage(url)
    elif choice == 'text':
        article_text = input("Paste the text you want to summarize: ")
    else:
        print("Invalid choice. Please restart the program.")
        return

    print("Generating summary...")
    summary = summarize_text(article_text)
    print("Summary:", summary)
    text_to_speech(summary)

if __name__ == "__main__":
    main()
