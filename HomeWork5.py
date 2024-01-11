import json

final_dict = {}

with open('purchase_log.txt', encoding='utf-8') as purchases:
      for i in purchases:
        line = i.strip()
        dict_ = json.loads(line)
        #назначаем ключем значение ключа userd_id
        key = dict_['user_id']
        # print(key)
        #Назначаем значением значение ключа category
        value = dict_['category']
        # print(value)
        #Создаем новый словарь, где ключ принмает значение переменной key, а значение принимается из value
        final_dict[key] = value


with open('visit_log.csv', 'r') as f:
      with open('funnel.csv','w', encoding='utf-8') as f_2:
          for i, line in enumerate(f):
              #Удаляем лишние пробелы и переносы строк, и преобразуем в список по разделителю ','
            line = line.strip().split(',')
              #Если первый элемент списка есть в ключах словаря final_dict
            if line[0] in final_dict.keys():
                # Добавляем в список значение ключа
              line.append(final_dict[line[0]])
              # print(final_dict[line[0]])
              ad_line = ','.join(line)
              #Записываем новый файл
              f_2.write(ad_line + '\n')

