from google.colab import drive
drive.mount('/content/drive')

#before running this, run "pip install striprtf" in command line
!pip install striprtf
import os.path
from striprtf.striprtf import rtf_to_text 

def all_paths(dirname):
  dir_list = os.listdir(dirname)
  final = []
  for item in dir_list:
    path = os.path.join(dirname, item)
    if os.path.isdir(path):
      final += all_paths(path)
    else:
      final.append(path)
  
  return final 

def extract_our_dataset(path):
  doc = open(path, 'r')
  rtf = doc.read() 
  text = rtf_to_text(rtf)
  lines = text.split('\n')

  headlines = []
  texts = []
  flag_article = False
  flag_second = True
  count_consecutive = 0

  text = ""
  headline = ""

  for line in lines:

    if line != '' and line != ' ':
      count_consecutive += 1
      if flag_article == False and flag_second: 
        headlines.append(line)
        flag_second = False

    else:
      if count_consecutive > 1:
        flag_article = True
      count_consecutive = 0
    
    test_for_end = line.split(' ')
    if len(test_for_end) == 2 and test_for_end[0] == 'Document':
      flag_article = False 
      flag_second = True
      texts.append(text)
      text = "" 

    if flag_article and line != '':
      text += line


  return headlines, texts


new_path_list = all_paths(PATH) # Enter File Path Here

new_labels = []
new_texts = []

for path in new_path_list:
  if path != "NULL": # Replace if there are any corrupt files at hand
    temp_head, temp_text = extract_our_dataset(path)
    new_labels += temp_head
    new_texts += temp_text
  print(len(new_labels), len(new_texts), path)

