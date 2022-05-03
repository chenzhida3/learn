

def result_format(datas):
    datas_list = []
    for item in datas:
        result = 'Pass' if item['result'] else 'Fail'
        item['result'] = result
        datas_list.append(item)
    return datas_list


def get_file_content(filename, chunk_size=512):
    with open(filename, encoding='utf-8') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break