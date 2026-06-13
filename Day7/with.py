# with គឺជា Context Manager (អ្នកគ្រប់គ្រងបរិបទ) ដែលត្រូវបានប្រើដើម្បី "ខ្ចប់" (wrap) ដំណើរការនៃប្លុកកូដមួយ។»
# auto close file after usage
with open('sample.txt', 'w') as file:
    file.write('Hello, World!')