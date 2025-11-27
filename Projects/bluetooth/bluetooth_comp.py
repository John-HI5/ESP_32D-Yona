import numpy as np
from tensorflow.keras.datasets import cifar10
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# === Load CIFAR-10 dataset ===
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Flatten images (N, 32, 32, 3) -> (N, 32*32*3)
X_train = X_train.reshape(X_train.shape[0], -1) / 255.0
X_test = X_test.reshape(X_test.shape[0], -1) / 255.0

# One-hot encode labels
encoder = OneHotEncoder(sparse_output=False)
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)


# === Linear Classifier ===
class MyLinearClassifier:
    def __init__(self, input_dim, num_classes, learning_rate=0.01):
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.lr = learning_rate
        self.W = np.random.randn(num_classes, input_dim) * 0.01
        self.b = np.zeros((num_classes, 1))

    def softmax(self, z):
        z_stable = z - np.max(z, axis=1, keepdims=True)
        exp_z = np.exp(z_stable)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def cross_entropy_loss(self, y_hat, y):
        n = y.shape[0]
        return -np.sum(y * np.log(y_hat + 1e-8)) / n

    def forward(self, X):
        z = X @ self.W.T + self.b.T
        return self.softmax(z)

    def backward(self, X, y, y_hat):
        n = X.shape[0]
        dw = (y_hat - y).T @ X / n
        db = np.sum(y_hat - y, axis=0, keepdims=True).T / n
        return dw, db

    def update_params(self, dw, db):
        self.W -= self.lr * dw
        self.b -= self.lr * db

    def train(self, X, y, epochs=100):
        for epoch in range(epochs):
            y_hat = self.forward(X)
            loss = self.cross_entropy_loss(y_hat, y)
            dw, db = self.backward(X, y, y_hat)
            self.update_params(dw, db)
            if epoch % 10 == 0 or epoch == epochs - 1:
                acc = self.accuracy(X, y)
                print(f"Epoch {epoch}, Loss: {loss:.4f}, Acc: {acc:.4f}")

    def predict(self, X):
        y_hat = self.forward(X)
        return np.argmax(y_hat, axis=1)

    def accuracy(self, X, y):
        y_pred = self.predict(X)
        y_true = np.argmax(y, axis=1)
        return np.mean(y_pred == y_true)


# === Train the model ===
input_dim = X_train.shape[1]
num_classes = y_train.shape[1]

model = MyLinearClassifier(input_dim, num_classes, learning_rate=0.1)
model.train(X_train, y_train, epochs=50)

print("\nTest Accuracy:", model.accuracy(X_test, y_test))
