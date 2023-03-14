'''
Write a program that defines two functions called create_sent1( ) and
create_sent2( ). Both receive following 3 lists:
subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV Serials','Netflix']
Both functions should form sentences by picking elements from these
lists and return them. Use for loops in create_sent1( ) and list
comprehension in create_sent2( ).
'''

def create_Sent1(sub, ver, obj):
    lst=[]
    for i in range(len(sub)):
        for j in range(len(obj)):
            for k in range(len(obj)):
                sent=sub[i]+' '+ver[j]+' '+obj[k]
                lst.append(sent)
    return lst

def create_sent2(sub, ver, obj):
    return [(s+' '+v+' '+o) for s in sub for v in ver for o in obj]

subjects=['He', 'She']
verbs=['love', 'hates']
objects=['TV Serials', 'Netflix']

lst1=create_Sent1(subjects, verbs, objects)
for l in lst1:
    print(l)

print()

lst2=create_sent2(subjects, verbs, objects)
for l in lst2:
    print(l)