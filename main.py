from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load(model_directory)

interpreter.parse(u"The text I want to understand")