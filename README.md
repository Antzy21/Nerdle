# Nerdle

A small python project for helping solve the Nerdle puzzle.
https://nerdlegame.com/

## How to use

```powershell
PS > Python .\nerdle_solver.py

Enter results for equation: 9*8-7=65
--- Not used : 0 --- Used : 1 --- Used in place : 2 ---

Result for 9: 1
func: xxxxxxxx --- cant_use: [] --- posConds:  [['9'], [], [], [], [], [], [], []]

Result for *: 0
func: xxxxxxxx --- cant_use: ['*'] --- posConds:  [['9'], [], [], [], [], [], [], []]

Result for 8: 1
func: xxxxxxxx --- cant_use: ['*'] --- posConds:  [['9'], [], ['8'], [], [], [], [], []]

...
```

Calling with no parameters will assume that  `9*8-7=65` is used as the initial input.

Any args passed after that will be interpreted as equations to be analysed one at a time. e.g.
```powershell
Python .\nerdle_solver.py 12+34=46 6/3+9=11
```