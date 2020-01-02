class Model:
	def __init__(self, estimator, y, X):
		self.estimator = estimator
		self.y = y
		self.x = X


	def fit():
		return self.estimator.fit(self.y, self.x)

	def predict(test):
		return self.estimator.predict(test)
