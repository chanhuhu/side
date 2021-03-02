import { render } from "@testing-library/react";
import { Suspense } from "react";

import SuspenseImage from "./SuspenseImage";

const props = {
  src:
    "https://img.wongnai.com/p/1600x0/2019/12/25/54961e4326954765a80cd20e2044083d.jpg",
  width: 1,
  height: 1,
};

describe("components/SuspenseImage", () => {
  it("renders without crash", () => {
    const { baseElement } = render(
      <Suspense fallback={null}>
        <SuspenseImage {...props} />
      </Suspense>
    );

    expect(baseElement).toBeTruthy();
  });
});
