use futures::executor::block_on;
use std::sync::{Arc, Mutex};

#[derive(Debug)]
struct State {
    counter: u64
}

fn main() {
    block_on(async_main())
}

async fn task1(shared_state: &Arc<Mutex<State>>) -> u8 {
    // shared_state.lock().unwrap().counter += 1;
    if let Ok(mut s) = shared_state.lock() {
        s.counter += 2;
    }

    println!("Hello, World");
    1
}

async fn task2(shared_state: &Arc<Mutex<State>>) -> u8 {
    // shared_state.lock().unwrap().counter += 2;
    if let Ok(mut s) = shared_state.lock() {
        s.counter += 1;
    }
    println!("Goodbye, World");
    2
}

async fn async_main() {
    let state = State {
        counter: 0
    };
    let shared_state = Arc::new(Mutex::new(state));
    let (result1, result2) = futures::join!(task1(&shared_state), task2(&shared_state));
    println!("Result1: {}, Result2: {}", result1, result2);
    println!("SharedState: {:?}", shared_state.lock().unwrap());
}
