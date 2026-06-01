export interface Quote {
  symbol: string;
  previousClose: number;
  currentPrice: number;
}

export interface QuoteSummary {
  symbol: string;
  change: number;
  changePct: number;
  direction: "up" | "down" | "flat";
}

function round2(value: number): number {
  return Math.round((value + Number.EPSILON) * 100) / 100;
}

export function summarizeQuote(quote: Quote): QuoteSummary {
  const change = quote.currentPrice - quote.previousClose;
  const changePct = quote.previousClose === 0 ? 0 : (change / quote.previousClose) * 100;
  const direction: QuoteSummary["direction"] = change > 0 ? "up" : change < 0 ? "down" : "flat";

  return {
    symbol: quote.symbol,
    change: round2(change),
    changePct: round2(changePct),
    direction,
  };
}
