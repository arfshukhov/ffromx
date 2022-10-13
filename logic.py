from math import *

def symbol_add(symbol: str, place):
    pos = place.cursorPosition()
    text = list(place.text())
    text.insert(pos, symbol)
    place.setText("".join(text))
    place.setCursorPosition(pos+1)


def execution(place, range_space, graph):
    expression = str(place.text())
    expression = expression.replace("√", "sqrt")
    expression = expression.replace("sqr", "pow")
    x_data = []
    y_data = []
    range_ = int(range_space.text())
    print(range_)
    for i in range(-range_, range_+1):
        exp = expression.replace("x", str(i))
        print("exp=",exp)
        try:
            #(exec(f"from math import *; x_data.append(i); y_data.append({exp})"))
            res = eval(exp)
            x_data.append(i)
            y_data.append(res)
            #print(x_data, y_data)
        except ZeroDivisionError:
            g1= graph.plot(x_data, y_data)
            x_data, y_data = [], []
            print("!!")
        except SyntaxError:
            place.setText("Invalid sintax. Check your expression...")
            break
    print(x_data, y_data)
    g2=graph.plot(x_data, y_data)
    print(1323333)

def break_expression(place):
    place.setText("")