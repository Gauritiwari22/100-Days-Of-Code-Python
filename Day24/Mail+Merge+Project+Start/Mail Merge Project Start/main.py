PLACE="[name]"

with open("Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()

with open("Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_files:
    letter=letter_files.read()
    for name in names:
        final_name=name.strip()
        new_letter=letter.replace(PLACE,final_name)
        with open (f"Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{final_name}.docx",mode="w") as final_letter:
            final_letter.write(new_letter)

