def get_links_from_file(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    url_arr = []

    for line in lines:
      url_arr.append(line[:-1])
    
  return url_arr

print(get_links_from_file('links1.txt'))