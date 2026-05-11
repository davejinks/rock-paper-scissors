# ✂️ Rock, Paper, Scissors — CLI Game

This is one of the first Python programs I ever wrote on my own — no tutorial holding my hand, just me trying to figure things out.

It's a simple terminal game, but honestly it gave me more trouble than I expected. Getting the win conditions right with all those `and` / `or` combinations took a few attempts before it finally clicked. Looking back now it seems straightforward, but at the time it wasn't.

I'm posting this because I want to track where I started. A year from now, when I'm building things far more complex, I want to be able to look back at this and see the distance I've covered.

---

## What I was learning when I wrote this

These aren't textbook definitions — just what actually made sense to me after wrestling with the code.

**`while True` + `break` + `continue`**  
I didn't fully understand loops until I had to use them here. The idea that a loop can just run forever until *you* decide to stop it was weirdly satisfying once it worked. `break` exits completely, `continue` skips back to the top — small distinction, big difference in behaviour.

**Nested loops**  
Two `while True` loops sitting inside each other — one for the main menu, one for the actual game. The tricky part was realising each loop has its own `break`. Pressing Q only exits the inner loop and drops you back to the menu, not all the way out of the program. That took me a moment.

**Getting the win condition right**  
This was the part that took the longest. Three possible winning combinations, each needing two conditions to be true at the same time, all joined with `or`. I kept getting the logic tangled. Eventually I just wrote it out on paper first, then translated it:

```python
elif ((players_choice == "rock" and computer_choice == "scissors") or
      (players_choice == "paper" and computer_choice == "rock") or
      (players_choice == "scissors" and computer_choice == "paper")):
    print("you win!!!!!!")
```

**Input validation**  
Before I learned this, my programs would just crash on bad input. Adding a check before processing anything — and using `continue` to loop back instead of crashing — made the program feel much more solid.

**`random.choice()`**  
First time I actually used Python's standard library for something useful. Import the module, call the function, done. Simple but it felt like an unlock.

**f-strings**  
Once I found these I stopped doing messy string concatenation. Being able to drop variables directly into a print statement made everything cleaner.

**`.lower()` on input**  
Small thing, but it means typing `Rock` or `ROCK` works the same as `rock`. Makes the game actually usable.

---

## How to run it

```bash
python main.py
```

No installations needed. Pure Python, nothing external.

---

## How to play

1. Run the program
2. Pick **1** to start
3. Type `rock`, `paper`, or `scissors`
4. Type `Q` whenever you want to stop
5. Pick **2** from the main menu to exit fully

---

## What I'd do differently now

- Scores reset when you go back to the main menu — I'd fix that
- No way to play best-of-3 or best-of-5
- I'd probably break it into functions instead of one long block of code

---

## 👤 Author

**David Solomon Essien**  
Mechatronics Engineering Student — LASUSTECH, Lagos  
🔗 [github.com/davejinks](https://github.com/davejinks)
