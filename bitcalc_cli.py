import sys

BITS_IN_A_BYTE = 8

def get_notation_hash(notation):
    notation_info = {
        'message': '(informal notation: kilobyte = 1024 bytes)',
        'type': 'legacy',
        'kilo': 1024
    }
    if notation.lower() == 'ieee':
        notation_info['message'] = '(IEEE notation: kilobyte = 1000 bytes)'
        notation_info['type'] = notation
        notation_info['kilo'] = 1000
    return notation_info

def convert_units(input_units, input_amount, notation):
    notation_hash = get_notation_hash(notation)
    kilo = notation_hash['kilo']

    output = {}
    units = ['bits', 'bytes', 'kilobits', 'kilobytes', 'megabits', 'megabytes', 'gigabits', 'gigabytes', 'terabytes', 'petabytes']

    if input_units == 'bits':
        output['bits'] = float(input_amount)
    elif input_units == 'bytes':
        output['bits'] = float(input_amount) * BITS_IN_A_BYTE
    elif input_units == 'kilobits':
        output['bits'] = float(input_amount) * kilo
    elif input_units == 'kilobytes':
        output['bits'] = float(input_amount) * BITS_IN_A_BYTE * kilo
    elif input_units == 'megabits':
        output['bits'] = float(input_amount) * kilo * kilo
    elif input_units == 'megabytes':
        output['bits'] = float(input_amount) * kilo * kilo * BITS_IN_A_BYTE
    elif input_units == 'gigabits':
        output['bits'] = float(input_amount) * kilo * kilo * kilo
    elif input_units == 'gigabytes':
        output['bits'] = float(input_amount) * kilo * kilo * kilo * BITS_IN_A_BYTE
    elif input_units == 'terabytes':
        output['bits'] = float(input_amount) * kilo * kilo * kilo * kilo * BITS_IN_A_BYTE
    elif input_units == 'terabits':
        output['bits'] = float(input_amount) * kilo * kilo * kilo * kilo
    elif input_units == 'petabytes':
        output['bits'] = float(input_amount) * kilo * kilo * kilo * kilo * kilo * BITS_IN_A_BYTE
    elif input_units == 'petabits':
        output['bits'] = float(input_amount) * kilo * kilo * kilo * kilo * kilo

    output['bytes'] = output['bits'] / BITS_IN_A_BYTE
    output['kilobits'] = output['bits'] / kilo
    output['kilobytes'] = output['kilobits'] / BITS_IN_A_BYTE
    output['megabits'] = output['kilobits'] / kilo
    output['megabytes'] = output['megabits'] / BITS_IN_A_BYTE
    output['gigabits'] = output['megabits'] / kilo
    output['gigabytes'] = output['gigabits'] / BITS_IN_A_BYTE
    output['terabits'] = output['gigabits'] / kilo
    output['terabytes'] = output['terabits'] / BITS_IN_A_BYTE
    output['petabits'] = output['terabits'] / kilo
    output['petabytes'] = output['petabits'] / BITS_IN_A_BYTE

    return output

def main():
    if len(sys.argv) != 4:
        print("Usage: python bitcalc.py <input_units> <input_amount> <notation>")
        sys.exit(1)

    input_units = sys.argv[1]
    input_amount = sys.argv[2]
    notation = sys.argv[3]

    input_amount = ''.join(filter(lambda x: x.isdigit() or x == '.', input_amount)) or '1'

    output = convert_units(input_units, input_amount, notation)

    for unit, amount in output.items():
        print(f"{unit}: {amount}")

if __name__ == "__main__":
    main()

