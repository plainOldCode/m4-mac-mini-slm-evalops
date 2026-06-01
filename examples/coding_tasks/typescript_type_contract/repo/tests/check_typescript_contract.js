const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const source = fs.readFileSync(path.join(__dirname, "..", "src", "quoteSummary.ts"), "utf8");

assert.match(source, /export\s+interface\s+Quote\b/, "Quote interface must be exported");
assert.match(source, /symbol\s*:\s*string/, "Quote.symbol must be a string");
assert.match(source, /previousClose\s*:\s*number/, "Quote.previousClose must be a number");
assert.match(source, /currentPrice\s*:\s*number/, "Quote.currentPrice must be a number");
assert.match(source, /export\s+interface\s+QuoteSummary\b/, "QuoteSummary interface must be exported");
assert.match(source, /direction\s*:\s*['\"]up['\"]\s*\|\s*['\"]down['\"]\s*\|\s*['\"]flat['\"]/, "direction must be a string-literal union");
assert.match(source, /export\s+function\s+summarizeQuote\s*\(\s*quote\s*:\s*Quote\s*\)\s*:\s*QuoteSummary/, "summarizeQuote must use explicit Quote and QuoteSummary types");
assert.doesNotMatch(source, /\bany\b/, "Do not use any");
assert.match(source, /Math\.round/, "Round numeric outputs to two decimals");
assert.match(source, /previousClose\s*===\s*0|previousClose\s*!==\s*0|previousClose\s*==\s*0/, "Handle zero previousClose explicitly");

console.log("typescript contract checks passed");
