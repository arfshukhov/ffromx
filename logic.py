from math import *
import time

import asyncio

import sys

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
        except ZeroDivisionError:
            g1 = graph.plot(x_data, y_data)
            x_data, y_data = [], []
            #print("!")
            continue
        except ValueError:
            graph.plot(x_data, y_data)
            x_data, y_data = [], []
            continue
    else:
        graph.plot(x_data, y_data)


def processing_expression(expression):
    expression = expression.replace("arcctg", "atan2")
    expression = expression.replace("arc", "a")
    expression = expression.replace("sqr", "pow")
    expression = expression.replace("√", "sqrt")
    expression = expression.replace("tg", "tan")

    return expression

def execution(place, range_space, graph, log_place):
    ioloop = asyncio.get_event_loop()
    expression = processing_expression(str(place.text()))
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
    try:
        for i in range(-range_-10, range_-10, 10):
            ioloop.run_until_complete(generate_coords(place, i+10, graph, expression))
    except SyntaxError as e:
        err_text = str(e)
        log_text = log_place.toPlainText()
        log_place.setText("\n".join([log_text, err_text]))
    except NameError as e:
        err_text = str(e)
        log_text = log_place.toPlainText()
        log_place.setText("\n".join([log_text, err_text]))
    except TypeError as e:
        err_text = str(e)
        log_text = log_place.toPlainText()
        log_place.setText("\n".join([log_text, err_text]))
    except Exception as e:
        err_text = str(e)
        log_text = log_place.toPlainText()
        log_place.setText("\n".join([log_text, err_text]))
    else:
        exp_text = str(place.text())
        log_text = log_place.toPlainText()
        log_place.setText("\n".join([log_text, "y="+exp_text]))


def break_expression(place):
    place.setText("")