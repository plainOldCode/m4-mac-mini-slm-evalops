package portfolio

import "strings"

type RouteDecision struct {
	Account string
	Reason  string
}

func RouteForSymbol(symbol string) RouteDecision {
	normalized := strings.ToUpper(strings.TrimSpace(symbol))
	switch {
	case strings.HasPrefix(normalized, "005930"), strings.HasPrefix(normalized, "SEC"):
		return RouteDecision{Account: "C", Reason: "Samsung Electronics route"}
	case strings.HasPrefix(normalized, "000660"), strings.HasPrefix(normalized, "SKH"):
		return RouteDecision{Account: "D", Reason: "SK Hynix route"}
	default:
		return RouteDecision{Account: "WATCH", Reason: "unknown symbol, no account matched"}
	}
}
