from math import *
from lupa import LuaRuntime
import time

import asyncio

lua = LuaRuntime()

def symbol_add(symbol: str, place):
    pos = place.cursorPosition()
    text = list(place.text())
    text.insert(pos, symbol)
    place.setText("".join(text))
    place.setCursorPosition(pos+1)

async def empty_x_range(place, expression):
    place.setText("range of x is empty")
    time.sleep(3)
    place.setText(expression)


async def generate_coords(place, range_, graph, expression):
    x_data = []
    y_data = []
    for i in range(range_, range_+11):
        try:
            i = i/10
            exp = expression.replace("x", str(i))

            res = eval(exp)
            x_data.append(i)
            y_data.append(res)
            #print(x_data[-1], y_data[-1])
        except ZeroDivisionError:
            g1 = graph.plot(x_data, y_data)
            x_data, y_data = [], []
            #print("!")
            continue
        except ValueError:
            graph.plot(x_data, y_data)
            x_data, y_data = [], []
            #print("!!")
            continue
        except SyntaxError:
            place.setText("Invalid sintax. Check your expression...")
            break
    else:
        graph.plot(x_data, y_data)

def execution(place, range_space, graph):
    ioloop = asyncio.get_event_loop()
    expression = str(place.text())
    expression = expression.replace("√", "pow")
    expression = expression.replace("sqr", "pow")
    expression = expression.replace("tg", "tan")
    x_data = []
    y_data = []
    range_: int = 0
    t1 = time.time()
    try:
        range_ = int(range_space.text())*10
        range__ = [i for i in range(-range_, range_)]
    except:
        range_space.setText("range of x is empty")
        pass
    graph.setLimits(xMin=-range_, xMax=range_,
                    yMin=-range_*1.5, yMax=range_*1.5)
    for i in range(-range_-10, range_-10, 10):

        ioloop.run_until_complete(generate_coords(place, i+10, graph, expression))



def break_expression(place):
    place.setText("")