# SimplePerceptor
This repository contains a simple Python exercise designed to demonstrate how a Perceptron works. The perceptron is the fundamental building block of Artificial Neural Networks and Machine Learning.

The intent of this project is strictly educational.

The program acts as a basic decision-making system. It helps you decide whether you should go to a concert or stay at home based on 5 independent conditions (our inputs):

    Is the artist famous?

    Is the weather good?

    Are your friends coming?

    Is the food good?

    Is alcohol available?

The system evaluates these factors using a weighted sum:

    First, the program reads the "importance" of each condition from a text file named pesi_concerto.txt. These numbers represent the weights and the bias.

    Then, it asks the user to answer the 5 questions using 1 (Yes) or 0 (No).

    It multiplies each answer by its specific weight and adds the bias.

    Finally, it applies a step activation function: if the total score is strictly greater than our chosen threshold (1.5), the perceptron activates and tells you to go to the concert. If not, it tells you to stay home.
