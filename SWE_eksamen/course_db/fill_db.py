import psycopg2, datetime
from hypothesis.strategies import (text,integers,sampled_from,
            dates,characters)

navne = """1   Nielsen	249.088
2	Jensen	247.723
3	Hansen	208.069
4	Pedersen	157.334
5	Andersen	155.314
6	Christensen	115.998
7	Larsen	112.454
8	Sørensen	107.446
9	Rasmussen	91.963
10	Jørgensen	85.855
11	Petersen	76.504
12	Madsen	62.699
13	Kristensen	59.371
14	Olsen	46.574
15	Thomsen	38.943
16	Christiansen	36.069
17	Poulsen	31.501
18	Johansen	30.671
19	Møller	29.886
20	Mortensen""".split('\n')

efternavne = [x.split()[1] for x in navne]

navne = """1	Peter	48.655
2	Jens	46.479
3	Michael	45.096
4	Lars	44.857
5	Henrik	42.274
6	Thomas	42.112
7	Søren	40.787
8	Jan	38.277
9	Christian	37.685
10	Martin	37.185
11	Niels	36.103
12	Anders	34.252
13	Morten	34.049
14	Jesper	33.884
15	Jørgen	32.901
16	Hans	32.850
17	Mads	31.603
18	Per	31.464
19	Ole	31.266
20	Rasmus	30.367
1	Anne	45.852
2	Kirsten	41.361
3	Mette	38.748
4	Hanne	38.658
5	Anna	34.156
6	Helle	34.023
7	Susanne	31.156
8	Lene	30.853
9	Maria	29.256
10	Marianne	26.989
11	Lone	25.315
12	Camilla	24.639
13	Inge	24.284
14	Pia	24.192
15	Karen	24.127
16	Bente	23.913
17	Louise	23.846
18	Charlotte	23.688
19	Jette	23.247
20	Tina	23.225""".split('\n')

fornavne = [x.split()[1] for x in navne]

c = characters(whitelist_categories='L',min_codepoint=0x41,max_codepoint=255)
t = text(max_size=5,alphabet=c,min_size=4)
efternavn = sampled_from(efternavne)
fornavn = sampled_from(fornavne)
note = text(max_size=50,alphabet=c,min_size=10)
i = integers(min_value=1,max_value=300)
d = dates(min_value=datetime.date(1990,1,1),max_value=datetime.date(2000,12,31))
p = integers(min_value=1,max_value=30)

con = psycopg2.connect(user='postgres',host='localhost',port=5432,dbname='studie')
cur = con.cursor()


def create_student(first,last, birthday):
    SQL = f"insert into students (firstname,lastname,dateofbirth)\
            values ('{first}','{last}','{birthday}')"
    cur.execute(SQL)

def create_course(name,short, points):
    SQL = f"insert into courses (name,shortname,points) \
            values ('{name}','{short}',{points})"
    print(SQL)
    cur.execute(SQL)

for i in range(10):
    create_student(fornavn.example(),efternavn.example(),d.example())
    create_course(note.example(),t.example(),p.example())
con.commit()

con.close()
