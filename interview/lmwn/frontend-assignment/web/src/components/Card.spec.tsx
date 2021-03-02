import { render } from "@testing-library/react";

import Card from "./Card";

describe("components/Tag", () => {
  it("renders without crash", () => {
    const { baseElement } = render(<Card>u dumb</Card>);

    expect(baseElement).toBeTruthy();
  });

  it("contain class", () => {
    const { container } = render(<Card className="hello">u dumb</Card>);

    expect(container.firstChild).toHaveClass("hello");
  });
});
