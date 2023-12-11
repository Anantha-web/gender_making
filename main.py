import os

folder_path = "test"
res_path = "resulttest"

for file in os.listdir(folder_path):
    name_without_extension = os.path.splitext(file)[0]
    # if for yi->male
    # elif for du->male
    # else then neutral
    if(name_without_extension.endswith("yi")):
        source_file_path = folder_path + '/' + file
        with open(source_file_path, 'r') as source_file:
            lines = source_file.readlines()
        
        modified_lines = []
        for line in lines:
            line = line.strip()
            line = line + ', male'
            modified_lines.append(line + '\n')
        
        destination_file_path = res_path + '/' + file
        with open(destination_file_path, 'w') as destination_file:
            destination_file.writelines(modified_lines)
    elif(name_without_extension.endswith("du")):
        source_file_path = folder_path + '/' + file
        with open(source_file_path, 'r') as source_file:
            lines = source_file.readlines()
        
        modified_lines = []
        for line in lines:
            line = line.strip()
            line = line + ', male'
            modified_lines.append(line + '\n')
        
        destination_file_path = res_path + '/' + file
        with open(destination_file_path, 'w') as destination_file:
            destination_file.writelines(modified_lines)
    else:
        source_file_path = folder_path + '/' + file
        with open(source_file_path, 'r') as source_file:
            lines = source_file.readlines()
        
        modified_lines = []
        for line in lines:
            line = line.strip()
            line = line + ', neutral'
            modified_lines.append(line + '\n')
        
        destination_file_path = res_path + '/' + file
        with open(destination_file_path, 'w') as destination_file:
            destination_file.writelines(modified_lines)
