pub fn production_rate_per_hour(speed: u8) -> f64 {
    let success_rate = match speed {
        0..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        _ => unreachable!(),
    };
    speed as f64 * (221f64 * success_rate)
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / 64f64).round() as u32
}
