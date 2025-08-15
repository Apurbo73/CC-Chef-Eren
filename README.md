# CC-Chef-Eren


---

### `for i in range(a)`

* **Starts at 0**, ends at `a-1`
* Runs `a` times
* Example with `a = 5`:

  ```
  i: 0, 1, 2, 3, 4
  ```
* Includes `0` in your logic (which affects even/odd counting).

---

### `for i in range(1, a+1)`

* **Starts at 1**, ends at `a`
* Also runs `a` times
* Example with `a = 5`:

  ```
  i: 1, 2, 3, 4, 5
  ```
* Skips `0`, includes `a` itself.

---

**In your case:**

* `range(a)` → counts numbers `0` to `a-1` → adds an *extra even number* (`0`).
* `range(1, a+1)` → counts numbers `1` to `a` → matches the problem’s “between 1 and a” expectation.

That’s why you got **43** with the first version but **45** with the second.

---



