input_file_path = 'BK_Alges_EP_V1_5_18_original.txt' # Replace with the actual input file path
output_file_path = 'BK_Alges_EP_V1_5_18_mod.txt'  # Replace with the desired output file path

# Read the contents of the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()  # Read the contents of the input file line by line

# Creates list with words to be changed
initial_part = []
for line in lines:
    words = line.split()
    for word in words:
        if word.endswith("_file,"):
            initial_part.append(word[:-6])  # Remove "_file" suffix

print("words to add objects",initial_part, len(initial_part))



# Process words and modify the content
modified_words_check = []
modified_lines = []

for line in lines:
    words = line.split()
    modified_words = []
    for word in words:
        if word.endswith("_file,"):
            modified_word = word.replace('_file', '') # Remove "_file" suffix
            modified_words.append(modified_word)
            modified_words_check.append(modified_word)
            print("file",word,"|mod|",modified_word)
        elif word[:-1] in initial_part:
            modified_word = word[:-1] + "_object" + word[-1]
            modified_words.append(modified_word)
            print("object",word,"|mod|",modified_word)
        else:
            modified_words.append(word)
    modified_line = ' '.join(modified_words)
    modified_lines.append(modified_line)
      
print("words that will have _file removed",modified_words_check,len(modified_words_check))


#for a in range(len(initial_part)):
#   if initial_part[a] == modified_words_check[a]:
#        print(0)
#    else:
#        print(1)

# Write the modified contents to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(modified_lines))

print("Output file created successfully.")