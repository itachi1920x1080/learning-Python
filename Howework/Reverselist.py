number = [10, 20, 30, 40, 50,10]

# create a set from list
un_number = set(number)
#set(): លុបលេខស្ទួនបានភ្លាមៗ ប៉ុន្តែវាមិនរក្សាលំដាប់ទីតាំងដើមនៃទិន្នន័យទេ។
# convert set to list
final_list = list(un_number)

final_list.reverse()
print(f"orginal list is: {number}")
print(f"reversed list is: {final_list}")