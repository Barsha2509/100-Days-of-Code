#TODO: Create a letter using starting_letter.txt
with open("/Users/abhisheksinha/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r') as file:
    contents = file.readlines()
    # print(contents)

letter_header = contents[0]
# print(letter_header)

letter_body = contents[1:]
# print(letter_body)

#for each name in invited_new_names.txt
with open("/Users/abhisheksinha/PycharmProjects/Mail Merge Project Start/Input/names/invited_names.txt", mode='r') as data:
    names = data.readlines()
    # print(new_names)
new_names = []
for name in names:
    clean_name = name.strip("\n")
    new_names.append(clean_name)
# # print(new_names)
# print(contents)
#
#Replace the [name] placeholder with the actual name.
for i in new_names:
    header = letter_header.replace("[name]", i)

#Save the letters in the folder "ReadyToSend".

    with open(f"/Users/abhisheksinha/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.docx", mode = "w") as send:
        send.write(header)

    with open(f"/Users/abhisheksinha/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.docx", mode = "a") as send:
        for j in letter_body:
         send.write(j)
