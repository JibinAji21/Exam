# f=open('demo.txt','x')
# print(f.write("hello\nwelcome\ngood mrng"))

f=open('demo.txt','r')
l=len(f.readlines())
f.seek(0)
longest_word=''
for i in range(l):
    a=f.readline().strip()
    s=a.split(' ')
    for j in s:
        if j!='':
            if len(longest_word)<len(j):
                longest_word=j
print('longest_word =',longest_word)
