import random
random.seed(1)

y = int(input("Number of people in your class: "))
print("There are", y, " people in your class")

#get score of ppl in sch
score_list = random.sample(range(1, 100), y)
score_list.sort(reverse=True)
print ("List of scores is : " + str(score_list))

#your score and placing
def rank_score(your_score):
  if your_score in score_list:
    index = score_list.index(your_score) +1
    print('The placing of your score within your class is #', index)

  else:
    print("you are not in this class")

x = int(input("Your score: "))
rank_score(x)
