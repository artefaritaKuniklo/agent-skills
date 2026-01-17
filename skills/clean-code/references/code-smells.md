# Code Smells Reference

Code smells indicate design weaknesses. Not bugs—code works—but suggest improvements.

## Application-Level

**Duplicated Code** - Extract to shared functions. Changes must only be made once.

**Shotgun Surgery** - One change requires edits across multiple files. Indicates poor cohesion. Move related code together.

## Class-Level

**Large Class** - Too many responsibilities. Violates SRP. Extract into focused classes.

**Long Parameter List** - 3+ params = refactor. Group params into objects or reduce responsibility.

**Magic Numbers** - Use named constants. Improves readability and maintainability.

## Method-Level

**Long Method** - Over 10-20 lines = split. Extract complex conditions into separate methods.

**Duplicate Code** - Extract identical patterns. Use inheritance or composition.

**Switch Statements** - Consider polymorphism instead. Reduces sprawl and improves OO design.

## Data-Level

**Data Clumps** - Variables used together = group into objects. Makes code clearer.

**Primitive Obsession** - Use objects instead of primitive types. Encapsulates behavior.

**Comments in Code** - Commented-out code clutters repo. Use version control. Delete it.

## Refactoring Techniques

**Extract Method** - Move code to separate function with clear name

**Extract Class** - Move related methods/fields to new class

**Inline Method** - Remove unnecessary indirection when method is trivial

**Rename** - Better names reveal intent and reduce need for comments

**Consolidate** - Merge similar/duplicate code into single implementation

## Additional Smells

**Shotgun Surgery** - One change needs edits across many classes. Move related code together.

**Divergent Change** - Class changes for different reasons. Split into focused classes.

**Feature Envy** - Method uses another class more than its own. Move to proper class.

**Data Clumps** - Variables always passed together. Group into object.
