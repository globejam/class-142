import pandas as pd

df=pd.read_csv("final.csv")

C=df["vote_average"].mean()

m=df["vote_count"].quantile(0.9)

q_movies=df2.copy().loc[df2["vote_count"]>=m]

def weighted_rating(x,m=m,C=C):
  v=x["vote_count"]
  R=x["vote_average"]
  return ((v/(v+m))*R)+((m/(v+m))*C)

q_movies["score"]=q_movies.apply(weighted_rating,axis=1)

q_movies=q_movies.sort_values("score",ascending=False)
output=q_movies[["original_title","vote_average","poster_link","release_date","run_time","overview"]].head(20).values.tolist()