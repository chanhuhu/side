import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

describe("App.tsx", () => {
  it("renders without crash", async () => {
    const { baseElement } = render(<App />);

    expect(baseElement).toBeTruthy();
  });
});
