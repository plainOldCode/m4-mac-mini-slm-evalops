function round2(value) {
  return Math.round((value + Number.EPSILON) * 100) / 100;
}

function summarizePortfolio(positions) {
  const totals = positions.reduce(
    (acc, position) => {
      const marketValue = position.quantity * position.currentPrice;
      const costBasis = position.quantity * position.averagePrice;
      acc.marketValue += marketValue;
      acc.costBasis += costBasis;
      if (position.currentPrice > position.averagePrice) {
        acc.winners.push(position.symbol);
      }
      return acc;
    },
    { marketValue: 0, costBasis: 0, winners: [] },
  );

  const profit = totals.marketValue - totals.costBasis;
  const profitRatePct = totals.costBasis === 0 ? 0 : (profit / totals.costBasis) * 100;

  return {
    marketValue: round2(totals.marketValue),
    costBasis: round2(totals.costBasis),
    profit: round2(profit),
    profitRatePct: round2(profitRatePct),
    winners: totals.winners.sort(),
  };
}

module.exports = { summarizePortfolio };
