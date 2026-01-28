# TODO Найдите количество книг, которое можно разместить на дискете
p = 100
l = 50
c = 25
b = 4

book_size = p * l * c * b
disk_size = 1.44 * 1024 * 1024
book_count = int(disk_size // book_size)
print("Количество книг, помещающихся на дискету:", book_count)
