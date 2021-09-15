import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
X=np.reshape(temperature_list,(len(temperature_list),1))
print(X.ravel())
Y=np.reshape(melted_list,(len(melted_list),1))
lr=LogisticRegression()
lr.fit(X,Y)
plt.scatter(X.ravel(),Y.ravel(),color="black")

def model(x):
  return 1/(1+np.exp(-x))

X_test=np.linspace(0,5000,10000)
melting_chances=model(X_test*lr.coef_+lr.intercept_).ravel()  
plt.plot(X_test,melting_chances,color="cyan",linewidth=3)
plt.axhline(y=0,color="blue",linestyle='-')
plt.axhline(y=1,color="blue",linestyle='-')
plt.axhline(y=0.5,color="blue",linestyle='--')
plt.axvline(x=X_test[6843],color="purple",linestyle='--')
plt.xlim(3400,3450)
plt.show()