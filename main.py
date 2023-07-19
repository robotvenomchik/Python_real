#test1

some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600,358]

def filter_list(value):
    if isinstance(value, (int, float)) and value > 500:
            return True
    return False
filtred_list=list(filter(filter_list,some_data))
print(filtred_list)








