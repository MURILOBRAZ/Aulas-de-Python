import tensorflow as tf  # Importa a biblioteca TensorFlow para trabalhar com aprendizado de máquina.
import numpy as np       # Importa a biblioteca NumPy para operações matemáticas eficientes.

# Define os dados de temperatura em Celsius e Fahrenheit como arrays NumPy.
celsius    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit = np.array([-40,  14, 32, 46.4, 59, 71.6, 100],  dtype=float)

# Cria uma camada densa (fully connected) com 1 unidade, esperando 1 valor de entrada.
l1 = tf.keras.layers.Dense(units=1, input_shape=[1])

# Cria um modelo sequencial (sequência linear de camadas) e adiciona a camada l1.
model = tf.keras.Sequential([l1])

# Compila o modelo, especificando a função de perda e o otimizador a serem utilizados.
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.05))

# Treina o modelo com os dados de entrada (celsius) e saída desejada (fahrenheit) por 500 épocas.
# O argumento verbose=False suprime a saída detalhada durante o treinamento.
history = model.fit(celsius, fahrenheit, epochs=2000, verbose=False)

# Imprime uma mensagem indicando que o treinamento do modelo foi concluído.
print("Finished training the model")

# Importa a biblioteca Matplotlib para plotar gráficos.
import matplotlib.pyplot as plt

# Configura os rótulos do eixo x e y do gráfico.
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")

# Plota o gráfico da perda (loss) ao longo das épocas durante o treinamento.
plt.plot(history.history['loss'])

# Salva o gráfico em um arquivo de imagem (por exemplo, formato PNG).
plt.savefig('loss_plot.png')

# Imprime a previsão do modelo para uma entrada de 100 graus Celsius.
print(model.predict([100]))

# Imprime os pesos da camada l1 após o treinamento.
print("These are the layer variables: {}".format(l1.get_weights()))
