import os

output = ''
for dir in os.listdir('.'):
    if not os.path.isdir(dir):
        continue
    output += '/* ' + dir + ' */\n'
    for file in os.listdir(dir):
        if file.endswith('.svelte'):
            output += 'export { default as ' + file.split('.')[0] + ' } from \'./'+dir+'/'+file+'\';\n'

open('index.ts','w').write(output)
