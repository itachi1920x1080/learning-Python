
# create a list of squares
# squares = [x**2 for x in range(10)]
# print(squares)
#filter evens number 
# evens = [x for x in range (1,10) if x % 2 == 0]
# print(evens)

# evens = [x for x in range (100) if x % 2 != 0]
# print(evens)

#lambda agruments :experssion
# add  = lambda x ,y : x + y
# print(add(2,3))


# map() គឺជាអនុគមន៍ស្រាប់ (built-in function) មួយដែលមានប្រយោជន៍ខ្លាំង។ វាអនុញ្ញាតឱ្យអ្នកយក អនុគមន៍ (function) មួយ ទៅអនុវត្តលើគ្រប់ធាតុទាំងអស់នៅក្នុង បញ្ជី (list) ដោយមិនចាំបាច់សរសេរ for loop វែងឆ្ងាយ។
# map(function, iterable)
number = [1,2,3,4]
squars = map (lambda x : x** 2,number)
print(list (squars))
# filter() គឺជាអនុគមន៍មួយដែលប្រើសម្រាប់ ជម្រាញ់ ឬសម្រាំងយក ទិន្នន័យចេញពី List ដោយផ្អែកលើលក្ខខណ្ឌដែលយើងបានកំណត់។
envenlist = filter(lambda x: x% 2==0,number)
print(list(envenlist))


# reduce() គឺជាអនុគមន៍ដែលខុសប្លែកពី map និង filter បន្តិច។ តួនាទីរបស់វាគឺ "បូកសរុប" ឬ "កាត់បន្ថយ" ធាតុទាំងអស់នៅក្នុង List ឱ្យមកនៅសល់លទ្ធផលតែ មួយ ប៉ុណ្ណោះ (Single Value)។

from functools import reduce 

number = [1,2,3,4]
result = reduce(lambda x,y:x*y,number)
print(result)