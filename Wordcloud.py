import matplotlib.pyplot as plt
from wordcloud import WordCloud as wc
import docx

punctuations = ['!', '"', '#', "\n" , '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=','>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
uninteresting_words = ["the", "mr", "mrs", "for", "us", "a", "so", "to", "if", "is", "not", "on", "it", "of", "and", "or", "an", "as", "in", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "than"]

def clean_text(text):
  cleaned_text = ""
  for line in text:
      for chr in punctuations:
          line = line.replace(chr, "")
      cleaned_text += line
  return cleaned_text

def count_frequency(cleaned_text):
  new_content = ""
  for chr in cleaned_text:
      new_content += chr
  temp_file = new_content.split(" ")
  frequencies = {}
  for word in temp_file:
      if word.lower() not in uninteresting_words:
          if word.lower() in frequencies:
              frequencies[word.lower()] +=1
          if word.lower() not in frequencies:
              frequencies[word.lower()] = 1
  freq = {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1])}
  return freq

def generate_cloud(text):
  c_text = clean_text(text)
  frequencies = count_frequency(c_text)
  cloud = wc(background_color="black",colormap='Blues',width=1200,height=720)
  cloud.generate_from_frequencies(frequencies)

  # Display your wordcloud image
  cloud.to_file("media/word.png")


def process_text(file_text):
  with open(file_text, "r+",encoding='utf-8') as fin:
    text = fin.readlines()
  generate_cloud(text)
  token = 'Done'
  return token

def process_docx(file_docx):
  text = ''
  doc = docx.Document(file_docx)
  for paragraph in doc.paragraphs:
    text += (paragraph.text)
  generate_cloud(text)
  token = 'Done'
  return token