def main():
    n = int(input())
    objects = {}
    
    for _ in range(n):
        line = input().split()
        obj_type = line[0]
        name = line[1]
        
        if obj_type == 'INNTAK':
            value = True if line[2] == 'SATT' else False
            objects[name] = {'type': obj_type, 'value': value}
        elif obj_type == 'UTTAK':
            input_name = line[2]
            objects[name] = {'type': obj_type, 'input_name': input_name}
        elif obj_type == 'EKKI':
            input_name = int(line[2])
            output_value = False if line[3] == 'OSATT' else True
            objects[name] = {'type': obj_type, 'input_name': input_name, 'output_value': output_value}
        elif obj_type == 'EDA':
            input1 = int(line[2])
            input2 = int(line[3])
            output_value = False if line[4] == 'OSATT' else True
            objects[name] = {'type': obj_type, 'input1': input1, 'input2': input2, 'output_value': output_value}
        elif obj_type == 'OG':
            input1 = int(line[2])
            input2 = int(line[3])
            output_name = line[4]
            objects[name] = {'type': obj_type, 'input1': input1, 'input2': input2, 'output_name': output_name}
    
    for obj_name in objects:
        if objects[obj_name]['type'] == 'UTTAK':
            input_value = None
            for pre_obj_name in objects:
                if 'output_name' in objects[pre_obj_name] and objects[pre_obj_name]['output_name'] == obj_name:
                    if input_value is None:
                        input_value = objects[pre_obj_name]['output_value']
                    else:
                        print(f"{obj_name} {('OSATT' if not input_value else 'SATT')}")
                        break
                elif 'input1' in objects[pre_obj_name] and objects[pre_obj_name]['input1'] == obj_name:
                    input_value = objects[pre_obj_name]['output_value']
                elif 'input2' in objects[pre_obj_name] and objects[pre_obj_name]['input2'] == obj_name:
                    input_value = objects[pre_obj_name]['output_value']
            if input_value is not None:
                print(f"{obj_name} {'SATT' if input_value else 'OSATT'}")

main()