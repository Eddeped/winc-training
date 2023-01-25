# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
score1='Ruud Gullit'
score2='Marco van Basten'
goal_0=32
goal_1=54
scorersa=score1+f' {goal_0}',score2+f' {goal_1}'
scorers=score1+f' {goal_0}, '+score2+f' {goal_1}'
report=score1+f' scored in the {goal_0}nd minute\n'+score2+f' scored in the {goal_1}th minute'
player=score1 
s1=player.find("Ruud")
first_name=player[s1:4]
last_name_len=player.find("Gullit")
last_name=player[last_name_len:]
name_short=player[s1:1]+'. '+last_name
x=len(first_name)
chant='Ruud!'*x
print (chant)

print (report)
print (first_name)
print (last_name)
print (name_short)

