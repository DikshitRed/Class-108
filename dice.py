import random
import plotly.express as px
import plotly.figure_factory as ff

dice_count=[]
count=[]

for f in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_count.append(dice1+dice2)
    count.append(f)
fig=ff.create_distplot([dice_count],["The Dice Count"])
fig=px.bar(x=dice_count, y=count)
fig.show()
