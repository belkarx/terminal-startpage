f = open("unformatted.txt")
lines = f.readlines()
f.close()

newlines = []

tab_count = 0

ln = len(lines)

first_tab = False

first_block = True

for x in range(ln):
    line = lines[x]
    if line == "\n":
        if not first_block:
            line = """</pre></div>\n<div class=tree-column><pre>\n"""
        else:
            first_block = False
            line = """<!DOCTYPE html5>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>STARTDAMNIT</title>
<link
  rel=" shortcut icon"
  type="image/png"
  href="assets/favicon.png"
/>
<link rel="stylesheet" href="main.css" />
</head>

<div class=grid-container>

<div class=tree-column><pre>"""
    elif "--" in line:
        line = line.replace("--", "└──")

    elif x != ln-1 and "--" in lines[x+1]:
        line = line.replace("- ", "└─ ")    
    elif "- " in line:
        line = line.replace("- ", "├─ ")
    
    if "[" in line:
        parts = line.split(" [")
        parts2 = parts[0].split("─")
        front = parts2[0]+"─"
        name = parts2[-1][1:]
        href = parts[-1][:-2]
        line = f"{front} <a href={href}>{name}</a>\n"

    newlines.append(line)

ending = """
</pre></div>
 </div>
  </body>
</html>
"""

f = open("index.html", "w")
body = "<!DOCTYPE html5>" + ''.join(newlines).split("<!DOCTYPE html5>")[-1]
f.write(body + ending)
f.close()
