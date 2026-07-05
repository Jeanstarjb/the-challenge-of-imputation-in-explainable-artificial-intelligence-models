import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleExplainableModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleExplainableModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

def impute_missing_values(data, strategy='mean'):
    """
    Impute missing values in the dataset.
    :param data: numpy array with missing values (np.nan)
    :param strategy: 'mean', 'median', or 'zero'
    :return: numpy array with imputed values
    """
    if strategy == 'mean':
        imputed_data = np.where(np.isnan(data), np.nanmean(data, axis=0), data)
    elif strategy == 'median':
        imputed_data = np.where(np.isnan(data), np.nanmedian(data, axis=0), data)
    elif strategy == 'zero':
        imputed_data = np.where(np.isnan(data), 0, data)
    else:
        raise ValueError("Unknown imputation strategy. Use 'mean', 'median', or 'zero'.")
    return imputed_data

def generate_dummy_data(num_samples=100, num_features=5, missing_rate=0.1):
    """
    Generate dummy data with missing values.
    :param num_samples: Number of samples
    :param num_features: Number of features
    :param missing_rate: Fraction of missing values
    :return: numpy array with missing values
    """
    data = np.random.rand(num_samples, num_features)
    mask = np.random.rand(*data.shape) < missing_rate
    data[mask] = np.nan
    return data

def train_model(model, data, labels, epochs=100, lr=0.01):
    """
    Train the model on the given data.
    :param model: PyTorch model
    :param data: Training data
    :param labels: Training labels
    :param epochs: Number of epochs
    :param lr: Learning rate
    """
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")

if __name__ == '__main__':
    # Generate dummy data
    np.random.seed(42)
    torch.manual_seed(42)
    num_samples = 100
    num_features = 5
    missing_rate = 0.2
    
    data = generate_dummy_data(num_samples, num_features, missing_rate)
    labels = np.random.rand(num_samples, 1)
    
    # Impute missing values
    imputed_data = impute_missing_values(data, strategy='mean')
    
    # Convert data to PyTorch tensors
    data_tensor = torch.tensor(imputed_data, dtype=torch.float32)
    labels_tensor = torch.tensor(labels, dtype=torch.float32)
    
    # Define and train the model
    input_dim = num_features
    hidden_dim = 10
    output_dim = 1
    model = SimpleExplainableModel(input_dim, hidden_dim, output_dim)
    
    train_model(model, data_tensor, labels_tensor, epochs=100, lr=0.01)
    
    # Test the model with a sample input
    test_sample = torch.tensor([imputed_data[0]], dtype=torch.float32)
    model.eval()
    prediction = model(test_sample)
    print(f"Test sample prediction: {prediction.item()}")