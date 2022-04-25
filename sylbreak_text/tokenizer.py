from keras.preprocessing.text import Tokenizer
from sylbreak_text.mm_num2word import extract_num, mm_num2word
from sylbreak_text.sylbreak import break_text, break_file

# define a document
try:
  doc = [break_file('/content/myanmar-tts/text/corpus.txt', ' ')]
  
except FileNotFoundError:
  print("""
    FileNotFoundError: [Errno 2] No such file or directory: 'corpus.txt'
    
    Make sure that 'corpus.txt' is under 'text' directory and you've modified 'tokenizer.py'
    so that the correct absolute path for 'corpus.txt' is provided.
    """)

  exit()

tokenizer = Tokenizer()
tokenizer.fit_on_texts(doc)

# mappings of each character and its id
syllable_index = tokenizer.word_index
sequence_index = {v:k for k, v in syllable_index.items()}

def _should_keep_syl(s):
  """
  Determines whether the input syllable is present in syllable_index

  @type   s   str
  @param  s   syllable
  
  @rtype      bool
  @return     result of the check
  """
  return s in syllable_index and s is not '_' and s is not '~'

def numbers_to_words(text):
  """
  Convert numbers into corresponding spoken words

  @type   text    str
  @param  text    input string of text

  @rtype          str
  @return         converted spoken words
  """
  nums = extract_num(text)
  for n in nums:
    text = text.replace(n, mm_num2word(n))

  return text


def normalize(text):
  """
  Normalize text string for numbers and whitespaces

  @type   text    str
  @param  text    input string of text

  @rtype          str
  @return         normalized string
  """
  text = numbers_to_words(text)
  text = break_text(text, '|')
  syllables = text.split("|")
  syllables.remove('')

  return syllables


def text_to_sequence(text):
  """
  Convert an input text into a sequence of ids

  @type   text    str
  @param  text    input string of text

  @rtype          list
  @return         list of IDs corresponding to the characters
  """
  syllables = normalize(text)
  seq = [syllable_index[s] for s in syllables if _should_keep_syl(s)]

  if not text.endswith("။"):
    seq.append(syllable_index['။'])

  return seq


def sequence_to_text(seq):
  """
  Convert a sequence of ids into the corresponding characters

  @type   seq   list
  @param  seq   list of ids

  @rtype        str
  @return       a string of text
  """
  text = ''
  for syl_id in seq:
    if syl_id in sequence_index:
      text += sequence_index[syl_id]

  return text

