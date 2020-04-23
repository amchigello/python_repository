import re

text = '''
Contact
Universität Heidelberg

Seminarstraße 2
69117 Heidelberg
Phone +49 6221 54-0
Fax +49 6221 54-2618
(Postal address: Postfach 10 57 60, 69047 Heidelberg)

Map (Ger)

 
University Management

President's Office
Grabengasse 1
69117 Heidelberg
Phone +49 6221 54-19001/19002
Fax +49 6221 54*19009
rektor@rektorat.uni-heidelberg.de

 
Points of Contact
Alumni

Heidelberg Alumni International
Marstallstraße 6
69117 Heidelberg
Phone +49 6221 54-3489
Fax +49 6221 54.2091
(Postal address: Postfach 10 57 60, 69047 Heidelberg)
alumni@zuv.uni-heidelberg.de
'''

pattern = re.compile(r'\.[a-z]+')

matches = pattern.findall(text)
for x in matches:
    print(x)
