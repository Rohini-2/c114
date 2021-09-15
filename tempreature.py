temp = float(input("Enter the temperature here:- "))
chances = model(temp * lr.coef_ + lr.intercept_).ravel()[0]
if chances <=0.01:
  print("rocket will not launch")
elif chances >= 1:
  print("rokect will launch")
elif chances < 0.5:
  print("roket will not launch")
else:
  print("may be rocket get launched")