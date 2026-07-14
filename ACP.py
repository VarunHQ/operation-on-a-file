
 
print("================================")
print("PURE-SMART NOTES ORGANIZER FOR KIDS")
print("================================")
 
 

sample_notes = [
    "IMPORTANT: Complete school work\n",
    "TODO: Play outdoors for atleast 30 mins\n",
    "NOTE: Comp. Sci Topic Test (ref. School Diary)\n",
    "IMPORTANT: Play Minecraft with Friends\n",
    "SKIP: Go to the park\n",
    "NOTE: 21st July is the day for the sumbisson of Project for Innova TN26 \n",
    "TODO: Help mom with either chores or dinner\n"
]
 
file = open("Varun's notes.txt", "w")
file.writelines(sample_notes)
file.close()
 
print("Sample file 'Varun's notes.txt' created successfully.")
 

 
print("\nPART 1: Preview Notes with read(n)")
 
file = open("Varun's notes.txt", "r")
preview = file.read(303)
file.close()
 
print("The whole file:")
print(preview)
 
 
 
print("\nPART 2: Read All Lines with readlines()")
 
file = open("Varun's notes.txt", "r")
lines = file.readlines()
file.close()
 
print("Total lines in file:", len(lines))
 
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
 
 
 
print("\nPART 3: Loop Through File Line by Line")
 
file = open("Varun's notes.txt", "r")
 
for line in file:
    print("Reading:", line.strip())
 
file.close()
 
 
 
print("\nPART 4: Filter Lines with Conditions")
 
file = open("Varun's notes.txt", "r")
 
for line in file:
    if line.startswith("SKIP"):
        print("Skipped:", line.strip())
    else:
        print("Kept:", line.strip())
 
file.close()
 
 
 
print("\nPART 5: Copy Selected Lines to a New File")
 
file = open("Varun's notes.txt", "r")
lines = file.readlines()
file.close()
 
output_file = open("organized-notes.txt", "w")
 
for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        output_file.write(line)
 
output_file.close()
 
print("Selected lines copied to 'organized-notes.txt'.")
 
 

print("\nOrganized Notes:")
 
file = open("organized-notes.txt", "r")
 
for line in file:
    print(line.strip())
 
file.close()
 
 
 
print("\n================================")
print("PURE-    SMART NOTES ORGANIZER SUMMARY")
print("================================")
print("read(n): Previewed the first few characters.")
print("readlines(): Stored all lines in a list.")
print("Loop: Read the file line by line.")
print("Condition: Skipped lines starting with SKIP.")
print("Copy: Saved IMPORTANT and TODO lines into a new file.")
print("================================")