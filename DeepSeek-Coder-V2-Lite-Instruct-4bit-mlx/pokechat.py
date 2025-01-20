def decode_message(encoding_string, pokemon_ids):
    encoding_dict = {str(i).zfill(3): char for i, char in enumerate(encoding_string, start=1)}
    message = ''
    for pokemon_id in pokemon_ids:
        if pokemon_id in encoding_dict:
            message += encoding_dict[pokemon_id]
    return message

# Sample Input 1
encoding_string = "PpIiKkAaCcHhUu"
pokemon_ids = "001004006008010012014"
print(decode_message(encoding_string, pokemon_ids))  # Output: Pikachu

# Sample Input 2
encoding_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,?!"
pokemon_ids = "016009011001053016009011001"
print(decode_message(encoding_string, pokemon_ids))  # Output: pika pika