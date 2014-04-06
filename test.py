__author__ = 'daokh'

mpes = ["hi", "foo", "bar", 'hid']

for mpe in mpes:
    if(mpe == "hi"):
        mpes.remove(mpe)

print mpes


S = [1,30,20,30,2]
S.pop()
update=[4,5,6,2]
for i, s in enumerate(S):
    for u in update:
     if s == u:
         S[i] = 999

print S


mpeid = []
if not mpeid:
    print "yes"

print mpeid

result = {"mpeid":1}
foo = result.update({'status':'succeeded'})
print result

input = {"fda":2}
if not input:
    print"YES"