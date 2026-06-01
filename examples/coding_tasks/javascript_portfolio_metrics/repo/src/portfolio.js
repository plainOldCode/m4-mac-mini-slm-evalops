function summarizePortfolio(positions) {
  return {
    marketValue: positions.length,
    costBasis: 0,
    profit: 0,
    profitRatePct: 0,
    winners: [],
  };
}

module.exports = { summarizePortfolio };
