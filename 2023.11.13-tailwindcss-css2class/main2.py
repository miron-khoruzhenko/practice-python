from bs4 import BeautifulSoup
import re

# Чтение и анализ HTML файла
with open("./src/index.html", "r") as file:
  soup = BeautifulSoup(file, "lxml")

# Чтение и анализ CSS файла
tailwind_classes = {}
new_css = ''
with open("./src/input.css", "r") as file:
  lines = file.readlines()
  current_classes = []
  tw_classes = []

  for line in lines:

    if ('.' in line or '#' in line) and not ('@apply' in line or '(' in line or '[' in line):
      # print(line[:line.find(' {')].strip().split(' '))

      for key in line[:line.find(' {')].strip().split(' '):
        if ':' in key:
          continue
        current_classes.append(key)
    
    if '}' in line:
      # print('Current Classes: ', current_classes)
      for clss in current_classes:
        if clss in tailwind_classes:
          tailwind_classes[clss] += f' {" ".join(tw_classes)}'
        else:
          tailwind_classes[clss] = " ".join(tw_classes)
          
      current_classes = []
      tw_classes = []


    #*
    if '@apply' in line:
      # print()
      # print(line.strip())
      # print(line.find('@apply'), line.find(';'))
      # print(line[line.find('@apply')+len('@apply'):line.find(';')].strip())
      tw_classes += line[line.find('@apply')+len('@apply'):line.find(';')].strip().split(' ')
      # print(tw_classes)
      continue
    new_css += line


with open('./dist/updated_css.css', 'w') as file:
  file.write(new_css)


for tag in soup.find_all(id=True):
  original_id = tag.get("id")
  current_classes = tag.get('class', [])

  if f'#{original_id}' in tailwind_classes:
    current_classes += tailwind_classes[f'#{original_id}'].split(' ')
    
  tag['class'] = current_classes


# Обновление классов в HTML
for tag in soup.find_all(class_=True):
# TODO: если точка то стери и добавь к классу если хеш то к создай класс ужади хеш и добавь туда
  original_classes = tag.get("class")
  new_classes = original_classes.copy()

  for original_class in original_classes:

    # if original_class in tailwind_classes:
    if f'.{original_class}' in tailwind_classes:
      new_classes += tailwind_classes[f'.{original_class}'].split(' ')

    
  tag['class'] = new_classes


# Сохранение измененного HTML
with open("./dist/index_updated.html", "w") as file:
  file.write(str(soup))

# print("Обновление классов завершено.")
