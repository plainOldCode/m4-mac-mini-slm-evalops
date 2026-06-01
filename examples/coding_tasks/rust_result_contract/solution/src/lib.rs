pub struct Holding {
    pub symbol: String,
    pub quantity: u32,
}

pub fn parse_holding(input: &str) -> Result<Holding, String> {
    let (symbol_raw, quantity_raw) = input
        .split_once(':')
        .ok_or_else(|| "missing colon".to_string())?;
    let symbol = symbol_raw.trim().to_uppercase();
    if symbol.is_empty() {
        return Err("empty symbol".to_string());
    }
    let quantity = quantity_raw
        .trim()
        .parse::<u32>()
        .map_err(|_| "invalid quantity".to_string())?;
    Ok(Holding { symbol, quantity })
}
