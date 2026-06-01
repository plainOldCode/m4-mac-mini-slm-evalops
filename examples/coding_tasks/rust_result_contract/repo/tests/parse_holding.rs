use rust_result_contract::parse_holding;

#[test]
fn parses_valid_holding() {
    let holding = parse_holding(" skh : 20 ").expect("holding should parse");
    assert_eq!(holding.symbol, "SKH");
    assert_eq!(holding.quantity, 20);
}

#[test]
fn rejects_missing_colon() {
    assert!(parse_holding("SKH 20").is_err());
}

#[test]
fn rejects_empty_symbol() {
    assert!(parse_holding(":20").is_err());
}

#[test]
fn rejects_invalid_quantity() {
    assert!(parse_holding("SEC:abc").is_err());
}
