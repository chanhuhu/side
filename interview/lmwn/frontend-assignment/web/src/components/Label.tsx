import React from "react";

export default function Label({ children }: { children?: React.ReactNode }) {
  return <label style={{ display: "block" }}>{children}</label>;
}
