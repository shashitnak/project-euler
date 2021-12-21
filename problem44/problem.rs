#![feature(int_abs_diff)]
use std::collections::HashSet;

const N: usize = 5000;

struct Pentagonal {
    n: usize,
}

impl Pentagonal {
    fn new() -> Self {
        Pentagonal { n: 1 }
    }
}

impl Iterator for Pentagonal {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        let value = (self.n * (3 * self.n - 1)) / 2;
        self.n += 1;
        Some(value)
    }
}

fn main() {
    let pentagonals: HashSet<usize> = Pentagonal::new().take(N).collect();
    let result = Pentagonal::new()
        .take(N)
        .flat_map(|p| {
            Pentagonal::new()
                .take(N)
                .map(move |n| (n, p))
                .filter_map(|(p1, p)| {
                    (pentagonals.contains(&(p1.abs_diff(p))) && pentagonals.contains(&(p1 + p)))
                        .then(|| p1.abs_diff(p))
                })
        })
        .min()
        .unwrap();
    println!("D = {}", result);
}
