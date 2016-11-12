#!/usr/bin/env python

# Place code here you would like to execute. fN corresponds to the number of times the light was flicked.

import relay


def f3(gpio):
    print("3 was called!")
    relay.turn_on_relay_for(gpio, 30)


def f4():
    print("4 was called!")
    #relay.turn_on_relay_for(30)

def f5():
    print("5 was called!")


def f6():
    print("6 was called!")


def f7():
    print("7 was called!")


def f8():
    print("8 was called!")
