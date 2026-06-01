package portfolio

import "testing"

func TestRouteForSymbol(t *testing.T) {
	tests := []struct {
		symbol  string
		account string
	}{
		{"005930.KS", "C"},
		{"sec-local", "C"},
		{"000660.KS", "D"},
		{"skh-main", "D"},
		{"ABC", "WATCH"},
	}

	for _, test := range tests {
		got := RouteForSymbol(test.symbol)
		if got.Account != test.account {
			t.Fatalf("RouteForSymbol(%q).Account = %q, want %q", test.symbol, got.Account, test.account)
		}
		if got.Reason == "" {
			t.Fatalf("RouteForSymbol(%q).Reason should not be empty", test.symbol)
		}
	}
}
