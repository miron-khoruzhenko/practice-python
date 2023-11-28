from bs4 import BeautifulSoup

# Функция для чтения файла
def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

# Функция для записи в файл
def write_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

# Функция для извлечения уникальных классов из HTML с помощью BeautifulSoup
def extract_unique_classes(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    all_classes = set()
    for element in soup.find_all(class_=True):
        all_classes.update(element.get('class'))
    
    return all_classes 

# Функция для поиска и замены стилей в CSS
def find_and_replace_styles(css_content, html_classes):
    updated_css_content = css_content
    css_dict = {}
    
    for line in css_content.splitlines():
        if line.strip().startswith('.'):
            # class_name = line.split('{')[0].strip().strip('.')
            class_names = line.split('{')[0].strip().split(' ')
            tmp = class_names
            class_names = []

            for class_name in tmp:
                if not class_name.startswith('.') or ':' in class_name:
                    continue
                class_name = class_name.strip('.').split('.')
                for tmp_class in class_name:
                    class_names.append(tmp_class)
                    print(tmp_class)
                

            for class_name in class_names:
                if not class_name.startswith('.') or ':' in class_name:
                    continue
                print(class_name)
                if class_name in html_classes:
                    start = line.find('@apply') + len('@apply')
                    end = line.find(';', start)
                    styles = line[start:end].strip()
                    # print(styles)
                    css_dict[class_name] = styles
                    updated_css_content = updated_css_content.replace(line, '')  # Remove the line from CSS
    
    return updated_css_content, css_dict

# Функция для обновления классов в HTML
def update_html_classes(html_content, css_dict):
    soup = BeautifulSoup(html_content, 'html.parser')
    for element in soup.find_all(class_=True):
        original_classes = element.get('class')
        new_classes = ' '.join(css_dict.get(cls, cls) for cls in original_classes)
        element['class'] = new_classes.split()
    return str(soup)

# Функция для обновления классов в HTML
def update_html_classes(html_content, css_dict):
    soup = BeautifulSoup(html_content, 'html.parser')
    for element in soup.find_all(True, class_=True):
        original_classes = element['class']
        new_classes = [css_dict.get(cls, cls) for cls in original_classes]
        element['class'] = new_classes
    return str(soup)

# Пути к файлам
html_file_path = './src/index.html'
css_file_path = './src/input.css'

html_file_dist_path = './dist/index.html'
css_file_dist_path = './dist/input.css'

# Чтение содержимого файлов
html_content = read_file(html_file_path)
css_content = read_file(css_file_path)

# Извлечение уникальных классов из HTML
unique_html_classes = extract_unique_classes(html_content)

# Нахождение и замена стилей в CSS, создание словаря замен
updated_css_content, css_styles_dict = find_and_replace_styles(css_content, unique_html_classes)

# Обновление классов в HTML
updated_html_content = update_html_classes(html_content, css_styles_dict)

# Запись результатов обратно в файлы
write_file(html_file_dist_path, updated_html_content)
write_file(css_file_dist_path, updated_css_content)

print("HTML and CSS files have been updated.")
