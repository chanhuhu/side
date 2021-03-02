import React, { Suspense, useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import apiClient from "../api/client";
import Card from "../components/Card";
import ExternalLink from "../components/ExternalLink";
import Input from "../components/Input";
import LoadingImage from "../components/LoadingImage";
import SuspenseImage from "../components/SuspenseImage";
import Tag from "../components/Tag";
import "../styles/Home.css";
import { Trip } from "../types";
import useQuery from "../utils/useQuery";

export default function Home() {
  //#region state
  const [search, setSearch] = useState("");
  const [trips, setTrips] = useState<Trip[] | null>(null);
  //#endregion

  let query = useQuery();
  let history = useHistory();

  //#region useEffect
  useEffect(() => {
    (async () => {
      let res = await apiClient.get("trips");
      let trips = res.data;
      setTrips(trips);
      setSearch(query.get("keyword") ?? "");
    })();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    (async () => {
      let res = await apiClient.get(`trips?keyword=${search}`);
      let trips = res.data;
      setTrips(trips);
    })();
  }, [search]);
  //#endregion
  return (
    <div className="container">
      <h1 className="title">เที่ยวไหนดี</h1>
      <div className="search">
        <datalist id="trips">
          {trips?.map((trip) => (
            <option key={trip.eid} value={trip.title}></option>
          ))}
        </datalist>
        <Input
          list="trips"
          onChange={(e) => {
            const newSearch = e.target.value;
            setSearch(newSearch);
            history.push(`?keyword=${newSearch}`);
          }}
          value={search}
          placeholder="หาที่ท่องเที่ยวแล้วไปกัน..."
        />
      </div>
      <div className="cards">
        {trips?.map((trip) => {
          // todo find way to just deconstruct slice array for getting head, rest array of images
          let firstImageURL = trip.photos[0];
          let restImage = trip.photos.slice(1, trip.photos.length);
          return (
            <Card key={trip.eid}>
              {/**right part */}
              <div>
                <Suspense fallback={<LoadingImage />}>
                  <SuspenseImage
                    key={firstImageURL}
                    className="card-cover"
                    alt={trip.title}
                    src={firstImageURL}
                  />
                </Suspense>
              </div>
              {/**left part */}
              <div className="card-right">
                <ExternalLink
                  className="card-title"
                  target="_blank"
                  rel="noopener noreferrer"
                  href={trip.url}
                >
                  {trip.title}
                </ExternalLink>
                <p className="card-desc">{trip.description}</p>

                <ExternalLink
                  href={trip.url}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  อ่านต่อ
                </ExternalLink>

                <ul className="tags">
                  <span>หมวด -</span>
                  {trip.tags.map((tagName, i) => (
                    <Tag
                      key={tagName}
                      tagName={tagName}
                      onClick={() => {
                        setSearch(tagName);
                        history.push(`?keyword=${tagName}`);
                      }}
                    />
                  ))}
                </ul>
                <div className="card-images">
                  {restImage.map((photoURL) => (
                    <Suspense key={photoURL} fallback={<LoadingImage />}>
                      <SuspenseImage
                        className="card-image"
                        alt={trip.title}
                        src={photoURL}
                      />
                    </Suspense>
                  ))}
                </div>
              </div>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
