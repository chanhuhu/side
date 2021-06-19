use anyhow::{Context, Result};
use std::fmt::Debug;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
struct Cli {
    pattern: String,
    #[structopt(parse(from_os_str))]
    //#[structopt(short = "o", long = "output")]
    path: std::path::PathBuf,
}

fn main() -> Result<()> {
    let args = Cli::from_args();
    let reader = reader_from_path(&args.path)?;
    let lines = reader
        .lines()
        .flat_map(|res| res.ok())
        .collect::<Vec<String>>();
    find_matches(&lines, &args.pattern, &mut std::io::stdout())?;
    Ok(())
}

fn reader_from_path<P: AsRef<Path> + Debug>(path: P) -> Result<BufReader<File>, anyhow::Error> {
    let file =
        File::open(path.as_ref()).with_context(|| format!("Failed to read file {:?}", path))?;
    Ok(BufReader::new(file))
}

fn find_matches(lines: &Vec<String>, pattern: &str, mut writer: impl std::io::Write) -> Result<()> {
    for line in lines {
        if line.contains(pattern) {
            writeln!(writer, "{}", line)?;
        }
    }
    Ok(())
}

mod test {
    use super::*;
    #[test]
    fn find_a_match() {
        let mut result = Vec::new();
        let act = vec![String::from("lorem ipsum"), String::from("dolor sit amet")];
        find_matches(&act, "lorem", &mut result).unwrap();
        assert_eq!(result, b"lorem ipsum\n");
    }
}
