import { render } from "@testing-library/react";

import Tag from "./Tag";

describe("components/Tag", () => {
  it("renders without crash", () => {
    const { baseElement } = render(<Tag tagName="u dumb" />);

    expect(baseElement).toBeTruthy();
  });

  it("contain class", () => {
    const { container } = render(<Tag className="hello" tagName="u dumb" />);

    expect(container.firstChild).toHaveClass("hello");
  });
});
