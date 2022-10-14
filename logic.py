from math import *

def symbol_add(symbol: str, place):
    pos = place.cursorPosition()
    text = list(place.text())
    text.insert(pos, symbol)
    place.setText("".join(text))
    place.setCursorPosition(pos+1)


def execution(place, range_space, graph):
    expression = str(place.text())
    expression = expression.replace("√", "pow")
    expression = expression.replace("sqr", "pow")
    x_data = []
    y_data = []
    range_ = int(range_space.text())
    graph.setLimits(xMin=-range_, xMax=range_,
                             yMin=-range_, yMax=range_)
    print(range_)
    for i in range(-range_, range_+1):
        print(i)
        try:
            exp = expression.replace("x", str(i))
            #print("exp=", exp)
            #(exec(f"from math import *; x_data.append(i); y_data.append({exp})"))
            res = eval(exp)
            x_data.append(i)
            y_data.append(res)
            print(x_data[-1], y_data[-1])
        except ZeroDivisionError:
            #g1 = graph.plot(x_data, y_data)
            #x_data, y_data = [], []
            #print("!!")
            continue
        except ValueError:
            #g2 = graph.plot(x_data, y_data)
            #x_data, y_data = [], []
            #print("!!")
            continue
        except SyntaxError:
            place.setText("Invalid sintax. Check your expression...")
            break
    #print(x_data, y_data)
    g3 = graph.plot(x_data, y_data)
    #print(1323333)

def break_expression(place):
    place.setText("")