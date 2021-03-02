import { render } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import ExternalLink from "./ExternalLink";

describe("components/ExternalLink", () => {
  it("renders without crash", () => {
    const { baseElement } = render(<ExternalLink href="/" />);

    expect(baseElement).toBeTruthy();
  });

  it("contains text", () => {
    const { getByText } = render(<ExternalLink href="/">Hello</ExternalLink>);

    expect(getByText("Hello")).toBeTruthy();
  });

  it("contains element", () => {
    const { getByTestId } = render(
      <ExternalLink href="/">
        <div data-testid="div" />
      </ExternalLink>
    );

    expect(getByTestId("div")).toBeTruthy();
  });

  it("contains color", () => {
    const { container } = render(
      <ExternalLink href="/" color="text-blue-400" />
    );

    expect(container.firstChild).toHaveAttribute("color", "text-blue-400");
  });
});
