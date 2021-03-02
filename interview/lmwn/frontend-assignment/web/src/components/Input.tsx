import React, { forwardRef, InputHTMLAttributes } from "react";
import Label from "./Label";
import "./Input.css";

export type Props = {
  label?: string;
} & InputHTMLAttributes<HTMLInputElement>;

export default forwardRef<HTMLInputElement, Props>(
  ({ label, ...props }, ref) => {
    return (
      <Label>
        {label}
        <input
          className="input"
          style={{ display: "block", width: "100%" }}
          placeholder={label}
          ref={ref}
          {...props}
        />
      </Label>
    );
  }
);
