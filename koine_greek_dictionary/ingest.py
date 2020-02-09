import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
import re


def clean_meaning(meaning, strong):
  # remove <a href="javascript:void(0)" etc. >
  clean = re.sub(r"<a href=\"javascript:void\(0\)\" title=\"([^\"]+)\"[^<]+<\/a>", r"\g<1>", meaning)

  # remove <ref> and only keep reference
  clean = re.sub(r"<ref='[^']+'>([^<]+)</ref>", r"\g<1>", clean)

  # remove <hi rend="subscript"> and <hi rend="sub">
  clean = clean.replace('<hi rend="subscript">', '').replace('<hi rend="sub">', '')
  
  # remove <ref osisRef="xxx">
  clean = re.sub(r"<ref osisRef=\".*\">", r"", clean)
  
  # find unclosed <i> tags
  found = re.findall(r"<\/?i>", clean)
  if len(found) % 2 != 0:
    print('<i>', strong)

  # find unclosed <i> tags
  found = re.findall(r"<\/?b>", clean)
  if len(found) % 2 != 0:
    print('<b>', strong)

  # remove <foreign xml:lang="grc">
  clean = clean.replace("<foreign xml:lang=\"grc\">", '')

  # remove <Lat> and </Lat>
  clean = clean.replace("<Lat>", '').replace("</Lat>", '')

  return clean

env = Environment(
  loader=FileSystemLoader('koine_greek_dictionary/'),
  # autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('entry_template.xml')

lexicon = pd.read_csv('koine_greek_dictionary/lexicon.tsv', sep='\t')#.head()

lexicon['Meaning'] = lexicon.apply(lambda row: clean_meaning(row['Meaning'], row['EStrong#']), axis=1)

dictionary = template.render(words=lexicon.to_dict('records'))

with open("koine_greek_dictionary/KoineGreekDictionary.xml", "w") as fh:
  print('writing to KoineGreekDictionary.xml')
  fh.write(dictionary)