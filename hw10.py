import pickle
import os
scores=[]

def input_scores(scores):
  print("[점수 입력]")
  i=0
  while True:
    i+=1
    score=int(input(f"#{i}? "))
    scores.append(score)
    if score<0:
      del scores[len(scores)-1]
      return False

def get_average(scores):
  sum=0
  for i in range(len(scores)):
    sum+=scores[i]
  return sum/len(scores)

def show_scores(scores):
  print()
  print("[점수 출력]")
  print("개인점수: ",end="")
  for i in range(len(scores)):
    print(f"{scores[i]}",end=" ")

def save_data(filename):
    with open(filename,"wb") as file:
        pickle.dump(scores,file)
        
def load_data(filename):
    with open(filename,"rb") as file:
        return pickle.load(file)

filename="score.bin"

if os.path.exists(filename):
    print("[파일 읽기]")
    scores=load_data(filename)
    load_data(filename)
    show_scores(scores)
    print(f"\n평균: {get_average(scores):.1f}")
    input()
else:
    input_scores(scores)
    get_average(scores)
    show_scores(scores)
    print()
    print(f"평균: {get_average(scores):.1f}")
    save_data(filename)
    input()
