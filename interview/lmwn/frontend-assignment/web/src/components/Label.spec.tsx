import { render } from "@testing-library/react";
import Label from "./Label";

describe("components/Label", () => {
  it("renders without crash", () => {
    const { baseElement } = render(<Label />);

    expect(baseElement).toBeTruthy();
  });

  it("contains text", () => {
    const { getByText } = render(<Label>Hello</Label>);

    expect(getByText("Hello")).toBeTruthy();
  });

  it("contains element", () => {
    const { getByTestId } = render(
      <Label>
        <div data-testid="div" />
      </Label>
    );

    expect(getByTestId("div")).toBeTruthy();
  });
});
