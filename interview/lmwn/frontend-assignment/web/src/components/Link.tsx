import React from "react";
import { Link as RouterLink, LinkProps } from "react-router-dom";

export default function Link(props: LinkProps) {
  return <RouterLink className="link" {...props} />;
}
