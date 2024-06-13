import random
import time

output_file = 'tanque_1.txt'


def generate_data():
    temperatura = 32.0 + random.uniform(-1.0, 7.0)
    velocidade = random.randint(25, 100)
    return f"temperatura : {int(temperatura)}  \nvelocidade do cooler : {velocidade} %"


def read_data():
    try:
        count = 0
        with open(output_file, 'w') as file:
            #Gera um arquivo com linhas definadas para evitar mair uso da memória 
            while count < 10:
                data = generate_data()
                print(data)
                file.write(data + '\n')
                file.flush()
                count += 1
                time.sleep(1)
    except KeyboardInterrupt:
        print("Leitura interrompida pelo usuário")


if __name__ == "__main__":
    read_data()
