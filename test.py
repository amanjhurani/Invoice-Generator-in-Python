print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '--'.join(lines)

print(text)