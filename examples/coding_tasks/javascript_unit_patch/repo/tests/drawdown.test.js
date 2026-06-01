const assert = require("node:assert/strict");
const { maxDrawdownPct } = require("../src/drawdown");

assert.equal(maxDrawdownPct([]), 0);
assert.equal(maxDrawdownPct([100]), 0);
assert.equal(maxDrawdownPct([100, 105, 110]), 0);
assert.equal(maxDrawdownPct([100, 120, 90, 95]), 25);
assert.equal(maxDrawdownPct([240, 233, 230, 260, 221]), 15);
assert.equal(maxDrawdownPct([100, 99.5]), 0.5);

console.log("drawdown tests passed");
