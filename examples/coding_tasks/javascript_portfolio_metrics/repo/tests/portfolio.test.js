const assert = require("node:assert/strict");
const { summarizePortfolio } = require("../src/portfolio");

const sample = [
  { symbol: "SKH", quantity: 2, averagePrice: 1700000, currentPrice: 2330000 },
  { symbol: "SEC", quantity: 10, averagePrice: 281000, currentPrice: 340000 },
  { symbol: "CASH", quantity: 1, averagePrice: 1000000, currentPrice: 1000000 },
];

assert.deepEqual(summarizePortfolio(sample), {
  marketValue: 9060000,
  costBasis: 7210000,
  profit: 1850000,
  profitRatePct: 25.66,
  winners: ["SEC", "SKH"],
});

assert.deepEqual(summarizePortfolio([]), {
  marketValue: 0,
  costBasis: 0,
  profit: 0,
  profitRatePct: 0,
  winners: [],
});

console.log("portfolio metrics tests passed");
