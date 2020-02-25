# PDDLc
*Bora's PDDL Companion*

**PDDLc** is a small *companion* script that helps you **check** (syntax) and
**plan** using PDDL.

Developed for the [2D - Reasoning and Agents](https://www.inf.ed.ac.uk/teaching/courses/inf2d/) course in [The University of Edinburgh](https://www.ed.ac.uk/).


## Usage
1. Ensure that you have a working Java 8 runtime (already provided on DICE).
2. Clone the repository.
   - OR, you can also selectively download `pddlc.py` and `pddl4j-X.X.X.jar`
     files. You must then ensure that the files are in the same directory.

### Checking Syntax
```
python3 pddlc.py check domain.pddl problem.pddl
```

- Checking (for some unknown reason) might fail on completely valid inputs (such
  as the *blocks-world* example in the assignment) so I advise you to check
  syntax only if you are getting parsing errors from the planner.

### Planning
```
python3 pddlc.py plan domain.pddl problem.pddl
```


## License
ISC License, see [LICENSE](./LICENSE) for details.

**This project relies on:**

- [PDDL4J](https://github.com/pellierd/pddl4j), licensed under LGPL-3.0.
- [solver.planning.domains](http://solver.planning.domains/).
