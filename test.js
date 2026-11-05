/**
 * Simple test helpers for sandbox experiments.
 */

function add(a, b) {
  return a + b;
}

function greet(name = "world") {
  return `Hello, ${name}!`;
}

module.exports = { add, greet };

if (require.main === module) {
  console.log(greet("sandbox"));
  console.log("2 + 3 =", add(2, 3));
}
