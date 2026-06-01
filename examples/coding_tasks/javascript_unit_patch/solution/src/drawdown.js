function round2(value) {
  return Math.round((value + Number.EPSILON) * 100) / 100;
}

function maxDrawdownPct(prices) {
  if (prices.length < 2) {
    return 0;
  }

  let peak = prices[0];
  let maxDrawdown = 0;
  for (const price of prices) {
    if (price > peak) {
      peak = price;
    }
    if (peak > 0) {
      maxDrawdown = Math.max(maxDrawdown, ((peak - price) / peak) * 100);
    }
  }
  return round2(maxDrawdown);
}

module.exports = { maxDrawdownPct };
