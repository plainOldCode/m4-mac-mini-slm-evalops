function maxDrawdownPct(prices) {
  if (prices.length < 2) {
    return 0;
  }
  return Math.max(...prices) - Math.min(...prices);
}

module.exports = { maxDrawdownPct };
