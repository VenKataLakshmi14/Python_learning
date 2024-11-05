import os

current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

new_dir = "my_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created!")
else:
    print(f"Directory '{new_dir}' already exists!")

print("\nList of files and directories in the current directory:")
for item in os.listdir(current_directory):
    print(item)

if os.path.exists(new_dir) and os.path.isdir(new_dir):
    os.rmdir(new_dir)
    print(f"\nDirectory '{new_dir}' has been removed.")
else:
    print(f"\nDirectory '{new_dir}' does not exist or is not empty.")
