import random
when = ['Once upon a time', 'Yesterday', 'Tonight', 'A long time ago','On 20nd April']
who = ['a horse', 'a penguin', 'a mouse', 'a turtle','a kitten']
name = ['Alia', 'Mariam','Crazy', 'Cassie', 'Maddona']
residence = ['Australia','India', 'Paris', 'Venice', 'England']
went = ['cinema', 'university','class', 'mall', 'circus']
happened = ['made a lot of friends','bought a pizza', 'found a secret door', 'solved a case', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
