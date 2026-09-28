
text= "Hello World"
print(f"Text :{text}")

print("utf-8 encode".center(60, "-"))
encoded_text = text.encode("utf-8")
print(encoded_text)

print("utf-8 decode".center(60, "-"))
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)

print("ASCII".center(60, "-"))
ascii_bytes = text.encode("ascii", errors="replace")
print(ascii_bytes)
