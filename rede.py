import numpy as np
#Definindo funções de ativação 
def sigmoid(x):
    return 1/ (1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

#Preparando os dados 

#--------------------------
#Dados de entrada (4 amostras, 2 características)
X = np.array([[0, 0], [0, 1], [1,0], [1,1]])

#Saídas esperadas (4 amostras, 1 saída)
y = np.array([[0], [1], [1], [0]])

#---------------------------

#Inicializar Pesos e Blases 

#--------------------------
np.random.seed(1)
weights_input_hidden = np.random.uniform(size=(2, 2))
weights_hidden_output = np.random.uniform(size=(2, 1))
#--------------------------

#Propagação Direta e Reversa
learning_rate = 0.1

for epoch in range(10000):
    # Propagação direta
    hidden_input = np.dot(X, weights_input_hidden) 
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)
#--------------------------

    # Cálculo do erro
    error = y - final_output
#--------------------------

    # Propagação reversa
    d_final_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = d_final_output.dot(weights_hidden_output.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_output)
#--------------------------

    # Atualização dos pesos
    weights_hidden_output += hidden_output.T.dot(d_final_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_output) * learning_rate
#--------------------------

print("Pesos finais:")
print(weights_input_hidden)
print(weights_hidden_output)
#--------------------------

# Testando a rede
print("Saída prevista:")
hidden_input = np.dot(X, weights_input_hidden)
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output)
final_output = sigmoid(final_input)
print(final_output)

#--------------------------
