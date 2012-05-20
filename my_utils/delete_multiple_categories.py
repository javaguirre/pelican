import re
import os

DIR = '/home/javaguirre/Proyectos/python/my_blog/rst'

for filename in os.listdir(DIR):
    new_file = []
    with open(os.path.join(DIR, filename)) as f:
        for line in f:
            if re.match("^:category:", line):
                new_line = re.sub(r"(:category: \w+), .+", "\g<1>", line)
                new_file.append(new_line)
            else:
                new_file.append(line)


    with open(os.path.join(DIR, filename), "w") as f:
        for line in new_file:
            f.write(line)
