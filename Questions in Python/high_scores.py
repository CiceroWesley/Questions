def latest(scores):
    print("Latest element {}.".format(scores[len(scores)-1]))


def personal_best(scores):
  sort = sorted(scores)
  print("Value {}.".format(sort[len(sort)-1]))

def personal_top_three(scores):
    sort = sorted(scores)
    if len(sort) > 2:
      for i in range(len(sort)-1,len(sort)-4,-1):        #secund step plus one
        print(sort[i])
    elif len(sort) == 2:
      print(sort[1])
      print(sort[0])
    else:
      print(sort[0])    

score = []

latest(score)
personal_best(score)
personal_top_three(score)


'''
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

In this exercise, you're going to use and manipulate lists. Python lists are very versatile, and you'll find yourself using them again and again in problems both simple and complex.

- [**Data Structures (Python 3 Documentation Tutorial)**](https://docs.python.org/3/tutorial/datastructures.html)
- [**Lists and Tuples in Python (Real Python)**](https://realpython.com/python-lists-tuples/)
- [**Python Lists (Google for Education)**](https://developers.google.com/edu/python/lists)
'''
