from tokenUtil import TokenUtils

tutils = TokenUtils()

encoded = tutils.encode('Hello world!')

print(encoded)

original_text = tutils.decode(encoded)

print(f'original_text is "{original_text}"')

# if __name__ == '__main__':
#     pass