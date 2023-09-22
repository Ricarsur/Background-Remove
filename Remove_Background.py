from rembg import remove

input_path = 'unnamed.jpg'
output_path= 'wdsa.png'

with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)