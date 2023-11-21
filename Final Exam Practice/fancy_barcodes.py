import re

barcodes_count = int(input())
pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
product_group = ""
for i in range(barcodes_count):
    input_barcode = input()
    barcodes = re.findall(pattern, input_barcode)
    if len(barcodes) == 0:
        print('Invalid barcode')
        continue
    valid_barcodes = [match[1] for match in barcodes]
    for current_barcode in valid_barcodes:
        digit_pattern = r"\d+"
        digits_in_barcode = re.findall(digit_pattern, current_barcode)
        if len(digits_in_barcode) == 0:
            product_group = '00'
            print(f'Product group: {product_group}')
        else:
            product_group = ''.join(digits_in_barcode)
            print(f'Product group: {product_group}')