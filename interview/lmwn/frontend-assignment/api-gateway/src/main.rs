use actix_cors::Cors;
use actix_web::{App, HttpResponse, HttpServer, Responder, get, http::Method, http::header, post, web};
use serde::{Deserialize,Serialize};
use actix_web::middleware::Logger;

#[macro_use]
extern crate log;

use env_logger::Env;

#[derive(Clone, Debug, Deserialize)]
struct RequestParams {
    keyword: Option<String>
}

#[derive( Clone, Debug, Deserialize, Serialize,Eq, Ord, PartialEq, PartialOrd)]
struct Trip {
    title: String,
    eid: String,
    url: String,
    description: String,
    photos: Vec<String>,
    tags: Vec<String>
}

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

async fn manual_hello() -> impl Responder {
    HttpResponse::Ok().body("Hey there!")
}

#[get("/trips")]
async fn get_trips(request_params: web::Query<RequestParams>) -> impl Responder {
    let client = reqwest::Client::new();
    let response = client.get("http://localhost:9000/trips").send().await.expect("Failed to executed request.");
    let trips: Vec<Trip> = response.json().await.expect("Failed to converted json.");
    let result = match &request_params.keyword {
        // result = if keyword and then get trips by keyword with intersection and insensitive search 
        Some(keyword) => {
            // todo should not clone trips and use generic predicate instead hard code
            let get_by_title: Vec<Trip> = trips.clone().into_iter().filter(|trip| trip.title.to_lowercase().contains(&keyword.to_lowercase())).collect();
            let get_by_desc: Vec<Trip> = trips.clone().into_iter().filter(|trip| trip.description.to_lowercase().contains(&keyword.to_lowercase())).collect();
            let get_by_tags: Vec<Trip> = trips.clone().into_iter().filter(|trip| {
                let lowered_case_tags: Vec<String> = trip.tags.iter().map(|tag| tag.to_lowercase()).collect();
                lowered_case_tags.contains(&keyword.to_lowercase())
            }).collect();
            let mut filtered_trips = [get_by_tags, get_by_desc, get_by_title].concat();
            filtered_trips.sort_by(|a,b| a.eid.cmp(&b.eid));
            filtered_trips.dedup();
            filtered_trips
        }
        // otherwise return all trips
        None => trips,
    };
    HttpResponse::Ok().json(result)
    
}


#[actix_rt::main]
async fn main() -> std::io::Result<()> {

    HttpServer::new(move || {
        let env = Env::default().filter_or("MY_LOG_LEVEL", "trace").write_style_or("MY_LOG_STYLE", "always");
        env_logger::init_from_env(env);
        let cors = Cors::default()
            .allowed_origin("http://localhost:3000")
            .allowed_methods(vec![Method::GET, Method::OPTIONS, Method::POST])
            .allowed_headers(vec![header::AUTHORIZATION, header::ACCEPT])
            .allowed_header(header::CONTENT_TYPE)
            .supports_credentials()
            .max_age(86400);

        App::new()
            .wrap(Logger::default())
            .wrap(cors)
            .service(hello)
            .service(echo)
            .service(get_trips)
            .route("/hey", web::get().to(manual_hello))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}