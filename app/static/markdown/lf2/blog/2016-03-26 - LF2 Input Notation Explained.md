# LF2 Input Notation Explained

Maybe you've come across some LF2 notation at some point already. If you know LF2 notation already, you might want to skip ahead to the extended LF2 notation.
The basic LF2 notation is quite quickly explained. It simply follows the keys you press and assigns a character to them.

## Basic Notation

| Symbol      | Meaning        |
| :---------- | :------------- |
| `D`         | Defend         |
| `A`         | Attack         |
| `J`         | Jump           |
| `>`         | Right          |
| `<`         | Left           |
| `^`         | Up             |
| `v`         | Down           |


### Examples

* Davis: `D^A` = dragon punch / uppercut
* any character: `>>` = run right
* any character: `<<` = run left
* Deep: `D^J` = leap attack (or: "BI-Sprung" ;- )

If you want to describe a whole series of moves, you'd have to write text in between LF2 notation to explain what happens after one move and before the next, because LF2 notation only covers so much. Admittedly you can write something like `Dennis: A + A + < + >> + A`. However, there are some issues with this:

This only possible, for moves, which consist of one part and thus always deal the same amount of damage, regardless of hitting early or late in the duration of execution of the move.

There is ambiguity in the notation. For example Deep's leap attack: `Deep: D^J + A` could also mean _"Do the leap attack jump, land on the ground and then press the attack button."_ You cannot refer to any single parts of moves. For example you cannot express, that the last hit of Dennis' DvA shall not hit.

## Extended Notation

The extended notation includes the elements of the _basic notation_, but also contains the following additional elements:

| Symbol                                                  | Meaning                                                                                                                                          |
| :----------                                             | :-------------                                                                                                                                   |
| `R`                                                     | run                                                                                                                                              |
| `_`                                                     | while the action belonging to the input immediately before the underscore is being executed, the action immediately after the underscore is done |
| `1X / 2X / 3X ...`                                      | only one part of a move, which consists of multiple equally damaging parts.                                                                      |
| `1` or `2` or `3` or ... or `1-2` or `1-2-3` or `2-3-4` | the move consists of multiple parts, which are not equally damaging, let the **n-th part** or parts hit, where **n** equals the numbers          |
| `L`                                                     | modifies the move immediately before the `L`, last part of a move, which consists of parts, which are not equally damaging                       |
| `F`                                                     | modifies the move immediately before the `F`, first part of a move, which consists of parts, which are not equally damaging                      |
| `N`                                                     | after a move the opponent still receives some damage, for example falling damage from Freeze's whirlwind.                                        |


### Examples

* `Deep: D^J_A` (leap, leap attack, 78 damage) compared to `D^J + A` (either leap, leap attack, 78 damage or leap, touch ground, attack, 35 damage)
* Only the last hit of `Deep: DvA`: `DvAL`
* Only the first three hits of `Dennis DvA`: `DvA1-2-3`

<br>
_(Created on 2016-03-26 by Zelphir Kaltstahl)_