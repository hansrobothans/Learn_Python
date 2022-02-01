import pywebio


age = pywebio.input.input("How old are you?",type=pywebio.input.NUMBER)

pywebio.output.put_text("your age is %d"%age)