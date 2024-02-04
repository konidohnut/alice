import argparse


def main(file_path):
    with open(file_path, 'r') as file:
        encrypted_message = file.read().strip()
        k = 0
        encrypted_message = [char for char in encrypted_message if char.isalnum()]
        while k < len(encrypted_message) - 1:
            if encrypted_message[k] == encrypted_message[k + 1]:
                encrypted_message.pop(k)
                encrypted_message.pop(k)
                if k != 0:
                    k -= 1
                else:
                    continue
            else:
                k += 1
        print('result:', ''.join(encrypted_message))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some file.')
    parser.add_argument('file', type=str, help='Path to the file')
    args = parser.parse_args()
    main(args.file)
