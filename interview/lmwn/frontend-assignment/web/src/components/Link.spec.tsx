import { render } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import Link from "./Link";

describe("components/Link", () => {
  it("renders without crash", () => {
    const { baseElement } = render(
      <BrowserRouter>
        <Link to="#" />
      </BrowserRouter>
    );

    expect(baseElement).toBeTruthy();
  });
});
