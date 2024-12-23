import random
# Main training function
def perceptron_training(true_w1: int, true_w2: int, true_w3: int, true_b: int, w1: float, w2: float, w3: float, b: float, training_speed: float):
    epoch = 0
    #cycle of 1000 epoch
    for i in range(100000):
        total_error = 0
        # 1 epoch = 100 random inputs for perceptron
        for j in range(100):
            x1 = random.randint(0, 1)
            x2 = random.randint(0, 1)
            x3 = random.randint(0, 1)
            #real output
            result = x1 * true_w1 + x2 * true_w2 + true_w3 * x3 + true_b

            if (result >= 0):
                result = 1
            elif (result < 0):
                result = 0
            #predicted output
            z = x1*w1 + x2*w2 + x3*w3 + b
            if(z >= 0):
                predicted_result = 1
            elif(z < 0):
                predicted_result = 0

            # Check if there is a mistake (positive or negative)
            error = result - predicted_result
            total_error += abs(error)
            #Changes a new weights | if error 0 or xi 0 than = 0
            w1 += x1*error*training_speed
            w2 += x2*error*training_speed
            w3 += x3 * error * training_speed
            b += error * training_speed

            print("w1:", w1, "w2:",w2, "w3:",w3, "b:",b, sep=" ")
            print("x1: ", x1,"x2: ", x2,"x3: ", x3, "result: ", result, sep=" ")
            print()
            epoch += 1
        if (total_error == 0):
            print(epoch)
            break;

def settings_start():
    # Setting all values
    true_w1, true_w2, true_w3, true_b = 1, 1, 2, -2
    w1, w2, w3, b = 0.5, 0.5, 0.5, -0.5
    training_speed = 0.1
    perceptron_training(true_w1, true_w2, true_w3, true_b, w1, w2, w3, b, training_speed)


settings_start()























