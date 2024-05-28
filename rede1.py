import numpy as np

#Definir funções de ativação 
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Dados de entrada: [tamanho, quartos, idade]
X = np.array([
    [2104, 3, 20],
    [1600, 3, 15],
    [2400, 3, 10],
    [1416, 2, 20],
    [3000, 4, 5]
])

# Preços das casas correspondentes
y = np.array([
    [400],
    [330],
    [369],
    [232],
    [540]
])

#Normalizando os dados 

X = X / np.max(X, axis=0)
y = y / 1000  # Normalizando os preços para uma faixa menor

#Inicializar Pesos e Blases 

np.random.seed(42)
weights_input_hidden = np.random.uniform(size=(3, 5))
weights_hidden_output = np.random.uniform(size=(5, 1))

#Treinando Rede Neural 
## Implementa propagaçao direta pra calcular saidas da rede
## Calcula o erra e implementa a propagação reversa para ajustar pesos
## Utilizamos uma função linear na camada de saida adequada para problemas de regressão 
learning_rate = 0.01
epochs = 10000

for epoch in range(epochs):
    # Propagação direta
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = final_input  # Função linear na camada de saída

    # Cálculo do erro
    error = y - final_output

    # Propagação reversa
    d_final_output = error
    error_hidden_layer = d_final_output.dot(weights_hidden_output.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_output)

    # Atualização dos pesos
    weights_hidden_output += hidden_output.T.dot(d_final_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_output) * learning_rate

    if epoch % 1000 == 0:
        print(f'Epoch {epoch}, Error: {np.mean(np.abs(error))}')

print("Pesos finais:")
print(weights_input_hidden)
print(weights_hidden_output)

#Testar Rede Neural 
# Normalizando os dados de teste de forma semelhante aos dados de treinamento
X_test = np.array([
    [2000, 3, 20],
    [1500, 2, 15]
]) / np.max(X, axis=0)

# Realizando previsões
hidden_input = np.dot(X_test, weights_input_hidden)
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output)
final_output = final_input * 1000  # Desnormalizando os preços

print("Previsões:")
print(final_output)
