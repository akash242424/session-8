# Session 08: Testing & Debugging with AI

This repository contains the Classwork (CW) and Homework (HW) assignments for **Prompt Engineering for C and C++ (BCO610A)**. The primary focus of this session is executing a strict **Red Before Green** testing workflow[cite: 21], proving fixes through specification-driven tests, and identifying AI-generated testing traps ("Misleading Green")[cite: 26].

---

## 📁 Classwork (CW): Student Grading Utility

The `student_utils.py` module calculates averages and assigns grades based on a specific banding rubric. It originally contained three distinct bug classes which were identified and fixed using specification-driven testing[cite: 29].

### Bug Fix Audit Table

| Bug Class | Broken Logic | Applied Fix | Spec Test That Exposed It |
| :--- | :--- | :--- | :--- |
| **Arithmetic**[cite: 29] | Divided by `len(marks) - 1`[cite: 28] | Changed to divide by `len(marks)` to prevent zero-division crashes[cite: 10, 20]. | `test_single_element_no_crash` |
| **Boundary**[cite: 29] | Used `if mark > PASS_MARK` (40)[cite: 28] | Changed to `>= PASS_MARK` to include exactly 40[cite: 10, 20]. | `test_exactly_at_pass_mark` |
| **Unreachable Branch**[cite: 29] | `>= 90` checked after `>= 60`[cite: 28] | Moved the `>= 90` distinction check to the top of the `if/elif` chain[cite: 10, 20]. | `test_top_band` |

### CW Testing Details
* **Coverage:** Validates ordinary arithmetic, single-element arrays without crashing, strict boundary checks at pass marks, and complete grading bands[cite: 23, 31].
* **Run Command:** `python CW/test_student_utils.py`[cite: 7, 17]
* **Test Count:** 10 total tests (9 specification-driven, 1 student-designed)[cite: 7, 17].

---

## 📁 Homework (HW): E-Commerce Discount Calculator

The `discount.py` module applies sequential discounts based on cart totals and VIP status. Three bugs were intentionally seeded into this custom program to demonstrate test failure (Red Stage) before applying implementation fixes (Green Stage)[cite: 4, 14].

### Custom Specification
1. `cart_total < 0` raises `ValueError`.
2. `0 - 50` returns `0.0` (0%) discount.
3. `51 - 100` returns `0.10` (10%) discount.
4. `> 100` returns `0.20` (20%) discount.
5. `is_vip=True` adds `0.05` (5%) to the discount.
6. Max total discount is capped at `0.25` (25%).

### Seeded Bug Audit Table

| Bug Class | Seeded Bug | Applied Fix | Spec Test That Exposed It |
| :--- | :--- | :--- | :--- |
| **Boundary** | Used `>= 50` for 10% discount | Changed to `> 50` so exactly 50 gets 0%. | `test_exactly_fifty_gets_zero_discount` |
| **Unreachable Branch** | `> 100` checked after `> 50` | Moved `> 100` to the top of the discount tier logic. | `test_one_twenty_gets_twenty_percent` |
| **Arithmetic** | VIP added `0.50` instead of `0.05` | Changed addition strictly to `0.05`. | `test_vip_gets_five_percent_bonus` |

### HW Testing Details
* **Coverage:** Verifies `ValueError` exception bounds, exact boundaries for discount tiers, correct routing of highest-tier discounts, and accurate floating-point arithmetic for VIP bonuses and maximum caps.
* **Run Command:** `python HW/test_discount.py`
* **Test Count:** 6 custom specification-driven tests.

---

## 🧪 Experiment Results: The "Misleading Green" Trap

During the homework, an experiment was conducted where AI was prompted to generate tests based *only* on the broken `discount.py` implementation code instead of the specification.

**Result:** The AI-generated tests passed immediately on the broken code without any fixes applied. The AI assumed the bugs were intentional features (e.g., asserting that a $50 cart *should* get 10% off due to the seeded boundary bug). 

**Conclusion:** This demonstrates the danger of **Misleading Green**[cite: 26]. Fixing is not proving[cite: 30]. Evidence (a test failing first) is stronger than confidence, and a test that never fails proves nothing[cite: 29, 30]. Tests must always be written from the specification, completely independent of the implementation code[cite: 26].
